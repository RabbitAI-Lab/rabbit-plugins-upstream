# Molecular Machine-Learning Drug-Discovery Report

**Project:**  
**Date:**  
**Analyst:**  
**Code/data/model version:**

## Executive decision summary

- Decision the model supports:
- Recommended action:
- Number of compounds prioritized:
- Primary external performance:
- Applicability-domain coverage:
- Prospective evidence status:
- Most important limitation:

## 1. Intended use and prohibited uses

### Intended use

### Prohibited uses

This model must not be represented as proof of binding, efficacy, safety, mechanism, or clinical
utility without the corresponding experiments.

## 2. Biological question and endpoint

- Target/property/phenotype:
- Assay and biological context:
- Measurement and units:
- Transform or classification threshold:
- Rationale:

## 3. Data provenance and license

| Source | Version/date | Query/filter | Records | License/terms |
|---|---|---|---:|---|
| | | | | |

## 4. Curation

| Stage | Records retained | Records removed | Reason/rule |
|---|---:|---:|---|
| Raw | | | |
| Parseable structures | | | |
| Standardized parents | | | |
| Endpoint harmonized | | | |
| Deduplicated | | | |
| Final | | | |

Document fragment, charge, tautomer, stereochemistry, replicate, censoring, and conflict rules.

## 5. Representation

- Fingerprints:
- Descriptors:
- Protein/complex/network features:
- Feature filtering:
- Feature versions:

## 6. Validation design

- Outer split and why it matches deployment:
- Inner validation/tuning:
- Train/validation/test sizes:
- Positive prevalence or response ranges:
- Train–test nearest-neighbor similarity:
- Leakage controls:

## 7. Baselines and models

| Pipeline | Representation | Key hyperparameters | Tuning budget |
|---|---|---|---:|
| Prevalence/mean | | | |
| Nearest neighbor | | | |
| Linear/logistic | | | |
| Random Forest | | | |
| SVM/SVR | | | |
| Gradient boosting/XGBoost | | | |

## 8. Performance

### Classification

| Model | PR-AUC | ROC-AUC | MCC | Balanced accuracy | Precision@budget | Recall@budget | EF1% |
|---|---:|---:|---:|---:|---:|---:|---:|
| | | | | | | | |

### Regression

| Model | MAE | RMSE | R² | Spearman | Top-k recovery |
|---|---:|---:|---:|---:|---:|
| | | | | | |

Include confidence intervals, per-scaffold/domain results, and the exact primary metric.

## 9. Calibration, uncertainty, and applicability domain

- Calibration method and Brier/reliability result:
- Structural domain method and threshold:
- Descriptor/mechanistic domain:
- Conformal/ensemble method:
- Empirical coverage and interval/set size:
- Fraction of deployment library in-domain:

## 10. Interpretation

- Stable global features/fragments:
- Local explanations for selected compounds:
- Agreement across folds/seeds/models:
- Confounders investigated:
- Mechanistic hypotheses requiring tests:

## 11. Candidate selection

| Rank | Compound ID | Canonical SMILES | Prediction | Probability/interval | Nearest similarity | Domain | Cluster/scaffold | Rationale |
|---:|---|---|---:|---|---:|---|---|---|
| | | | | | | | | |

Document diversity, novelty, feasibility, reactive/assay-interference review, and exploration
fraction.

## 12. Prospective validation plan/results

- Primary assay:
- Counter-screens:
- Selectivity:
- Cellular validation:
- ADME/toxicity:
- Tested compounds and all outcomes:

## 13. Limitations and failure modes

1.
2.
3.

## 14. Reproducibility artifacts

- Curated data checksum:
- Split assignment file:
- Environment lock/container:
- Code commit:
- Model artifact checksum:
- Model card:
- Prediction file:

## 15. Conclusion

State what evidence supports, what it does not support, and the next experiment.

## References
