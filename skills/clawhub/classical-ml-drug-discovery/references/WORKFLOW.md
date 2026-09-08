# Full QSAR workflow (loaded on demand)

Referenced from `SKILL.md`. The twelve steps below are the detailed form of the
compact checklist in the skill body. Read this file when you are actually
executing a step, not to decide whether the skill applies.

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

