# 🧪 Classical ML Drug Discovery

**Category:** research, development, knowledge

Builds defensible molecular ML workflows (Random Forest, SVM/SVR, Gradient Boosting) and turns
predictions into a diverse, uncertainty-aware experimental shortlist — not unsupported claims.

## What it does
- Curate bioactivity data (SMILES, assay labels) and audit duplicates/conflicts;
- choose leakage-resistant splits (random/scaffold/temporal/DTI-cold);
- compare RF, SVM/SVR, GB, and optional XGBoost inside folds;
- calibrate uncertainty (inductive conformal prediction), reconcile multi-model consensus;
- select a chemically diverse assay batch; map feature importance back to molecules;
- produce a reproducible report. CLI subcommands: `audit train predict analyze conformal
  ensemble select interpret`.

## 🔐 Permissions & requirements
- **Required:** Python 3.10+, NumPy, pandas, scikit-learn, joblib, RDKit.
- **Optional:** xgboost, lightgbm, catboost, shap.
- **Filesystem:** reads only user-supplied paths; writes only to the requested output dir; offline (no network).
- **API keys:** none required.

## 🔒 Security & privacy
- Local-only, no network requests, no telemetry, no environment/API-key reading.
- **Never load an untrusted `.joblib`/pickle file** — Python deserialization can execute code.
- External sites optional; get explicit permission before sending proprietary structures/labels.
- Review third-party package/model licenses before commercial use.
- Model scores are decision support, not evidence of efficacy/safety.

## 🚀 Quick start
```bash
python3 scripts/qsar_pipeline.py audit   --input compounds.csv --smiles-column smiles --target-column activity --task classification --output-dir audit_output
python3 scripts/qsar_pipeline.py train   --input compounds.csv --smiles-column smiles --target-column activity --task classification --split scaffold --models rf svm gb xgb --output-dir qsar_run
python3 scripts/qsar_pipeline.py predict --model qsar_run/model.joblib --trust-model --input library.csv --smiles-column smiles --output predictions.csv
```

## 📚 Included
- `SKILL.md` — operational protocol, non-negotiable rules, failure modes.
- `references/` — ALGORITHM_GUIDE, OPEN_SOURCE_TOOLS, VALIDATION_PROTOCOL, RESEARCH_REPORT.
- `templates/` — PROJECT_BRIEF, DRUG_DISCOVERY_REPORT_TEMPLATE.
- `scripts/qsar_pipeline.py`, `scripts/verify_integrity.py`; `tests/test_smoke.py`, `tests/test_advanced.py`.

## ✅ Verification
```bash
python3 scripts/verify_integrity.py
sha256sum -c CHECKSUMS.sha256
```
**Canonical artifact SHA-256:** `c0a2ed1e9cf8ab58a5422659bde07f96ab1662c1986efe29c29aaf27bc686a1c`

## License
Apache License 2.0. See `LICENSE`.
