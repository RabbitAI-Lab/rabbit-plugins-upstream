---
name: classical-ml-drug-discovery
description: End-to-end, evidence-aware drug-discovery skill for building and auditing molecular QSAR, virtual-screening, ADMET, toxicity, binding-affinity, and drug-target models with Random Forests, Support Vector Machines/Regression, and Gradient Boosting. Use when a user asks to curate bioactivity data, compare RF/SVM/XGBoost, design leakage-resistant chemical validation, screen a compound library, assess applicability domain or uncertainty, select diverse experimental candidates, audit a molecular ML paper, or identify open-source cheminformatics software and web services.
version: 1.0.1
categories: [research, development, knowledge]
topics: [drug-discovery, qsar, machine-learning, cheminformatics, virtual-screening]
metadata:
  openclaw:
    emoji: "🧪"
    requires:
      bins: [python3]
      python: [numpy, pandas, scikit-learn, joblib, rdkit]
    optional:
      python: [xgboost, lightgbm, catboost, shap]
      network: [ebi.ac.uk, pubchem.ncbi.nlm.nih.gov, bindingdb.org, tdcommons.ai]
---

# 🧪 Classical ML Drug Discovery

Build defensible molecular machine-learning workflows with **Random Forest (RF)**,
**Support Vector Machine/Regression (SVM/SVR)**, and **Gradient Boosting (GB)**—then turn
predictions into a diverse, uncertainty-aware experimental shortlist rather than unsupported
claims.

This skill is for computational **decision support**. It never treats a model score as proof of
binding, efficacy, safety, mechanism, or clinical utility.

## Trigger conditions

Invoke this skill when the user asks for any of the following:

- QSAR/QSPR classification or regression from SMILES and assay labels;
- comparison of RF, SVM/SVR, classical GB, XGBoost, LightGBM, or CatBoost;
- ligand-based virtual screening or target-specific activity prediction;
- protein–ligand rescoring with RF/SVM/boosted-tree models;
- ADMET, toxicity, solubility, pKa, permeability, clearance, hERG, or CYP prediction;
- drug–target interaction, polypharmacology, repurposing, or target-druggability modeling;
- chemical dataset curation, duplicate/conflict audit, scaffold/time/cluster splitting;
- applicability-domain, calibration, conformal-prediction, or uncertainty analysis;
- diversity-aware candidate selection for an assay;
- critique or reproduction of a molecular machine-learning publication;
- identification of open-source drug-discovery software or websites based on these methods.

## Non-negotiable rules

1. **Define the decision before the model.** State what will be selected, rejected, ranked,
   or measured and the experimental budget.
2. **Never label untested compounds inactive without an explicit, justified assumption.**
3. **Never mix incompatible endpoints silently.** IC50, Ki, Kd, and EC50 are not
   interchangeable; species, target construct, assay modality, and conditions matter.
4. **Deduplicate standardized parent structures before splitting.** Salts, tautomers,
   stereochemical variants, and replicate rows can otherwise leak.
5. **Freeze a deployment-relevant test set before tuning.** Random splitting alone is not a
   novel-chemotype test. Scaffold splitting is useful but can still be optimistic.
6. **Fit every learned preprocessing operation inside training folds.** This includes
   imputation, scaling, supervised feature selection, resampling, calibration, and tuning.
7. **Use rare-active metrics for virtual screening.** Accuracy and ROC-AUC alone are
   insufficient. Report PR-AUC, precision/recall or hit rate at the assay budget, and an
   early-enrichment metric.
8. **Compare a chemically meaningful nearest-neighbor baseline.** Complex models must
   demonstrate value beyond analogue retrieval.
9. **Report applicability domain and uncertainty separately from accuracy.** Neither one
   guarantees the other.
10. **Interpretation is associative, not causal.** Fingerprint bits, RF importance, and SHAP
    values generate hypotheses; they do not establish mechanism.
11. **Do not claim discovery before prospective experiments.** Say “predicted candidate,”
    “prioritized compound,” or “computational hit.”
12. **Preserve proprietary data locally by default.** Do not upload structures or assay labels
    to third-party services without explicit permission.

## Fast operational path

If the user provides a CSV with `smiles` and a response column, use the bundled CLI:

```bash
SKILL_DIR="${SKILL_DIR:-$HOME/skills/classical-ml-drug-discovery}"

# 1) Audit chemistry, endpoints, duplicates, and conflicts without training
python3 "$SKILL_DIR/scripts/qsar_pipeline.py" audit \
  --input compounds.csv \
  --smiles-column smiles \
  --target-column activity \
  --task classification \
  --output-dir audit_output

# 2) Train leakage-aware RF, SVM, and gradient-boosting baselines
python3 "$SKILL_DIR/scripts/qsar_pipeline.py" train \
  --input compounds.csv \
  --smiles-column smiles \
  --target-column activity \
  --task classification \
  --split scaffold \
  --models rf svm gb xgb \
  --output-dir qsar_run

# 3) Predict an external library with a similarity-based domain flag
python3 "$SKILL_DIR/scripts/qsar_pipeline.py" predict \
  --model qsar_run/model.joblib \
  --trust-model \
  --input library.csv \
  --smiles-column smiles \
  --output predictions.csv
```

