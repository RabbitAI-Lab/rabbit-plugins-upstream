# Debugging Guide — hPL docking stack (v100.3.0)

Best practices applied (from the 2026-08-03 audit; sources: Python logging docs,
exception-handling guides, PEP 8, FAIR scientific-software practices).

## 1. Environment self-check first (`--check`)
Always run before anything else when a job misbehaves:
```bash
python multi_site_docking.py --check        # or redock_high.py --check
```
Prints python/vina/obabel/rdkit/meeko/gemmi/numpy versions, flags missing
REQUIRED tools, exits non-zero on problems. Paste the output into a bug report.

## 2. Verbose logging (`--debug`, `--log-file`)
```bash
python multi_site_docking.py --ligands ligands.csv --debug --log-file run.log
```
- Structured logs with timestamps + levels to stderr and/or a file.
- Every external command is logged (`RUN: vina --receptor ...`).
- On failure, the exact failing command + stdout/stderr tails are logged, so the
  run is reproducible from the log alone.
- No bare `except:` anywhere — all failures log a full traceback.

## 3. Fail-closed error handling
- Domain exceptions: `DockingError`, `PrepError`, `ConfigError`, `ValidationError`
  (see `debug_utils.py`). Always chained with `raise ... from e` to keep context.
- Inputs are validated BEFORE any expensive compute (`require_file`,
  `require("smiles" in header)`).
- A global exception hook logs any uncaught exception — nothing fails silently.

## 4. Reproducibility
Every run writes `versions.json` next to its results (python/vina/rdkit/meeko/
gemmi/numpy versions + seed + exhaustiveness + full command line). Fixed seeds
everywhere (default 42).

## 5. Validate outputs (`validate_results.py`)
```bash
python validate_results.py --results dock_results/results_all_sites.csv --runs-dir dock_results/runs
```
Checks: rows exist, statuses valid, every `ok` row has a numeric score in a
plausible range (−15..−2 kcal/mol), all 5 sites covered, `vina.log` files exist.
Exits non-zero (gate for CI / pipelines) when decision-grade quality is violated.
Rows marked `ok` without a score = **silent fake** → hard FAIL.

## 6. Tests (`run_tests.sh` / pytest)
```bash
bash run_tests.sh            # uses the conda env if present
# or: python -m pytest tests/ -v
```
24 tests (≈2 s, no docking needed):
- `test_debug_utils.py` — logging, exceptions, env-check, run_cmd, versions
- `test_sites.py` — triad detection (true geometry found; distant cluster
  rejected), oxyanion/lid/pocket/cterm windows, receptor cleaning, chain pick,
  and the **real 1LPB** check (Ser152-Asp176-His263 + validated grid centers)
- `test_parsing.py` — vina score parsing, unicode name asciify
- `test_cli.py` — validate_results PASS/FAIL gates, build_report sections

## 7. Troubleshooting quick table
| Symptom | Likely cause | Action |
|---|---|---|
| `--check` shows vina MISSING | conda env not activated | `micromamba run -p plenv ...` or add plenv/bin to PATH |
| "catalytic triad ... not found" | wrong chain/receptor | verify receptor has the catalytic chain; use `--receptor` |
| all jobs `failed` instantly | meeko prep output dir missing | mkdir receptor/ ligprep/ runs/ (auto since v100.2.1) |
| `pending: 0` in redock_high | SMILES CSV not found | pass `--ligands molecules_resolved.csv` (since v100.2.2) |
| OOM / `Killed` | ligand with >20 rotatable bonds | raise `--max-rotb` on bigger RAM, or filter |
| scores look random at colipase | interface site is a protein-protein surface | expected — weak absolute scores, use ranking only |
