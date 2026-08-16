# 🧪 Classical ML Drug Discovery

A rigorous ClawHub skill for planning, building, auditing, interpreting, and reporting molecular
machine-learning workflows based on **Random Forests**, **Support Vector Machines/Regression**,
and **Gradient Boosting**.

It converts the evidence and practical guidance in the bundled deep-research report into an
agent protocol, a local command-line pipeline, validation checklists, open-source tool routing,
and reusable drug-discovery report templates.

## What it does

The skill helps an agent or researcher:

- define a drug-discovery modeling decision and exact biological endpoint;
- curate SMILES, assay labels, duplicates, conflicts, and standardized parent structures;
- calculate Morgan fingerprints and compact RDKit descriptors;
- create random, scaffold-grouped, or temporal holdouts;
- compare Random Forest, SVM/SVR, classical Gradient Boosting, and optional XGBoost;
- tune models inside training data with group-aware or standard cross-validation;
- calculate classification/regression and virtual-screening-relevant metrics;
- estimate a structural applicability-domain threshold from training similarities;
- serialize a model and generate a model card, audit, split file, predictions, and feature
  importance;
- predict external libraries with nearest-training similarity and domain flags;
- select diverse, uncertainty-aware experimental candidates;
- audit leakage, class imbalance, calibration, explanation stability, and unsupported claims;
- route users to open-source libraries, workflows, pretrained models, and web resources;
- produce a complete reproducible drug-discovery report.

## Scientific boundaries

This skill is computational decision support. It does **not** prove:

- target binding;
- biological efficacy;
- selectivity;
- absence of toxicity;
- mechanism of action;
- clinical safety or benefit.

Predicted candidates require appropriate biochemical, cellular, ADME/toxicity, and—only when
justified—in vivo validation. The skill explicitly prohibits treating a web predictor or model
score as experimental evidence.

## Quick start

```bash
# Install required Python packages in an isolated environment.
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-optional.txt

# Audit a labeled molecular dataset.
python3 scripts/qsar_pipeline.py audit \
  --input compounds.csv \
  --smiles-column smiles \
  --target-column activity \
  --task classification \
  --output-dir audit_output

# Compare RF, SVM, classical GB, and XGBoost with a scaffold holdout.
python3 scripts/qsar_pipeline.py train \
  --input compounds.csv \
  --smiles-column smiles \
  --target-column activity \
  --task classification \
  --split scaffold \
  --models rf svm gb xgb \
  --output-dir qsar_run

# Score a new library locally.
python3 scripts/qsar_pipeline.py predict \
  --model qsar_run/model.joblib \
  --trust-model \
  --input library.csv \
  --smiles-column smiles \
  --output predictions.csv
```

Run `python3 scripts/qsar_pipeline.py <audit|train|predict> --help` for every option.

## Inputs and outputs

### Input

A CSV containing at least:

- a SMILES column;
- for `audit` and `train`, a classification label or numerical regression response.

Optional time splitting requires a date/time column. Every modeled source row must have a
parseable timestamp. When one standardized parent has measurements at multiple times, the CLI
assigns the entire aggregated parent to its **latest** source timestamp before it creates the
cutoff. This conservative quarantine prevents an aggregate containing a later label from leaking
into an earlier training block; the assignment is recorded in `split_assignments.csv` and
`data_audit.json`.

### Training outputs

- `model.joblib` — fitted pipeline plus feature/domain metadata;
- `metrics.json` — inner CV and frozen holdout metrics;
- `test_predictions.csv` — holdout predictions and similarity/domain fields;
- `split_assignments.csv` — exact train/test assignment;
- `data_audit.json` — invalid, duplicate, conflict, and curation counts;
- `curated_data.csv` — standardized modeling records;
- `feature_importance.csv` — available tree/linear importance;
- `model_card.md` — intended use, data, model, performance, and limitations.

## Included knowledge