`xgb` is optional and is skipped with an actionable message if XGBoost is not installed.
The required local packages are documented in `requirements-optional.txt`.

## Full workflow

### Phase 1 — Define the scientific decision

Capture the following before touching labels:

| Field | Required answer |
|---|---|
| Biological question | Target, phenotype, property, or safety liability |
| Endpoint | Exact measurement, units, transform, species, construct, assay |
| Prediction mode | Classification, regression, or ranking |
| Deployment population | Lead series, public library, novel scaffolds, new target, future data |
| Experimental budget | Number or fraction of compounds that can be tested |
| Error costs | Relative cost of false positives and false negatives |
| Novelty requirement | Same-series optimization or scaffold hopping |
| Required evidence | Retrospective, external, prospective biochemical, cellular, PK, in vivo |
| Confidentiality | Whether structures/labels may leave the local machine |

If the request is underspecified and the missing choice changes the analysis, ask focused
questions. If the user requests autonomous full execution, choose conservative defaults, record
them, and continue.

### Phase 2 — Acquire data with provenance

Preferred public sources include:

- ChEMBL for curated bioactivities;
- PubChem BioAssay for screening results and assay descriptions;
- BindingDB for measured binding affinities;
- TDC and MoleculeNet for standardized benchmarks;
- PDBbind or curated complex sets for structure-based scoring;
- internal assays when the intended deployment is an internal chemical series.

Record database version, retrieval date, exact query, target identifier, assay filters, units,
qualifiers, and data license. Do not scrape a source that forbids automated access.

### Phase 3 — Curate structures and responses

Perform and report:

1. SMILES parsing and sanitization;
2. largest-fragment/parent selection policy;
3. charge and tautomer policy;
4. stereochemistry policy;
5. canonicalization;
6. exact and standardized-parent duplicates;
7. replicate aggregation rule;
8. conflicting-label rule;
9. unit normalization and endpoint transformation;
10. missing/censored-value handling;
11. assay/species/construct harmonization;
12. final inclusion and exclusion counts.

For molar potency, use `pActivity = -log10(activity in molar units)` only when the source
units and endpoint type are consistent. Preserve raw values and qualifiers.

### Phase 4 — Choose representations

Benchmark at least two representations when data allow:

- **ECFP/Morgan bits or counts:** fast baseline for RF, linear/RBF SVM, and boosted trees;
- **compact physicochemical descriptors:** interpretable ADMET/property baseline;
- **expanded RDKit/Mordred/PaDEL descriptors:** potentially strong but must be cleaned inside
  folds;
- **protein–ligand contact or PLEC features:** structure-based scoring;
- **protein sequence/structure and pair features:** drug–target interaction;
- **assay/omics/network features:** contextual response and repurposing.

The bundled CLI combines Morgan bits with a compact RDKit descriptor panel and stores the
feature specification in the model bundle.

### Phase 5 — Freeze the test design

Choose the split that matches deployment:

| Deployment claim | Minimum defensible split |
|---|---|
| Future random samples from the same mixture | Stratified/random holdout plus repeated CV |
| New analogues in the same program | Temporal or medicinal-chemistry-series holdout |
| Novel chemotypes | Structure-cluster holdout; scaffold split as a secondary baseline |
| Future project data | Temporal split with no future leakage |
| New compounds for known targets | Drug-cold DTI split |
| Known compounds for new targets | Target-cold DTI split |
| Both new | Drug-and-target-cold split |
| Transfer across laboratories | External laboratory/source holdout |

A scaffold split is not automatically an out-of-distribution guarantee. Measure train–test
nearest-neighbor similarity and report it.

### Phase 6 — Fit mandatory baselines

Always include:

- prevalence/mean or median baseline;
- nearest-neighbor similarity baseline;
- simple linear/logistic model where appropriate;
- Random Forest;
- SVM/SVR;
- classical GB and/or XGBoost.

Use identical molecules and outer splits for every model. Give comparable tuning budgets.

### Phase 7 — Tune without leakage

Use nested cross-validation or an inner validation set. For scaffold/grouped training data, use
group-aware inner folds. For temporal deployment, preserve chronology in validation.

Suggested search priorities:

- **RF:** trees, maximum features, minimum leaf size, depth, class weights;
- **SVM/SVR:** scaling, kernel, C, gamma, epsilon, class weights;
- **GB/XGBoost:** learning rate, rounds, depth/leaves, row/column subsampling, minimum
  child/leaf size, split gain, regularization, positive-class weight, early stopping.

