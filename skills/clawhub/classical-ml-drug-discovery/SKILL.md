---
name: classical-ml-drug-discovery
description: "Build defensible molecular ML for drug discovery — QSAR, virtual screening, ADMET, toxicity, binding affinity, drug-target models — with Random Forest, SVM/SVR, and Gradient Boosting, plus dataset analysis, inductive conformal prediction, multi-model consensus, diversity-aware batch selection, and cheminformatics-aware interpretation. Use for curating bioactivity data, comparing RF/SVM/XGBoost, leakage-resistant validation, library screening, calibrated uncertainty, disagreeing-model reconciliation, diverse assay-batch selection, feature-to-molecule mapping, applicability-domain assessment, or auditing a molecular ML paper."
version: 1.3.2
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

Build defensible molecular ML workflows (RF, SVM/SVR, GB) and turn predictions into a diverse,
uncertainty-aware experimental shortlist — never an unsupported claim.

**This is computational decision support.** A model score is not proof of binding, efficacy,
safety, mechanism, or clinical utility.

## Use when
QSAR/QSPR classification or regression; RF vs SVM vs GB vs XGBoost/LightGBM/CatBoost; ligand-based
or target-specific screening; protein–ligand rescoring; ADMET/toxicity/solubility/pKa/permeability/
clearance/hERG/CYP; drug–target interaction, polypharmacology, repurposing, druggability; dataset
curation or duplicate/conflict/scaffold/time/cluster-split auditing; applicability domain,
calibration, conformal prediction, uncertainty; diverse candidate selection; critiquing/reproducing
a molecular ML paper; or finding open-source cheminformatics methods.

## Non-negotiable rules
1. **Define the decision before the model** — what is selected/rejected/ranked/measured and the experimental budget.
2. **Never label untested compounds inactive** without an explicit, justified assumption.
3. **Never mix incompatible endpoints silently** — IC50, Ki, Kd, EC50 are not interchangeable; species, construct, modality, conditions matter.
4. **Deduplicate standardized parent structures before splitting** — salts, tautomers, stereoisomers, replicates can leak.
5. **Freeze a deployment-relevant test set before tuning** — random split is not a novel-chemotype test; scaffold split helps but can be optimistic.
6. **Fit every learned preprocessing step inside training folds** — imputation, scaling, supervised feature selection, resampling, calibration, tuning.
7. **Use rare-active metrics for virtual screening** — report PR-AUC, precision/recall or hit rate at budget, and an early-enrichment metric; accuracy/ROC-AUC alone are insufficient.
8. **Compare a chemically meaningful nearest-neighbor baseline** — complex models must beat analogue retrieval.
9. **Report applicability domain and uncertainty separately from accuracy** — neither guarantees the other.
10. **Interpretation is associative, not causal** — fingerprint bits, RF importance, SHAP generate hypotheses, not mechanism.
11. **Do not claim discovery before prospective experiments** — say "predicted candidate"/"prioritized compound"/"computational hit".
12. **Preserve proprietary data locally by default** — don't upload structures/labels to third parties without permission.

## Fast path
```bash
SKILL_DIR="${SKILL_DIR:-$HOME/skills/classical-ml-drug-discovery}"
python3 "$SKILL_DIR/scripts/qsar_pipeline.py" audit   --input compounds.csv --smiles-column smiles --target-column activity --task classification --output-dir audit_output
python3 "$SKILL_DIR/scripts/qsar_pipeline.py" train   --input compounds.csv --smiles-column smiles --target-column activity --task classification --split scaffold --models rf svm gb xgb --output-dir qsar_run
python3 "$SKILL_DIR/scripts/qsar_pipeline.py" predict --model qsar_run/model.joblib --trust-model --input library.csv --smiles-column smiles --output predictions.csv
```
`xgb` is optional (skipped with a message if not installed). Deps: `requirements-optional.txt`.

## Full workflow
### 1. Define the decision — capture before labels
Biological question · endpoint (measurement, units, transform, species, construct, assay) · prediction
mode · deployment population · experimental budget · error costs · novelty requirement · required
evidence · confidentiality. If underspecified, ask; on autonomous runs choose conservative defaults,
record them, continue.

### 2. Data with provenance
ChEMBL, PubChem BioAssay, BindingDB, TDC/MoleculeNet, PDBbind, internal assays. Record version,
date, query, target ID, assay filters, units, qualifiers, license. Don't scrape sources that forbid it.

