---
name: classical-ml-drug-discovery
description: "Build defensible molecular ML for drug discovery — QSAR, virtual screening, ADMET, toxicity, binding affinity, drug-target models — with Random Forest, SVM/SVR, and Gradient Boosting, plus dataset analysis, inductive conformal prediction, multi-model consensus, diversity-aware batch selection, and cheminformatics-aware interpretation. Use for curating bioactivity data, comparing RF/SVM/XGBoost, leakage-resistant validation, library screening, calibrated uncertainty, disagreeing-model reconciliation, diverse assay-batch selection, feature-to-molecule mapping, applicability-domain assessment, or auditing a molecular ML paper."
version: 1.4.2
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
13. **Run `validate` (Y-randomization) before reporting any performance number** — a good score on small or heavily tuned data can be chance correlation. Report the p-value with the metric.
14. **A flagged field is not evidence.** `underpowered: true` means the test carries no information either way; `domain_threshold_degenerate: true` means `in_domain` is trivially true for everything. Never cite either as support. Run `schema` for the machine-readable trust contract.

## Fast path
```bash
SKILL_DIR="${SKILL_DIR:-$HOME/skills/classical-ml-drug-discovery}"
python3 "$SKILL_DIR/scripts/qsar_pipeline.py" audit   --input compounds.csv --smiles-column smiles --target-column activity --task classification --output-dir audit_output
python3 "$SKILL_DIR/scripts/qsar_pipeline.py" train   --input compounds.csv --smiles-column smiles --target-column activity --task classification --split scaffold --models rf svm gb xgb --output-dir qsar_run
python3 "$SKILL_DIR/scripts/qsar_pipeline.py" validate --model qsar_run/model.joblib --trust-model --input compounds.csv --smiles-column smiles --target-column activity --n-permutations 20 --output-dir qsar_run/validation
python3 "$SKILL_DIR/scripts/qsar_pipeline.py" predict --model qsar_run/model.joblib --trust-model --input library.csv --smiles-column smiles --output predictions.csv
```
`xgb` is optional (skipped with a message if not installed). Deps: `requirements-optional.txt`.

## Full workflow — 12 steps (detail: `references/WORKFLOW.md`)
1. **Define the decision** — endpoint, deployment population, budget, error costs, evidence required.
2. **Data with provenance** — source, version, date, query, assay filters, units, license.
3. **Curate** — parse/sanitize, parent policy, dedupe standardized parents, aggregate replicates, normalize units.
4. **Representations** — benchmark >=2 (Morgan bits + physchem panel is the CLI default).
5. **Freeze the test design** — match the split to the deployment claim (random / temporal / scaffold / cluster / drug-cold / target-cold / external-lab). Scaffold split is not an OOD guarantee; report train-test nearest-neighbor similarity.
6. **Mandatory baselines** — prevalence or mean, nearest-neighbor similarity, linear, RF, SVM/SVR, GB/XGB on identical splits.
7. **Tune without leakage** — nested or inner CV, group-aware folds, chronology preserved; never tune on the frozen test set.
8. **Evaluate the decision** — classification/screening: PR-AUC, precision or hit rate at budget, EF/BEDROC, MCC; regression: MAE, RMSE, R², Spearman, top-k recovery. Always with CIs.
9. **Applicability domain & uncertainty** — nearest-neighbor Tanimoto, calibration, conformal. Coverage holds only under exchangeability.
10. **Interpret safely** — held-out permutation importance first; attribution is associative, never causal.
11. **Select a batch** — never top-N: combine score, domain, uncertainty, diversity, novelty, feasibility, med-chem review.
12. **Validate & learn** — escalate retrospective -> orthogonal model -> biochemical -> cellular -> in vivo; feed back positives AND negatives.

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
| `validate` | **Y-randomization / Y-scrambling chance-correlation test.** Refits on shuffled labels and reports an empirical p-value + verdict (`--model --trust-model --input --target-column --n-permutations --output-dir`). Exit 0 ok · 4 chance not excluded · 5 underpowered |
| `schema` | JSON Schemas of every output + the trust contract, for models that never read prose (`[--name ID] [--compact]`) |

Outputs per command: `--help` for full flags. `analyze`/`conformal`/`ensemble`/`select`/`interpret`
are described further in README.md.

## Failure modes → required response
Twelve named situations (too few compounds · only actives · conflicting replicates ·
one dominant scaffold · split lacks a class · SVM too slow · XGBoost unavailable ·
strong CV but weak external test · poor calibration · mostly-OOD library · unstable
importance · web predictor disagrees) with the required response for each:
`references/FAILURE_MODES.md`. Never resolve one by weakening a claim silently —
state the limitation in the report.

## Security & privacy
- **Local-only: the CLI makes no network requests of any kind.** It reads only
  user-supplied paths and writes only to the requested output directory. Data
  sources named in this document (ChEMBL/EBI, PubChem, BindingDB, TDC) are places
  a **human** downloads data from by hand — the skill never contacts them, and it
  declares no network capability.
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
`WORKFLOW.md` (the 12 steps in full) · `FAILURE_MODES.md` (edge-case responses) ·
`RESEARCH_REPORT.md` (evidence review) · `ALGORITHM_GUIDE.md` (mechanics/tuning) ·
`VALIDATION_PROTOCOL.md` (leakage-resistant validation & metrics) · `OPEN_SOURCE_TOOLS.md`
(software matrix) · `PROJECT_BRIEF.md` · `DRUG_DISCOVERY_REPORT_TEMPLATE.md`.

## Verify
`python3 scripts/verify_integrity.py` and `sha256sum -c CHECKSUMS.sha256` (see README).