Do not use the frozen test set for early stopping or model selection.

### Phase 8 — Evaluate the decision

#### Rare-active classification / virtual screening

Primary metrics:

- PR-AUC or average precision;
- precision, recall, and hit rate at the exact experimental budget;
- EF0.1%, EF1%, or BEDROC;
- MCC or balanced accuracy.

Secondary metrics:

- ROC-AUC;
- calibration/Brier score;
- diversity and novelty of selected compounds;
- performance by similarity and applicability-domain bin.

#### Regression

Report:

- MAE and RMSE;
- R² and Spearman rank correlation;
- top-k recovery if selection is the goal;
- residuals versus activity, similarity, scaffold, and descriptor range;
- interval coverage and width if uncertainty is provided.

Use bootstrap or repeated-fold confidence intervals where possible.

### Phase 9 — Applicability domain and uncertainty

At minimum provide:

- nearest-neighbor Tanimoto similarity to training compounds;
- training-density or descriptor-range flags;
- response-range warning for tree regressors;
- calibration analysis for classification;
- ensemble or conformal uncertainty when justified.

The bundled CLI estimates a similarity threshold from leave-one-out nearest-neighbor
similarities in a capped training sample and labels predictions `in_domain` or `out_of_domain`.
This is a useful structural check, not a complete mechanistic domain.

For stronger uncertainty, use CPSign or another leakage-safe conformal workflow and test
coverage under the intended chemical shift. Conformal coverage requires exchangeability and
can fail under series or temporal drift.

### Phase 10 — Interpret safely

For RF/GB:

- use held-out permutation importance before impurity/gain importance;
- compare rankings across folds, seeds, and algorithms;
- group correlated descriptors and map fingerprint bits back to atomic environments;
- use SHAP only as a model-behavior explanation;
- investigate whether a feature encodes series identity, assay protocol, or nuisance chemistry.

For SVM:

- inspect linear coefficients when a linear model is used;
- for nonlinear kernels, use local perturbation or example-based explanations cautiously;
- report support-vector count and nearest support examples.

Never describe model attribution as biological causality.

### Phase 11 — Select an experimental batch

Do not simply take the highest scores. Construct a shortlist using:

1. predicted value;
2. applicability-domain status;
3. uncertainty;
4. cluster/scaffold diversity;
5. novelty relative to known actives;
6. physicochemical and reactive-group review;
7. synthesis or purchase feasibility;
8. orthogonal model/docking agreement;
9. medicinal-chemistry review.

Include a small exploration fraction when the program can tolerate it. Preserve the exact
selection rule before assays return.

### Phase 12 — Validate and learn

Escalate evidence through:

1. frozen external retrospective set;
2. independent computational model;
3. biochemical binding/activity assay;
4. aggregation, fluorescence, redox, and other interference controls;
5. selectivity/counter-screens;
6. cell target engagement and phenotype;
7. ADME/toxicity assays;
8. PK/PD and in vivo studies only when justified.

Update the model with both positive and negative prospective results, maintaining assay
consistency and version history.

## Algorithm decision guide

| Situation | Preferred starting model | Why | Main risk |
|---|---|---|---|
| Small/medium tabular dataset, fast baseline | RF | Robust, little scaling, nonlinear | Analogue leakage and poor extrapolation |
| High-dimensional fingerprints, limited samples | Linear or RBF SVM | Margin-based, strong in high dimensions | Scaling/tuning and kernel cost |
| Continuous property with small/medium data | SVR + RF | Complementary smooth/kernel and tree models | Assay noise and domain limits |
| Medium/large descriptor/fingerprint table | XGBoost | Strong regularized tabular learner | Tuning and feature-importance instability |
| Very large sparse table | LightGBM | Fast histogram/leaf-wise training | Overfit without leaf constraints |
| Numeric molecular data plus real categories | CatBoost | Ordered boosting and category handling | Categories may encode leakage |
| Structure-based rescoring | ODDT RF-Score plus independent scorer | Proven RF contact features | Training-target and docking-pose shift |
| SVM with valid prediction intervals/sets | CPSign | Conformal and Venn–Abers support | Exchangeability and license terms |
| No-code/low-code workflow | KNIME + RDKit | Visual, auditable pipeline | Node-version and extension-license drift |

See `references/ALGORITHM_GUIDE.md` for deeper details and
`references/RESEARCH_REPORT.md` for the complete evidence review.

## Open-source tool routing

