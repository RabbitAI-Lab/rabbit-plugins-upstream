---
name: pancreatic-lipase-pro-docking
version: 100.3.4
author: orionshaowswmw
license: MIT
category: education
categories: [education, research, science, chemistry]
description: Professional virtual-screening stack for human pancreatic lipase PDB 1LPB. v100.3.0 adds an observability & testing layer: structured logging, fail-closed domain exceptions, environment self-check (--check), reproducibility records (versions.json), output validation (validate_results.py), and a 24-test pytest suite — plus all v100.2.x multi-site (5-position) docking + report pipeline features.
tags:
  - education
  - research
  - science
  - chemistry
  - drug-discovery
  - docking
  - autodock-vina
  - rdkit
  - pancreatic-lipase
  - virtual-screening
  - bioinformatics
type: command
metadata: {"openclaw":{"emoji":"🧬"}}
---

# pancreatic-lipase-pro-docking 🧪🧬 v100.3.4 — DEBUGGING & TESTING LAYER (CLEANUP)

One-command virtual screening against human pancreatic lipase (hPL / PNLIP, PDB 1LPB): molecule names or ligand CSV → multi-site docking across **5 functional positions** → high-exhaustiveness re-dock → executive report. **Fail-closed**: never silent fake scores. v100.3.0 adds the debugging/observability layer distilled from best practices.

## v100.3.4 — release note
Same cleanup payload as v100.3.2/100.3.3. Registry versioning note: 100.3.2
registered server-side but never became installable (stuck tag/index), 100.3.3
was the live release of the cleanup payload, and 100.3.4 aligns the frontmatter
version with the registry version. Content is identical in all three.

## v100.3.2 — CLEANUP (2026-08-03, from full pyflakes audit)
Removed dead code flagged by pyflakes across 7 modules (no functional change —
verified by compile + 24-test suite + real docking smoke test):
- docking_speed_pipeline.py: unused `math` import; unused `hba` read (GI-flags fn)
- generate_executive_dashboard.py: unused `defaultdict`; redundant local `import math`
  inside the donut loop (top-level import already present); dead `tool_status` var
- lipase_docking_fastkit.py: unused `math`, `sys` imports
- professional_docking_runner.py: unused `shutil` import
- select_top_diverse_hits.py: unused `re`, `pathlib.Path` imports
- workflow_linter.py: unused `os` import
- tests/: unused `pytest`/`logging`/`json` imports
Result: `pyflakes` = 0 findings across the whole stack + tests (was 14).

## v100.3.1 — patch: tests resolve their stack root relative to themselves, so the
suite runs identically from the payload layout or a dev checkout (24/24 pass).

## v100.3.0 — Debugging & testing (best practices applied)
1. **`--check` environment self-test** — prints python/vina/rdkit/meeko/gemmi versions, flags missing REQUIRED tools, non-zero exit. Run it first whenever a job misbehaves.
2. **Structured logging** (`--debug`, `--log-file`) — timestamps + levels; every external command logged; on failure the exact command + stdout/stderr tails are logged for reproduction.
3. **Fail-closed exceptions** (`debug_utils.py`) — domain exceptions `DockingError/PrepError/ConfigError/ValidationError`, chained (`raise ... from e`); inputs validated before compute; global exception hook logs any uncaught exception (nothing silent).
4. **Reproducibility** — every run writes `versions.json` (tool versions + seed + exhaustive + cmdline); fixed seeds.
5. **Output validation** (`validate_results.py`) — rows/status/score-range (−15..−2) sanity, 5-site coverage, vina.log presence; rows marked `ok` without a score = hard FAIL; non-zero exit for CI gating.
6. **24-test pytest suite** (`tests/`, ~2 s, no docking needed): site detection (true triad found, distant cluster rejected, real 1LPB → Ser152-Asp176-His263 with validated centers), vina log parsing, unicode name resolution, validator/report CLI gates. `bash run_tests.sh`.
7. **DEBUGGING.md** — full guide + troubleshooting table.

## v100.2.x — Multi-site (5 positions) + report pipeline (kept)
- **The 5 positions**, auto-detected from structure (atom-composition + tight H-bond geometry, robust to numbering offsets): catalytic triad · oxyanion hole · lid (β5/amphipathic helix) · hydrophobic substrate pocket · colipase C-terminal interface
- `resolve_names.py` (PubChem name→SMILES, unicode-safe, ConnectivitySMILES fallback) · `multi_site_docking.py` (checkpointed, parallel, memory-guarded) · `redock_high.py` (ex16 re-dock + comparison) · `build_report.py` + `run_pipeline.sh` (report pipeline with AI multi-provider hook, no credentials embedded)
- Debug fixes: triad false-positive (tight geometry), meeko output-dir creation, redock SMILES lookup path

## v100.1.4 — BUGFIX (kept)
vina 1.2 `--log` removed → stdout captured as vina.log; PEP-701 f-string → py≤3.11 safe. Verified with real docking (ibuprofen −7.29, caffeine −6.78 kcal/mol).

## Quick Start
```bash
bash run_pipeline.sh molecules.txt --redock 10 --workers 2   # end-to-end
python multi_site_docking.py --check                          # env self-test
python multi_site_docking.py --ligands ligands.csv --workers 2 --debug --log-file run.log
python validate_results.py --results dock_results/results_all_sites.csv
bash run_tests.sh                                             # 24 tests
python3 build_report.py --results dock_results/results_all_sites.csv
# classic single-site: bash restore_and_run.sh ligands.csv
```
Receptor: `receptor/1LPB.pdb` next to the stack (or `--receptor PATH`). Requires python 3.9+ with rdkit, meeko, vina, gemmi (conda-forge: `micromamba create -p plenv -c conda-forge python=3.11 rdkit meeko vina gemmi openbabel pytest`).

*Built by [@rustyorb](https://github.com/rustyorb) — for authorized research and education. Only test systems/endpoints you own or have permission to audit.*
