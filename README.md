# MSc2026 LoL Release

Teaching release for the League of Legends rhythm analysis workflow.

This repository contains:

- the original full notebook: `notebooks/Parquet_longerAnalyses_May_26.ipynb`
- a concise teaching notebook: `notebooks/LoL_Rhythm_Analysis_Concise.ipynb`
- reusable Python analysis code:
  - `riot_analysis.py`
  - `grand_analysis.py`
  - `Parquet_longerAnalyses_May_26.py`
  - `server_timezones.py`
- the final GRAND report and figures in `results/GRAND/`

The large local DuckDB data file is intentionally not included.

## Setup

Use `uv` from the repository root:

```bash
uv venv .venv --python 3.12
source .venv/bin/activate
uv pip install -e .
```

Start Jupyter:

```bash
jupyter lab
```

## Data

To rerun the analysis, place the DuckDB file at:

```text
riot_local.duckdb
```

The Python code opens it read-only. Generated WAL/database files are ignored by git.

## Recommended Student Path

1. Open `notebooks/LoL_Rhythm_Analysis_Concise.ipynb`.
2. Read the setup and final-report cells first.
3. If you have `riot_local.duckdb`, set `RUN_ANALYSIS = True` in the notebook to run a server.
4. Use the script for full reruns:

```bash
python Parquet_longerAnalyses_May_26.py
```

To regenerate only the GRAND report from existing per-server outputs:

```bash
python Parquet_longerAnalyses_May_26.py --grand-only
```

## Final Report

Open:

```text
results/GRAND/grand_final_report.html
```

The report includes the final N-weighted summaries, pooled circular bimodality BICs, and the fitted one- vs two-component von Mises curves.

## Notes

The concise notebook does not duplicate all of `riot_analysis.py`. Instead, it shows how the analysis is assembled from small reusable functions. This is the preferred teaching form: students can inspect the functions in Python files and run the notebook top-to-bottom without scrolling through hundreds of implementation lines.