### 3. Curate structures & responses
SMILES parse/sanitize; largest-fragment/parent policy; charge & tautomer policy; stereochemistry;
canonicalize; exact & standardized-parent dedupe; replicate aggregation; conflicting-label rule; unit
normalization & endpoint transform; missing/censored handling; assay/species/construct harmonization;
final in/exclusion counts. Use `pActivity = -log10(molar activity)` only when units/endpoint are
consistent; preserve raw values & qualifiers.

### 4. Representations (benchmark ≥2)
ECFP/Morgan bits (RF, linear/RBF SVM, boosted trees) · compact physicochemical descriptors ·
expanded RDKit/Mordred/PaDEL (clean inside folds) · protein–ligand contact/PLEC (structure-based) ·
protein sequence/structure pairs (DTI) · assay/omics/network (contextual, repurposing). CLI combines
Morgan bits + compact RDKit panel and stores the spec in the bundle.

### 5. Freeze the test design
| Deployment claim | Minimum split |
|---|---|
| Future random samples from same mixture | Stratified/random holdout + repeated CV |
| New analogues in same program | Temporal or med-chem-series holdout |
| Novel chemotypes | Structure-cluster holdout; scaffold split as secondary baseline |
| Future project data | Temporal split, no future leakage |
| New compounds for known targets | Drug-cold DTI split |
| Known compounds for new targets | Target-cold DTI split |
| Both new | Drug-and-target-cold split |
| Transfer across labs | External laboratory/source holdout |

Scaffold split ≠ OOD guarantee — measure and report train–test nearest-neighbor similarity.

### 6. Mandatory baselines
Prevalence/mean-or-median · nearest-neighbor similarity · simple linear/logistic · RF · SVM/SVR ·
classical GB and/or XGBoost. Identical molecules & outer splits; comparable tuning budgets.

### 7. Tune without leakage
Nested CV or inner validation; group-aware folds for grouped/scaffold data; preserve chronology for
temporal. Tune RF (trees, max-features, min-leaf, depth, class weights), SVM/SVR (scaling, kernel, C,
gamma, epsilon, weights), GB/XGB (lr, rounds, depth, subsample, min-child, regularization, weight).
Never use the frozen test set for early stopping or model selection.

### 8. Evaluate the decision
**Classification/virtual screening:** PR-AUC/average precision, precision/recall/hit rate at budget,
EF0.1%/EF1%/BEDROC, MCC or balanced accuracy; secondary ROC-AUC, calibration/Brier, diversity &
novelty, per-domain-bin performance.
**Regression:** MAE, RMSE, R², Spearman, top-k recovery (if selection), residuals vs activity/similarity/
scaffold/descriptor range, interval coverage & width. Use bootstrap or repeated-fold CIs.

### 9. Applicability domain & uncertainty
Report nearest-neighbor Tanimoto to training, training-density/descriptor-range flags, response-range
warning for tree regressors, calibration analysis, ensemble/conformal uncertainty when justified. CLI
estimates a similarity threshold (5th percentile of training LOO-NN) and labels `in_domain`/
`out_of_domain`. For stronger uncertainty use CPSign or a leakage-safe conformal workflow and test
coverage under the intended shift. **Coverage is guaranteed only under exchangeability**; under
scaffold/temporal drift it degrades — treat as a heuristic, not a safety certificate.

### 10. Interpret safely
RF/GB: held-out permutation importance before impurity/gain; compare across folds, seeds, algorithms;
group correlated descriptors; map bits→atomic environments; use SHAP only as model-behavior explanation;
check whether a feature encodes series/assay/nuisance. SVM: linear coefficients (linear kernel); local
perturbation or example-based explanations cautiously; report support-vector count & nearest supports.
Never describe attribution as biological causality.

### 11. Select an experimental batch
Don't take top-N. Shortlist by: predicted value · domain status · uncertainty · cluster/scaffold
diversity · novelty vs known actives · physchem & reactive-group review · synthesis/purchase feasibility ·
orthogonal model/docking agreement · med-chem review. Include a small exploration fraction if tolerable.
Preserve the selection rule before assays return.

### 12. Validate & learn
Escalate: frozen external retrospective → independent model → biochemical binding/activity assay →
interference controls (aggregation, fluorescence, redox) → selectivity/counter-screens → cell target
engagement & phenotype → ADME/toxicity → PK/PD & in vivo (only if justified). Update the model with
both positive and negative prospective results, maintaining assay provenance.

