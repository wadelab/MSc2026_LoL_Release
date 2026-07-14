"""Control analysis: is the behavioural peak phase just a readout of play density?

For each retained server we recompute every player's PC1/PC2 24 h peak phase
keyed by account, merge it with that player's mean play hour (circular mean of
their game times), and measure the circular association among behaviourally
FDR-significant players. A strong positive association would mean the fitted
"behavioural rhythm" merely tracks *when* the player is online (a play-density /
time-of-day sampling effect); a near-zero association means the phase is a
property of behaviour, independent of the play schedule.

Writes results/GRAND/grand_phase_vs_playtime.csv (per-server and pooled rows).

Usage:  uv run python analysis_phase_vs_playtime.py
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from grand_analysis import PHASE_ANALYSIS_EXCLUDE
from riot_analysis import (
    AnalysisConfig,
    GOOD_PCA_COLS,
    add_time_normalized_features,
    benjamini_hochberg_mask,
    compute_pca,
    connect_read_only,
    filter_hourly_window,
    filter_metric_outliers,
    load_hourly_metrics,
    load_top_players,
    player_phase,
    project_player_pca,
)
from server_timezones import utc_offset_hours

ANALYSIS_PLATFORMS = ["BR1", "EUN1", "EUW1", "JP1", "LA1", "LA2", "NA1", "OC1"]
METRIC_COLS = {"PC1": "perf_factor_pc1", "PC2": "perf_factor_pc2"}


def circular_correlation(a_hours: np.ndarray, b_hours: np.ndarray) -> float:
    """Jammalamadaka-Sarma circular correlation for two hour-of-day vectors."""

    a = np.asarray(a_hours, dtype=float) * (2.0 * np.pi / 24.0)
    b = np.asarray(b_hours, dtype=float) * (2.0 * np.pi / 24.0)
    a_bar = np.arctan2(np.sin(a).mean(), np.cos(a).mean())
    b_bar = np.arctan2(np.sin(b).mean(), np.cos(b).mean())
    num = float((np.sin(a - a_bar) * np.sin(b - b_bar)).sum())
    den = float(np.sqrt((np.sin(a - a_bar) ** 2).sum() * (np.sin(b - b_bar) ** 2).sum()))
    return num / den if den > 0 else float("nan")


def player_peak_phases(conn, platform: str) -> pd.DataFrame:
    """Per-player PC1/PC2 peak hour, joint p-value and coverage span, by account."""

    config = AnalysisConfig(platform=platform)
    offset = int(utc_offset_hours(platform))

    hourly = load_hourly_metrics(conn, platform)
    hourly = filter_hourly_window(hourly, config.max_hour_limit)
    hourly, numeric_cols = add_time_normalized_features(hourly)
    hourly = filter_metric_outliers(hourly, numeric_cols)
    pca = compute_pca(hourly, numeric_cols, GOOD_PCA_COLS)

    _, player_data = load_top_players(conn, platform, config.top_n_players)
    player_data = project_player_pca(player_data, numeric_cols, pca)

    rows = []
    for account, group in player_data.groupby("ACCOUNTID", sort=False):
        rec = {"ACCOUNTID": str(account)}
        ts = pd.to_numeric(group["TIMESTAMP"], errors="coerce")
        rec["span_days"] = float((ts.max() - ts.min()) / 3600000.0 / 24.0)
        for metric, col in METRIC_COLS.items():
            fit = player_phase(group, col, offset)
            rec[f"{metric}_peak_h"] = np.nan if fit is None else fit[0]
            rec[f"{metric}_p"] = np.nan if fit is None else fit[2]
        rows.append(rec)
    return pd.DataFrame(rows).set_index("ACCOUNTID")


def run(output_root: str | Path = "results") -> pd.DataFrame:
    output_root = Path(output_root)
    servers = [p for p in ANALYSIS_PLATFORMS if p not in set(PHASE_ANALYSIS_EXCLUDE)]
    conn = connect_read_only()
    conn.execute("PRAGMA disable_progress_bar")

    per_server = []
    pooled: dict[str, dict[str, list]] = {m: {"play": [], "peak": []} for m in METRIC_COLS}
    for platform in servers:
        phases = player_peak_phases(conn, platform)
        play = pd.read_csv(output_root / platform / f"play_time_chronotypes_{platform}.csv")
        play.index = play["ACCOUNTID"].astype(str)
        phases = phases.join(play["mean_hour_local"], how="inner")

        for metric in METRIC_COLS:
            sig_mask = benjamini_hochberg_mask(
                phases[f"{metric}_p"].to_numpy(), alpha=AnalysisConfig(platform=platform).phase_alpha
            )
            sig = phases[sig_mask]
            per_server.append(
                {
                    "scope": platform,
                    "metric": metric,
                    "n_significant": int(len(sig)),
                    "circular_corr_play_vs_peak": circular_correlation(
                        sig["mean_hour_local"], sig[f"{metric}_peak_h"]
                    ),
                    "median_coverage_days": float(sig["span_days"].median()),
                }
            )
            pooled[metric]["play"].extend(sig["mean_hour_local"].tolist())
            pooled[metric]["peak"].extend(sig[f"{metric}_peak_h"].tolist())

    for metric in METRIC_COLS:
        play = np.array(pooled[metric]["play"])
        peak = np.array(pooled[metric]["peak"])
        per_server.append(
            {
                "scope": "POOLED",
                "metric": metric,
                "n_significant": int(len(play)),
                "circular_corr_play_vs_peak": circular_correlation(play, peak),
                "median_coverage_days": float("nan"),
            }
        )

    table = pd.DataFrame(per_server)
    dest = output_root / "GRAND" / "grand_phase_vs_playtime.csv"
    table.to_csv(dest, index=False)
    print(f"wrote {dest}")
    print(table[table["scope"] == "POOLED"].to_string(index=False))
    return table


if __name__ == "__main__":
    run()
