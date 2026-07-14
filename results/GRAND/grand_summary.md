# Grand Analysis

Servers included: 8

This is an across-server meta-analysis. Server-level outputs are summarized first, then combined with metric-specific N weights.

## Key N-Weighted Server Metrics

| metric | n_servers | weight_col | weight_sum | weighted_mean | weighted_sd | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- |
| target_best_period | 8 | server_n_win_games | 92720617.000 | 24.000 | 0.000 | 24.000 | 24.000 |
| win_rate_best_period | 8 | server_n_win_games | 92720617.000 | 23.570 | 3.987 | 6.126 | 33.688 |
| performance_pc1_explained | 8 | server_n_win_games | 92720617.000 | 0.619 | 0.049 | 0.416 | 0.674 |
| performance_pc2_explained | 8 | server_n_win_games | 92720617.000 | 0.192 | 0.021 | 0.161 | 0.243 |
| performance_pc3_explained | 8 | server_n_win_games | 92720617.000 | 0.094 | 0.018 | 0.071 | 0.140 |
| success_pc1_win_rate_loading | 8 | server_n_win_games | 92720617.000 | 0.317 | 0.109 | 0.043 | 0.384 |
| success_pc2_win_rate_loading | 8 | server_n_win_games | 92720617.000 | 0.170 | 0.102 | -0.112 | 0.304 |
| success_pc3_win_rate_loading | 8 | server_n_win_games | 92720617.000 | 0.272 | 0.282 | 0.053 | 0.976 |
| pc1_phase_fdr_significant | 8 | pc1_phase_players | 8000.000 | 214.125 | 198.718 | 91.000 | 721.000 |
| pc2_phase_fdr_significant | 8 | pc2_phase_players | 8000.000 | 185.000 | 234.665 | 15.000 | 761.000 |
| deltammr_phase_fdr_significant | 8 | deltammr_phase_players | 8000.000 | 3.250 | 1.854 | 1.000 | 6.000 |

## Within-Subject Period Peaks

| metric | n_servers | weight_col | total_valid_players | weighted_best_period | weighted_sd_best_period | weighted_sem_best_period |
| --- | --- | --- | --- | --- | --- | --- |
| PC1 | 7 | valid_players | 7000 | 23.964 | 0.076 | 0.029 |
| PC2 | 8 | valid_players | 8000 | 23.937 | 0.056 | 0.020 |
| DeltaMMR | 7 | valid_players | 7000 | 24.000 | 0.039 | 0.015 |

## FDR Phase Counts

| metric | n_servers | weight_col | total_players_analyzed | total_fdr_significant | weighted_fdr_fraction |
| --- | --- | --- | --- | --- | --- |
| PC1 | 7 | players_analyzed | 7000 | 992 | 0.142 |
| PC2 | 7 | players_analyzed | 7000 | 719 | 0.103 |
| DeltaMMR | 7 | players_analyzed | 7000 | 24 | 0.003 |

## Circular Model Preference

| metric | n_servers | weight_col | total_fdr_significant | fit_servers | skipped_servers | preferred_1_component_phases | preferred_2_component_phases |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PC1 | 7 | n_fdr_significant | 992 | 7 | 0 | 816 | 176 |
| PC2 | 7 | n_fdr_significant | 719 | 6 | 1 | 704 | 0 |
| DeltaMMR | 7 | n_fdr_significant | 24 | 0 | 7 | 0 | 0 |

## Phase-Count Weighted PC Peak Density

| metric | n_servers | total_phases | weighted_peak_hour | kappa | min_phases |
| --- | --- | --- | --- | --- | --- |
| PC1 | 7 | 992 | 23.700 | 4.000 | 20 |
| PC2 | 6 | 704 | 12.500 | 4.000 | 20 |

## Pooled Circular Bimodality Test

AIC and BIC compare penalized fit; the parametric-bootstrap likelihood-ratio p-value estimates how often an improvement this large occurs under the fitted one-component null.

| metric | n_servers | n_phases | preferred | vm1_loglik | vm2_loglik | delta_loglik_2_minus_1 | likelihood_ratio | vm1_aic | vm2_aic | delta_aic_1_minus_2 | vm1_bic | vm2_bic | delta_bic_1_minus_2 | bootstrap_lrt_p_value | bootstrap_exceedance_summary | component_1_h | component_2_h | component_1_weight | component_2_weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PC1 | 7 | 992 | 1-component | -1784.891 | -1782.370 | 2.521 | 5.042 | 3573.782 | 3574.740 | -0.958 | 3583.582 | 3599.239 | -15.657 | 0.063 | 62 / 1000 | 2.465 | 18.607 | 0.563 | 0.437 |
| PC2 | 6 | 704 | 1-component | -1263.204 | -1261.074 | 2.130 | 4.259 | 2530.408 | 2532.149 | -1.741 | 2539.522 | 2554.933 | -15.411 | 0.128 | 127 / 1000 | 15.013 | 7.203 | 0.568 | 0.432 |
| DeltaMMR | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
