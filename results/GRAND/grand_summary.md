# Grand Analysis

Servers included: 8

This is an across-server meta-analysis. Server-level outputs are summarized first, then combined with metric-specific N weights.

## Key N-Weighted Server Metrics

| metric | n_servers | weight_col | weight_sum | weighted_mean | weighted_sd | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- |
| target_best_period | 8 | server_n_win_games | 92720617.000 | 23.698 | 1.878 | 12.000 | 24.000 |
| win_rate_best_period | 8 | server_n_win_games | 92720617.000 | 20.876 | 6.192 | 8.000 | 24.000 |
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
| PC1 | 7 | valid_players | 7000 | 24.000 | 0.000 | 0.000 |
| PC2 | 7 | valid_players | 7000 | 24.000 | 0.000 | 0.000 |
| DeltaMMR | 7 | valid_players | 7000 | 24.000 | 0.000 | 0.000 |

## FDR Phase Counts

| metric | n_servers | weight_col | total_players_analyzed | total_fdr_significant | weighted_fdr_fraction |
| --- | --- | --- | --- | --- | --- |
| PC1 | 8 | players_analyzed | 8000 | 1713 | 0.214 |
| PC2 | 8 | players_analyzed | 8000 | 1480 | 0.185 |
| DeltaMMR | 8 | players_analyzed | 8000 | 26 | 0.003 |

## Circular Model Preference

| metric | n_servers | weight_col | total_fdr_significant | fit_servers | skipped_servers | preferred_1_component_phases | preferred_2_component_phases |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PC1 | 8 | n_fdr_significant | 1713 | 8 | 0 | 816 | 897 |
| PC2 | 8 | n_fdr_significant | 1480 | 7 | 1 | 704 | 761 |
| DeltaMMR | 8 | n_fdr_significant | 26 | 0 | 8 | 0 | 0 |

## Phase-Count Weighted PC Peak Density

| metric | n_servers | total_phases | weighted_peak_hour | kappa | min_phases |
| --- | --- | --- | --- | --- | --- |
| PC1 | 8 | 1713 | 22.400 | 4.000 | 20 |
| PC2 | 7 | 1465 | 9.800 | 4.000 | 20 |

## Pooled Circular Bimodality Test

| metric | n_servers | n_phases | preferred | delta_bic_1_minus_2 | component_1_h | component_2_h | component_1_weight | component_2_weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PC1 | 8 | 1713 | 2-component | 17.235 | 21.497 | 7.145 | 0.573 | 0.427 |
| PC2 | 7 | 1465 | 2-component | 28.378 | 9.365 | 19.934 | 0.647 | 0.353 |
| DeltaMMR | 0 | 0 |  |  |  |  |  |  |