## Algorithm choice (one-line rule + detail)
Prefer RF for small/medium tables; SVM for high-dim sparse; XGB/LightGBM for large descriptor tables;
CatBoost for numeric+categorical. Key risks: analogue leakage (RF), kernel cost (SVM), overfit (XGB).
Details: `references/ALGORITHM_GUIDE.md`.

## Tool routing
Feature: RDKit (opt. Mordred/PaDEL) · Models: scikit-learn, LIBSVM, XGBoost, LightGBM, CatBoost ·
ML: DeepChem/MoleculeNet, DeepMol · Pipelines: AMPL, QSPRpred · AutoML: QSARtuna, ZairaChem ·
Visual: KNIME+RDKit · Hosting: Flame · Multi-target: QSAR-Co-X · Conformal: CPSign · Rescore: ODDT/
RF-Score-VS · Endpoint: OPERA/CompTox · Online: OCHEM/openOCHEM, QITB · Pretrained: Ersilia Model Hub ·
Benchmarks: TDC, MoleculeNet. Links/licenses: `references/OPEN_SOURCE_TOOLS.md`.

## CLI (all offline, leakage-aware, reuse the model bundle)
`audit`+`train`+`predict` as above, plus:
| Subcommand | Purpose (key flags) |
|---|---|
| `analyze` | Dataset EDA: composition, duplicates, scaffold diversity, class balance, similarity, cluster/PCA → `analysis.json`, `dataset_layout.csv` (`--input --smiles-column --target-column --task --output-dir`) |
| `conformal` | Inductive conformal prediction sets/intervals + coverage report (`--model --trust-model --calibration --target-column --task --alpha --query --output`) |
| `ensemble` | Multi-model consensus & disagreement → `consensus_score`, `consensus_std` (`--predictions ... --score-column --task --output-dir`) |
| `select` | MaxMin diversity-aware batch (optional `--domain-only`, `--min-score`, `--feasibility-column`) → `pairwise_mean_similarity` (`--predictions --score-column --budget --output`) |
| `interpret` | Permutation/intrinsic importance + top Morgan-bit→molecule mapping (`--model --trust-model --data --output-dir --top-n`) |

Outputs per command: `--help` for full flags. `analyze`/`conformal`/`ensemble`/`select`/`interpret`
are described further in README.md.

## Failure modes (edge cases) → required response
| Failure | Response |
|---|---|
| Too few compounds | Reduce claims, prefer simple models, repeated/grouped validation, seek data |
| Only actives available | Don't invent inactives; use ranking, one-class/domain methods, or get screened negatives |
| Conflicting replicates | Investigate assay/provenance; aggregate only with a documented rule |
| One scaffold dominates | Grouped split; report scaffold-specific performance; diversify acquisition |
| Split lacks a class | Change split seed/design without consulting test outcomes; record the rule |
| SVM too slow | Linear SVM, kernel approximation, smaller tuning set, or boosted trees |
| XGBoost unavailable | Run classical GB and document; don't rename it XGBoost |
| Strong CV, weak external test | Diagnose similarity/leakage/shift; don't tune against external labels |
| Poor calibration | Recalibrate on inner folds; report ranking and probability quality separately |
| Mostly OOD library | Acquire representative labels or restrict claims; don't force ranking as reliable |
| Importance changes by fold | Report instability; avoid mechanistic conclusions |
| Web predictor disagrees | Check endpoint/model/domain/version; don't average blindly |

## Security & privacy
- Local-only, no network requests. Reads only user-supplied paths, writes only to the requested output.
- Never loads untrusted `.joblib`/pickle (Python deserialization can execute code).
- External sites optional; obtain explicit permission before sending proprietary data.
- Review third-party package/model licenses before commercial use.

## Report structure
Conform to `templates/DRUG_DISCOVERY_REPORT_TEMPLATE.md`: decision & intended use · data provenance
& license · endpoint definition · curation · representations · split rationale & train–test similarity ·
models & tuning · metrics with uncertainty · calibration & domain · interpretation stability ·
selection rule & diversity · limitations & prohibited uses · prospective validation plan ·
reproducibility artifacts & versions.

## References (loaded on demand)
`RESEARCH_REPORT.md` (evidence review) · `ALGORITHM_GUIDE.md` (mechanics/tuning) ·
`VALIDATION_PROTOCOL.md` (leakage-resistant validation & metrics) · `OPEN_SOURCE_TOOLS.md`
(software matrix) · `PROJECT_BRIEF.md` · `DRUG_DISCOVERY_REPORT_TEMPLATE.md`.

## Verify
`python3 scripts/verify_integrity.py` and `sha256sum -c CHECKSUMS.sha256` (see README).
