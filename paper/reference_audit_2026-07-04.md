# Reference Audit - 2026-07-04

Manuscript: paper/lol_circadian_rhythms.qmd
Bibliography: paper/references.bib

## Existence check

- Crossref DOI resolution: 26/26 DOIs resolved (no missing records).
- Citation key integrity: 26/26 cited keys resolve in bibliography.
- Independent second-source check (Europe PMC) on core chronobiology/performance DOIs: all queried records resolved.

## Claim-by-claim relevance verdicts

| Line | Citation key(s) | Claim attached | Verdict | Note |
|---:|---|---|---|---|
| 72 | roenneberg2007epidemiology | Human circadian rhythms are entrained to light-dark cycle | Supports | Direct chronobiology review support |
| 74 | schmidt2007time | Cognition shows time-of-day modulation | Supports | Review directly about circadian cognition |
| 77 | horne1976self; roenneberg2003life | Morningness-eveningness is a stable trait | Supports | Combination is appropriate for chronotype framing |
| 79 | adan2012circadian | Chronotype distribution is broad/continuous | Supports | Comprehensive chronotype review |
| 89 | hsu2024circadian | In gamers with gaming disorder, eveningness links to disrupted sleep/risk | Supports | Population-specific claim now matches source scope |
| 90 | nagorsky2020structure | Esports performance is structured/trainable | Supports | Paper directly addresses structure and training |
| 120-121 | aung2018predicting; vardal2022mind | Cohort provenance and prior use | Supports | Correct lineage citations |
| 132 | aung2018predicting | Early learning predicts end-of-season skill | Supports | Core result of cited paper |
| 133 | vardal2022mind | Practice spacing shapes gains | Supports | Core result of cited paper |
| 137 | raasveldt2019duckdb | DuckDB analytic database use | Supports | Software/system citation appropriate |
| 173 | lomb1976least; scargle1982studies | Lomb-Scargle for unevenly sampled series | Supports | Foundational method sources |
| 175 | astropy2018; vanderplas2018understanding | Astropy implementation and LS guidance | Supports | Implementation + explanatory methods citation |
| 191 | benjamini1995controlling | Benjamini-Hochberg FDR control | Supports | Foundational method source |
| 198 | fisher1993statistical; mardia2000directional; berens2009circstat | Circular statistics and von Mises modelling | Supports | Standard references for circular methods |
| 205-206 | akaike1974new; schwarz1978estimating | AIC and BIC model comparison | Supports | Foundational criteria sources |
| 231-233 | harris2020numpy; virtanen2020scipy; mckinney2010data; hunter2007matplotlib | Software stack used in analysis | Supports | Standard software citations |
| 373-374 | smarr2018social; facerchilds2015impact | Related educational and athletic big-data findings | Supports | Topically aligned contextual citations |
| 379 | horne1976self; roenneberg2003life | Lark/owl mixture interpretation | Partial | Conceptual fit is good; direct bimodality evidence is inferential, not from these sources |
| 399 | aung2018predicting | Across-season skill change is predictable | Supports | Correctly attributed |
| 403 | vardal2022mind | Prior work set MMR aside as match-level performance signal | Supports | Aligns with cited framing |
| 450 | aung2018predicting; vardal2022mind | Data restrictions tied to this cohort lineage | Supports | Appropriate provenance reference |

## Findings summary (severity-ordered)

1. No fabricated references detected.
2. No DOI metadata mismatches detected in automated checks.
3. One low-severity relevance caveat: line 379 is a conceptual inference from chronotype literature rather than a citation to direct bimodality evidence in this exact context.

## Recommended action

- Optional: add one citation that directly discusses chronotype distribution shape/bimodality in large populations if you want the line-379 interpretation to be explicitly anchored.

## Journal-variant re-check (2026-07-04)

Both variants (`journal_variants/lol_circadian_rhythms_chb.qmd`,
`journal_variants/lol_circadian_rhythms_gigascience.qmd`) share `references.bib`
and add no new citations in their variant-specific sections, so the relevance
verdicts above apply unchanged. Automated existence check flagged four entries;
all four are benign after manual + second-database review, and no `.bib` edit is
needed:

| key | flag | resolution |
|---|---|---|
| horne1976self | MISSING (not in Crossref) | Real paper (MEQ), confirmed via Semantic Scholar / ResearchGate. *Int. J. Chronobiology* is defunct and has no DOI; entry is correct as-is. |
| mardia2000directional | year 2000 vs Crossref 1999 | Crossref lists print 1999 / online 2008; 2000 is the standard cited (title-page) year. Kept 2000. |
| astropy2018 | first-author mismatch | False positive — corporate author `{Astropy Collaboration}`; Crossref expands to individuals. Entry correct. |
| raasveldt2019duckdb | title differs | False positive — Crossref truncates title to "DuckDB"; bib carries the full title. Entry correct. |

No fabrications, no wrong-paper DOIs, no retractions.
