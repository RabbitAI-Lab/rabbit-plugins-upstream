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
**Canonical artifact SHA-256:** `0f7a200b4cb84ee05cf4aadd27c53104340cb6fc06a609d2da4794832be3a56e`

## License
Apache License 2.0. See `LICENSE`.


## New in v1.4.0

### `validate` — Y-randomization (chance-correlation) check
A good score on small or heavily tuned data can be pure chance. `validate` refits
the same pipeline on shuffled labels and reports an empirical p-value:

```bash
python3 scripts/qsar_pipeline.py validate --model qsar_run/model.joblib --trust-model \
  --input compounds.csv --smiles-column smiles --target-column activity \
  --n-permutations 20 --output-dir qsar_run/validation
```

`p = (1 + #{null >= real}) / (1 + n_permutations)`. Exit codes: `0` ok ·
`4` chance not excluded · `5` underpowered.

**Underpowered runs are labelled, not misreported.** A permutation test can never
return a p-value below `1/(n+1)`, so fewer than 19 permutations makes `p <= 0.05`
unreachable. Rather than call that "chance not excluded", the tool reports
`UNDERPOWERED` and tells you how many permutations you need.

Y-randomization tests only chance correlation on this data under this CV. It says
nothing about novel-chemotype generalization, applicability domain, or biology.

### `schema` — machine-readable output contracts
```bash
python3 scripts/qsar_pipeline.py schema            # all schemas + trust contract
python3 scripts/qsar_pipeline.py schema --compact  # minified, fewer tokens
```
Emits JSON Schemas for `qsar_validate.v1`, `qsar_select.v1` and `qsar_train.v1`,
plus a `trust_contract` listing fields that may **never** be cited as evidence
(e.g. `in_domain` when `domain_threshold_degenerate` is true).

### Fixes
- `select --budget 0` returned the **entire** candidate pool (0 is falsy in
  Python, so it fell through to the default). Budgets below 1 are now rejected,
  and a budget above the pool size warns and reports both numbers.
- `conformal` on a model without `predict_proba` produced all-zero nonconformity
  scores and reported **100% coverage** that meant nothing. It now falls back to a
  decision-function margin (a valid nonconformity measure — empirically 89.9%
  coverage at a 90% target) and refuses outright if no class score exists.
- A `0.0` applicability-domain threshold silently marked every compound
  `in_domain`; runs now emit `domain_threshold_degenerate` and a warning.
- Test suites raised `SkipTest` at import, printing a traceback and exiting **0** —
  indistinguishable from a pass. They now skip loudly with exit **77**.
- `TOOL_VERSION` (1.3.0) had drifted from `SKILL.md` (1.3.2), so model cards
  recorded the wrong provenance. A test now asserts they match.

### v1.4.1 — both ClawHub scanner findings fixed
The v1.4.0 upload was flagged `suspicious`. The scanner named two behaviours and
**both were real**:

- **Package verification failed for every consumer.** v1.4.0 added a
  `.clawhubignore`, and `verify_integrity.py` hashed it — but the registry strips
  every dot-path, so the installed copy was missing a file the checksum manifest
  listed. `verify_integrity.py` and `sha256sum -c` therefore FAILED on every
  install, breaking this skill's own headline "Verify" step. Hashing now skips any
  path the registry will strip, and a regression test reconstructs the published
  tree and verifies it.
- **Contradictory network declaration.** The frontmatter advertised optional
  network hosts while the body promised "no network requests". The CLI genuinely
  never opens a socket, so the capability declaration was removed and the wording
  clarified: those hosts are places a **human** downloads data from by hand. A test
  now asserts the frontmatter declares no network capability and that the scripts
  contain no network calls.

### v1.4.2 — conformal score-matrix shape guard (third scanner finding)
The scanner confirmed a conformal flaw that "can silently produce misleading
uncertainty results for some trusted models". Real: `conformal_ncs` indexed the
score matrix by class index without checking its shape. `--trust-model` accepts
externally built bundles, so an estimator returning a one-vs-one decision matrix
(`n(n-1)/2` columns, not `n_classes`), or any wrapper with a different column
layout, had its nonconformity read from an unrelated column — yielding a
confident, silently wrong prediction set. Both the probability and
decision-function paths now verify the matrix is `(n_samples, n_classes)` and
refuse with an explanatory error instead of guessing. Four regression tests cover
one-vs-one matrices, wrong-width probabilities, a 1-D decision function on a
multiclass bundle, and the valid one-vs-rest path.
