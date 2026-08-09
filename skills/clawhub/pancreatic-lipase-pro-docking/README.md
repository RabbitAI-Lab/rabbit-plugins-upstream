# 🧬 Pancreatic Lipase Pro Docking

**Categories:** research  
**Public tags:** #research, #drug-discovery, #molecular-docking, #pancreatic-lipase, #bioinformatics

## ✨ Functionalities

Professional virtual-screening stack for human pancreatic lipase (PDB 1LPB). Multi-site molecular docking (catalytic triad, oxyanion hole, lid, etc.), molecule preparation, scoring, hit selection, and report generation.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/pancreatic-lipase-pro-docking
```

Prepare the documented conda environment, supply authorized receptor/ligand inputs, run the multi-site pipeline, validate results, and treat scores as computational predictions.

A representative command from the unchanged skill documentation is:

```bash
bash run_pipeline.sh molecules.txt --redock 10 --workers 2   # end-to-end
python multi_site_docking.py --check                          # env self-test
python multi_site_docking.py --ligands ligands.csv --workers 2 --debug --log-file run.log
python validate_results.py --results dock_results/results_all_sites.csv
bash run_tests.sh                                             # 24 tests
python3 build_report.py --results dock_results/results_all_sites.csv
# classic single-site: bash restore_and_run.sh ligands.csv
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Requires conda environment with rdkit, meeko, vina, gemmi, openbabel
• Runs AutoDock Vina locally (CPU/GPU)
• Reads receptor PDB + ligand SDF/SMILES input
• May download molecules from PubChem (network)

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Runs compute-heavy docking locally.
- May fetch molecule data from PubChem; no sensitive data sent.
- No secrets are involved.
- Results are computational predictions — validate experimentally.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `d78da944bfe1d1e00336933e9433a344dd3279d187487cb75befbf4067f165fa`

Run from the installed skill directory:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
root = Path('.')
excluded_parts = {'.git', '.clawhub', '__pycache__', '.pytest_cache'}
excluded_names = {'readme.md', 'skill-card.md', '_meta.json', '.published', '.ds_store'}
files = sorted(
    (p for p in root.rglob('*') if p.is_file()
     and not any(part in excluded_parts for part in p.relative_to(root).parts)
     and p.name.lower() not in excluded_names),
    key=lambda p: p.relative_to(root).as_posix(),
)
h = hashlib.sha256()
h.update(b'TREE-SHA256-v1\0')
for p in files:
    rel = p.relative_to(root).as_posix().encode('utf-8')
    data = p.read_bytes()
    h.update(rel); h.update(b'\0')
    h.update(str(len(data)).encode('ascii')); h.update(b'\0')
    h.update(data); h.update(b'\0')
print(h.hexdigest())
PY
```

The printed digest must exactly match the value above. A mismatch means a
functional file, script, configuration, or metadata file differs from the
published artifact; review before use.


## 📚 Complete Skill Reference (Unchanged)

The text below is copied from the installed `SKILL.md` body so every
functionality and usage instruction remains available without rewriting or
changing the skill itself.

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

---

*README-only documentation remediation. No functional artifact file was changed.*
