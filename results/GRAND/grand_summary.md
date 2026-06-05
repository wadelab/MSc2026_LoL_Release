# Grand Analysis

Servers included: 8

This is an across-server meta-analysis. Server-level outputs are summarized first, then combined with metric-specific N weights.

## Key N-Weighted Server Metrics

| metric | n_servers | weight_col | weight_sum | weighted_mean | weighted_sd | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- |
| target_best_period | 8 | server_n_win_games | 92716063.000 | 17.597 | 6.012 | 11.994 | 24.048 |
| win_rate_best_period | 8 | server_n_win_games | 92716063.000 | 23.438 | 2.430 | 10.329 | 24.048 |
| performance_pc1_explained | 8 | server_n_win_games | 92716063.000 | 0.619 | 0.048 | 0.421 | 0.668 |
| performance_pc2_explained | 8 | server_n_win_games | 92716063.000 | 0.192 | 0.020 | 0.161 | 0.244 |
| performance_pc3_explained | 8 | server_n_win_games | 92716063.000 | 0.095 | 0.018 | 0.070 | 0.141 |
| success_pc1_win_rate_loading | 8 | server_n_win_games | 92716063.000 | 0.286 | 0.100 | 0.037 | 0.344 |
| success_pc2_win_rate_loading | 8 | server_n_win_games | 92716063.000 | 0.163 | 0.087 | -0.059 | 0.246 |
| success_pc3_win_rate_loading | 8 | server_n_win_games | 92716063.000 | 0.304 | 0.276 | -0.001 | 0.990 |
| pc1_phase_fdr_significant | 8 | pc1_phase_players | 8000.000 | 214.125 | 197.266 | 89.000 | 717.000 |
| pc2_phase_fdr_significant | 8 | pc2_phase_players | 8000.000 | 184.750 | 236.371 | 15.000 | 765.000 |
| deltammr_phase_fdr_significant | 8 | deltammr_phase_players | 8000.000 | 3.250 | 1.854 | 1.000 | 6.000 |

## Within-Subject Period Peaks

| metric | n_servers | weight_col | total_valid_players | weighted_best_period | weighted_sd_best_period | weighted_sem_best_period |
| --- | --- | --- | --- | --- | --- | --- |
| PC1 | 8 | valid_players | 8000 | 23.987 | 0.061 | 0.022 |
| PC2 | 8 | valid_players | 8000 | 24.035 | 0.055 | 0.019 |
| DeltaMMR | 7 | valid_players | 7000 | 23.988 | 0.047 | 0.018 |

## FDR Phase Counts

| metric | n_servers | weight_col | total_players_analyzed | total_fdr_significant | weighted_fdr_fraction |
| --- | --- | --- | --- | --- | --- |
| PC1 | 8 | players_analyzed | 8000 | 1713 | 0.214 |
| PC2 | 8 | players_analyzed | 8000 | 1478 | 0.185 |
| DeltaMMR | 8 | players_analyzed | 8000 | 26 | 0.003 |

## Circular Model Preference

| metric | n_servers | weight_col | total_fdr_significant | fit_servers | skipped_servers | preferred_1_component_phases | preferred_2_component_phases |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PC1 | 8 | n_fdr_significant | 1713 | 8 | 0 | 820 | 893 |
| PC2 | 8 | n_fdr_significant | 1478 | 7 | 1 | 698 | 765 |
| DeltaMMR | 8 | n_fdr_significant | 26 | 0 | 8 | 0 | 0 |

## Phase-Count Weighted PC Peak Density

| metric | n_servers | total_phases | weighted_peak_hour | kappa | min_phases |
| --- | --- | --- | --- | --- | --- |
| PC1 | 8 | 1713 | 22.400 | 4.000 | 20 |
| PC2 | 7 | 1463 | 9.800 | 4.000 | 20 |

## Pooled Circular Bimodality Test

| metric | n_servers | n_phases | preferred | delta_bic_1_minus_2 | component_1_h | component_2_h | component_1_weight | component_2_weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PC1 | 8 | 1713 | 2-component | 16.907 | 21.445 | 7.170 | 0.574 | 0.426 |
| PC2 | 7 | 1463 | 2-component | 33.880 | 9.386 | 20.006 | 0.672 | 0.328 |
| DeltaMMR | 0 | 0 |  |  |  |  |  |  |