- **Feature generation:** RDKit; optionally Mordred or PaDEL.
- **General models:** scikit-learn, LIBSVM, XGBoost, LightGBM, CatBoost.
- **Unified molecular ML:** DeepChem/MoleculeNet, DeepMol.
- **End-to-end pipeline:** AMPL.
- **AutoML:** QSARtuna, ZairaChem, DeepMol.
- **Reproducible QSPR/PCM:** QSPRpred.
- **Visual workflows:** KNIME + RDKit nodes.
- **Model hosting:** Flame.
- **Multi-target QSAR:** QSAR-Co-X.
- **SVM conformal prediction:** CPSign.
- **Docking rescoring:** ODDT/RF-Score-VS.
- **Transparent endpoint models:** OPERA/CompTox.
- **Online model/data environment:** OCHEM/openOCHEM.
- **Browser-local exploration:** QITB.
- **Pretrained model catalog:** Ersilia Model Hub.
- **Benchmarks/data:** TDC and MoleculeNet.

See `references/OPEN_SOURCE_TOOLS.md` for links, licenses, and caveats.

## Bundled CLI contract

### Audit

```bash
python3 scripts/qsar_pipeline.py audit --help
```

Produces:

- `data_audit.json`;
- `curated_data.csv`;
- invalid, duplicate, and conflicting-label counts;
- standardized canonical parent SMILES and scaffold identifiers.

### Train

```bash
python3 scripts/qsar_pipeline.py train --help
```

Produces:

- `model.joblib` with model, features, labels, metadata, and training-domain structures;
- `metrics.json` with CV and holdout metrics;
- `test_predictions.csv`;
- `split_assignments.csv`;
- `feature_importance.csv` when available;
- `data_audit.json`;
- `model_card.md` documenting intended use and limitations.

### Predict

```bash
python3 scripts/qsar_pipeline.py predict --help
```

Produces a CSV containing canonical structures, predictions, optional probabilities, nearest
training similarity, and domain flags. Invalid SMILES are retained with an error status.

## Required final-report structure

Every completed modeling task must report:

1. **Decision and intended use**
2. **Data provenance and license**
3. **Endpoint definition**
4. **Structure/assay curation**
5. **Representations**
6. **Split rationale and train–test similarity**
7. **Models and tuning budget**
8. **Metrics with uncertainty**
9. **Calibration and applicability domain**
10. **Interpretation stability**
11. **Candidate-selection rule and diversity**
12. **Limitations and prohibited uses**
13. **Prospective validation plan**
14. **Reproducibility artifacts and versions**

Use `templates/DRUG_DISCOVERY_REPORT_TEMPLATE.md`.

## Failure modes and required responses

| Failure | Required action |
|---|---|
| Too few compounds | Reduce claims, prefer simple models, repeated/grouped validation, seek more data |
| Only actives available | Do not invent inactives; use ranking, one-class/domain methods, or obtain screened negatives |
| Conflicting replicates | Investigate assay/provenance; aggregate only with a documented rule |
| One scaffold dominates | Use grouped split, report scaffold-specific performance, diversify acquisition |
| Split lacks both classes | Change split seed/design without consulting test outcomes; record the rule |
| SVM too slow | Linear SVM, kernel approximation, smaller tuning set, or boosted trees |
| XGBoost unavailable | Run classical GradientBoosting and document omission; do not rename it XGBoost |
| High CV but weak external test | Diagnose similarity/leakage/shift; do not tune against the external labels |
| Poor calibration | Recalibrate on inner folds; report ranking and probability quality separately |
| Mostly out-of-domain library | Acquire representative labels or restrict claims; do not force a ranking as reliable |
| Feature importance changes by fold | Report instability and avoid mechanistic conclusions |
| Web predictor disagrees | Check endpoint/model/domain/version; do not average blindly |

## Security and privacy behavior

- The bundled CLI is local-only and makes no network requests.
- It reads only paths explicitly supplied by the user and writes only to the requested output
  directory.
- It does not read environment variables, API keys, browser data, or unrelated files.
- It serializes models with `joblib`; **never load an untrusted `.joblib`/pickle file**, because
  Python deserialization can execute code.
- External websites are optional. Obtain explicit permission before sending proprietary SMILES,
  labels, targets, or structures.
- Review third-party package and model licenses before commercial use.

## Additional references

- `references/RESEARCH_REPORT.md` — complete deep-research report and citations.
- `references/ALGORITHM_GUIDE.md` — RF/SVM/GB mechanics, strengths, limits, and tuning.
- `references/VALIDATION_PROTOCOL.md` — leakage-resistant validation and metrics.
- `references/OPEN_SOURCE_TOOLS.md` — software and web-resource matrix.
- `templates/PROJECT_BRIEF.md` — task definition form.
- `templates/DRUG_DISCOVERY_REPORT_TEMPLATE.md` — final reporting template.

## Integrity verification

Follow the commands in `README.md` or run:

```bash
python3 scripts/verify_integrity.py
sha256sum -c CHECKSUMS.sha256
```