- `SKILL.md` — operational agent protocol and safety rules.
- `references/RESEARCH_REPORT.md` — the complete deep-research report with 60 references.
- `references/ALGORITHM_GUIDE.md` — RF/SVM/GB mechanics, selection, and tuning.
- `references/VALIDATION_PROTOCOL.md` — split, leakage, metric, calibration, and domain rules.
- `references/OPEN_SOURCE_TOOLS.md` — software/web matrix with license caveats.
- `templates/PROJECT_BRIEF.md` — project-definition form.
- `templates/DRUG_DISCOVERY_REPORT_TEMPLATE.md` — final report structure.
- `scripts/qsar_pipeline.py` — local audit/train/predict implementation.
- `tests/test_smoke.py` — local end-to-end smoke test.

## 🔐 Permissions and requirements

### Required runtime

- Python 3.10 or newer recommended;
- NumPy;
- pandas;
- scikit-learn;
- joblib;
- RDKit.

### Optional runtime

- XGBoost for `--models xgb`;
- LightGBM, CatBoost, and SHAP for manually extended workflows;
- an isolated virtual environment or container is strongly recommended.

### Filesystem access

The bundled CLI:

- reads only the input CSV and model path explicitly supplied by the user;
- writes only to the specified output directory or output CSV;
- serializes the fitted model and metadata to `model.joblib`;
- does not scan unrelated files.

### Network access

The bundled CLI makes **no network requests**. Network is optional only when an agent retrieves
public literature/data or the user explicitly chooses a third-party web predictor. Obtain explicit
permission before sending confidential structures, targets, or assay labels to any external service.

### API keys and secrets

No API key, credential, or secret is required by the bundled CLI. The skill does not read, store,
or log credentials.

## 🔒 Security & Privacy

### Data read or collected

The CLI reads user-provided molecular structures, labels, optional timestamps, and a previously
created local model bundle. It does not collect telemetry.

### Does data leave the machine?

No. The bundled scripts are local-only. If an agent uses optional websites listed in the reference
guide, data sent to those sites leaves the machine and becomes subject to their policies. Do not
upload proprietary or personal data without authorization.

### Model deserialization risk

`joblib` uses Python pickle semantics. Loading an untrusted `model.joblib` can execute malicious
code. Only load models created by you or a trusted source, and verify checksums before use.

### Chemical and scientific risks

- Invalid or unusual chemistry may not be represented correctly.
- Standardization can merge scientifically distinct forms.
- Random or scaffold validation can overestimate prospective novelty.
- An applicability-domain flag is not a safety certificate.
- Feature importance and SHAP are not mechanistic proof.
- Model predictions must not replace laboratory, clinical, or regulatory evidence.

### Dependency and supply-chain risks

Install dependencies in an isolated environment, pin versions for production, review package
licenses, and retain an environment lock file. XGBoost, RDKit, and other compiled packages should
come from trusted package channels.

### Review before installation

Inspect at minimum:

```bash
sed -n '1,260p' SKILL.md
sed -n '1,260p' scripts/qsar_pipeline.py
cat requirements-optional.txt
python3 scripts/verify_integrity.py
sha256sum -c CHECKSUMS.sha256
```

## ✅ Verification hash

**Canonical artifact SHA-256:** `fe0422c5dcc576236e9259488e3ec4ce905ef1a80b1114276742e32e0e6ae92e`

The canonical hash covers every published file except `CHECKSUMS.sha256`, `.published`, cache
files, and compiled bytecode. During hashing, the 64-character value on the canonical-hash line
above is normalized to zeros, allowing README verification without a circular self-hash.

Verify:

```bash
python3 scripts/verify_integrity.py
sha256sum -c CHECKSUMS.sha256
```

The second command checks exact per-file SHA-256 values for all functional artifacts other than
`README.md`, `CHECKSUMS.sha256`, publication markers, and cache files. The first command also
covers the normalized README.

## License

Apache License 2.0. See `LICENSE`.

## Citation and evidence

The skill bundles a 60-reference research report covering foundational algorithm papers,
prospective virtual-screening examples, molecular benchmarking, OECD QSAR guidance, and
current open-source project documentation. Cite the original model, data, software, and assay
sources in every scientific output.
