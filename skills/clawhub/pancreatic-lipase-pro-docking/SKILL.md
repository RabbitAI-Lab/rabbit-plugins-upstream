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
