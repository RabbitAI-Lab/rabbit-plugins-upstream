# Package Manifest

This zip contains a self-contained professional docking workflow for Arena.ai Agent Mode.

## Core execution
- `run_uploaded_molecules.sh` — easiest wrapper for uploaded CSV files
- `docking_speed_pipeline.py` — main speed/capacity optimized pipeline
- `docking_10x_pipeline.py` — checkpointed professional pipeline
- `lipase_docking_fastkit.py` — pancreatic lipase docking backend/template

## Large-library support
- `library_chunker.py`
- `merge_screen_results.py`
- `select_top_diverse_hits.py`
- `run_10k_end_to_end.sh`
- `SLURM_chunk_array_template.sh`

## Executive output GUI
- `generate_executive_dashboard.py`
- `executive_dashboard_demo.html`

## Validation/debugging
- `workflow_linter.py`
- `verify_stack.py`
- `verify_full_stack.py`

## Installation
- `environment.yml`
- `environment_full.yml`
- `requirements_pip_fallback.txt`
- `requirements_full_pip.txt`
- `setup_mamba.sh`
- `setup_full_stack.sh`
- `Dockerfile`

## Documentation
- `ARENA_AGENT_INSTRUCTIONS.md`
- `QUICKSTART_FOR_USER.md`
- `professional_docking_blueprint.md`
- `GI_FLUID_OPTIMIZATION.md`
- `SPEED_CAPACITY_GUIDE.md`
- `CHUNKING_PARALLEL_STRATEGY.md`
- `MAX_READY_CHECKLIST.md`
- `MAX_THROUGHPUT_COMMANDS.md`
- `BUG_HOTSPOTS_AND_FIXES.md`
- `OPTIONAL_TOOLS_MANIFEST.md`

## v100.2.0 additions
- multi_site_docking.py  — 5-position site-specific docking (auto site detection, checkpointed, parallel)
- redock_high.py         — high-exhaustiveness re-dock of top-N + ex2-vs-ex16 comparison
- build_report.py        — final markdown report (ground truth + optional AI analyses)
- resolve_names.py       — PubChem name->SMILES resolver (GET, unicode-safe, ConnectivitySMILES fallback)
- run_pipeline.sh        — end-to-end orchestrator (resolve -> dock -> redock -> report)
- REPORT_PIPELINE.md     — pipeline + debug documentation

## v100.3.0 additions (debugging & testing layer)
- debug_utils.py            — structured logging, domain exceptions, env self-check, run_cmd with context, versions.json
- validate_results.py       — post-run output validation (fail-closed gates, CI-friendly exit codes)
- tests/ (pytest)           — 24 tests: site detection (synthetic + real 1LPB), parsing, resolvers, CLI gates
- run_tests.sh              — test runner (uses conda env when present)
- DEBUGGING.md              — best-practice debugging guide + troubleshooting table
