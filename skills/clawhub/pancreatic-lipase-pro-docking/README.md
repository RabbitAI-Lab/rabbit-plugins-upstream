# 🧬 Pancreatic Lipase Pro Docking

**Categories:** research  
**Public tags:** #research, #drug-discovery, #molecular-docking, #pancreatic-lipase, #bioinformatics

## ✨ Functionalities

Professional virtual-screening stack for human pancreatic lipase (PDB 1LPB). Multi-site molecular docking (catalytic triad, oxyanion hole, lid, etc.), molecule preparation, scoring, hit selection, and report generation.

The complete functionality, workflows, limits, examples, and operational rules
are reproduced verbatim from the current SKILL.md in **Complete Skill Reference**
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

**Artifact SHA-256 (TREE-SHA256-v1):** `37a803c53c47c5d9c792bba1081afa42db11b093f8606ae4ea6482aad2bc8ed3`

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


## 📚 Complete Skill Reference (current SKILL.md)

---
name: pancreatic-lipase-pro-docking
version: 100.4.1
author: orionshaowswmw
license: MIT
categories: [research]
topics: [drug-discovery, molecular-docking, pancreatic-lipase, virtual-screening, autodock-vina]
type: command
metadata: {"openclaw":{"emoji":"🧬"}}
description: One-command maximum-precision virtual screening against human pancreatic lipase (PDB 1LPB, lipase+colipase+Ca2+ complex) — pH 7.4 ligand protonation, tautomer + stereoisomer enumeration, 5 geometrically-validated sites, precision tiers (fast/balanced/max with multi-seed consensus), native-ligand re-dock validation gate (MUP RMSD), fail-closed everywhere.
---

# pancreatic-lipase-pro-docking 🧪🧬 v100.4.1 — PRECISION LAYER

One-command virtual screening against human pancreatic lipase (hPL / PNLIP, PDB 1LPB): molecule names or ligand CSV → chemistry-correct ligand prep → multi-site docking across **5 validated positions** → optional high-exhaustiveness re-dock → executive report. **Fail-closed**: never silent fake scores.

## First run

```bash
bash restore_and_run.sh ligands.csv   # unpacks payload_universal_upload.txt -> docking_professional_stack/ + runs classic single-site; output speed_runs/<run-id>/ in cwd
                                      # flags: --exhaustiveness 32 --n-poses 10 --quality high --cpu 8 --allow-dry (preview/CI)
                                      # v100.4: --engine multi (default) = the precision engine below
```

Full multi-site stack — run inside `docking_professional_stack/` after restore:

```bash
python3 validate_native.py                       # PROTOCOL GATE: re-dock the co-crystallized MUP inhibitor, RMSD vs crystal pose (PASS<=2A WARN<=3A); run once per receptor/protocol change
python multi_site_docking.py --check             # env self-test: python/vina/rdkit/meeko/gemmi versions, non-zero exit if REQUIRED tools missing
python multi_site_docking.py --ligands ligands.csv --precision max --workers 2   # fast=(ex4,1 seed) balanced=(ex8,1) max=(ex24,3 seeds + consensus stats)
python validate_results.py --results dock_results/results_all_sites.csv          # fail-closed output validation
bash run_tests.sh                                # 41 tests, ~5 s, no docking; path-independent
python3 build_report.py --results dock_results/results_all_sites.csv
python3 redock_high.py --results dock_results/results_all_sites.csv --top 10     # confirmatory re-dock, distinct seeds per replicate
```

## Science layer (v100.4 — what makes it precise)

- **Receptor fidelity**: 1LPB is a complex — chain B lipase + chain A colipase + Ca²⁺. `--receptor-model complex` (default) keeps ALL of it (verified: Ca²⁺ present, typed +2, in the production PDBQT); `apo` keeps the lipase chain for legacy comparability. Detergent (BOG), native inhibitor, waters always dropped.
- **5 sites, geometry-validated on the real coordinates**: catalytic triad Ser152-Asp176-His263 (center anchored on Ser-OG, Asp scored via min(OD1,OD2)···His-ND1); oxyanion hole = backbone N of **Phe77 + Leu153** (measured 5.4/3.3 Å from Ser-OG; the old "+26 residues" arithmetic was wrong); lid ≈239–259; hydrophobic pocket (hydrophobes ≤8 Å of Ser-OG); **colipase interface = real ≤5 Å cross-chain contacts** (41 residues across chains B|A).
- **Ligand chemistry (`chemprep.py`)**: pH 7.4 rule-based major microstate (carboxylates −1, thiophenolates −1, alkyl phosphonates −2, phosphate esters −1, aliphatic amines/guanidines +1 with biguanide single-cation guard, amides/phenols neutral) — 10-case tested; canonical tautomer (RDKit standardizer); undefined-stereocenter enumeration (≤2 centers, ≤4 isomers, best kept + reported); ETKDG multi-conformer + MMFF lowest-energy start, per-ligand deterministic seed; PDBQT via meeko. `--protonation as-supplied` to bypass.
- **Bias elimination**: precision tiers with **independent replicate seeds** (seed+k·7919), full Vina mode-table parsing (affinity + rmsd_lb/ub), per-(ligand,site) consensus stats (mean/sd, `unstable(sd>0.5)` flag), variant attribution (which stereoisomer/tautomer won).
- **Validation**: `validate_native.py` re-docks MUP (altloc-A, occupancy 0.67) with the canonical ligand-centered box and element-aware Kabsch RMSD — current stack: 15/15 atoms, 2.39 Å top pose (WARN band, typical for an 11-carbon flexible phosphinate). `validate_results.py` gates score envelopes, NaN/inf, coverage, stability.

## Pipeline facts

- **Tools:** `resolve_names.py` (PubChem name→SMILES, unicode-safe) · `multi_site_docking.py` (checkpointed, parallel, memory-guarded; MW ≤700 / rotb ≤20 guards) · `redock_high.py` (confirmatory ex24 + seed agreement) · `run_pipeline.sh`/`build_report.py` (report + AI multi-provider hook, no embedded credentials).
- **Reliability:** fail-closed domain exceptions (nothing silent); structured logging (every external command + stdout/stderr tails); fixed seeds + `versions.json` per run; ligand variants cached by canonical-SMILES hash (re-runs free).
- **Env:** python 3.9+ with rdkit, meeko, vina, gemmi (`micromamba create -p plenv -c conda-forge python=3.11 rdkit meeko vina gemmi openbabel pytest`). Receptor: `receptor/1LPB.pdb` next to the stack, or `--receptor PATH`. Python ≤3.11-safe. Full guide: `DEBUGGING.md`.
- **Anchors (real runs, this stack):** ibuprofen −7.39…−7.46 kcal/mol, caffeine −6.70…−6.81 (catalytic site; historical: −7.29/−6.78 — calibration preserved through the science fixes).
- **Model routing:** docking/scoring is deterministic (Vina) — zero LLM tokens. AI is optional (report narrative): route prose to a cheap model; never let an LLM produce or "fix" scores.

Built by @rustyorb — authorized research/education only; test only systems you own or are authorized to audit. Multi-model audit trail: `CHANGELOG.md` + registry versions.

