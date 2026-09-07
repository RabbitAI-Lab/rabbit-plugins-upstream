# pancreatic-lipase-pro-docking v101.0.0

Deterministic AutoDock Vina screening against human pancreatic lipase
(PDB **1LPB** — lipase + colipase + Ca²⁺) across **5 geometrically validated
sites**, with chemistry-correct ligand preparation, a native re-dock protocol
gate, calibration drift detection, and one-command execution on free Kaggle
CPU kernels.

**Scores come from Vina. Never from a language model.**

## Install

```bash
openclaw skills install @orionshaowswmw/pancreatic-lipase-pro-docking
```

## Quick start

```bash
# unpack the stack (once)
bash restore_and_run.sh

# environment (once) — Python must be <=3.11
micromamba create -p plenv -c conda-forge python=3.11 rdkit meeko vina gemmi openbabel pytest
export PATH="$PWD/plenv/bin:$PATH"

# preflight, dock, gate
python docking_professional_stack/multi_site_docking.py --check
python docking_professional_stack/multi_site_docking.py \
  --ligands ligands.csv --precision balanced --workers 4 --outdir dock_results
python docking_professional_stack/validate_results.py \
  --results dock_results/results_all_sites.csv
```

`ligands.csv` needs a header with `name,smiles`.

## Run it on Kaggle instead

Free 4 vCPU / ~30 GB RAM kernels, 12 h ceiling, no weekly quota on CPU:

```bash
python scripts/kaggle_dock.py check
python scripts/kaggle_dock.py run --ligands ligands.csv --title "hPL screen batch 1"
```

Push, poll and fetch in one command; results come back in the same CSV schema as
a local run. Full guide including credential setup and kernel debugging:
`references/kaggle.md`.

## What makes the numbers trustworthy

| Gate | Command | Meaning |
|---|---|---|
| Environment | `multi_site_docking.py --check` | every tool present and versioned |
| Logic | `bash run_tests.sh` | 60 tests, ~4 s, no docking needed |
| Protocol | `validate_native.py` | re-docks the co-crystal MUP inhibitor; ≤2 Å PASS, >3 Å FAIL |
| Drift | `scripts/selfcheck.py run` | reference scores vs stored baseline; exit 1 = do not publish |
| Output | `validate_results.py` | score envelopes, NaN/coverage/stability |

Calibration anchors (catalytic site, real runs): ibuprofen **−7.3 to −7.5**,
caffeine **−6.6 to −6.8** kcal/mol.

## The five sites

`catalytic_triad` (Ser152-Asp176-His263) · `oxyanion_hole` (backbone N of
Phe77 + Leu153) · `lid` (~239-259) · `hydrophobic_pocket` (hydrophobes ≤8 Å of
Ser152-OG) · `colipase_interface` (41 cross-chain contacts ≤5 Å).

Site centres are computed from the actual receptor coordinates at run time.

## Science layer

- **pH 7.4 microstates** — carboxylates −1, aliphatic amines/guanidines +1,
  phenols/amides neutral (rule-based, 10-case tested).
- **Canonical tautomer** + **undefined-stereocenter enumeration** (≤2 centres,
  ≤4 isomers); the winning variant is reported per row.
- **ETKDGv3 + MMFF** lowest-energy start conformer; meeko PDBQT output.
- **Bias control** — independent replicate seeds (`seed + k·7919`), consensus
  mean/sd, and an `unstable(sd>0.5)` flag. Never rank on unstable rows.
- **Applicability guards** — MW ≤700, rotatable bonds ≤20.

## Honest limitations

- Vina scores are a coarse filter, not binding free energies. Rank order within
  a congeneric series is meaningful; absolute values are not.
- Differences under ~0.5 kcal/mol are within Vina's reproducibility band and do
  not constitute a ranking.
- Ser152 is a nucleophilic serine; **covalent and mechanism-based inhibitors are
  not modelled**. Orlistat's real mechanism is covalent acylation — a Vina score
  for it describes non-covalent recognition only.
- Docking generates hypotheses. It does not demonstrate inhibition.

## Layout

```
SKILL.md                     agent entry point (routes to the rest)
references/kaggle.md         cloud execution + kernel debugging
references/debugging.md      failure triage
references/reference.md      complete CLI + output schemas
references/workflows.md      end-to-end recipes
scripts/kaggle_dock.py       Kaggle runner (check|push|status|fetch|run)
scripts/selfcheck.py         calibration + drift detection
calibration/                 baseline.json + history.jsonl
docking_professional_stack/  the engine, receptor, and 60-test suite
```

## What changed in v101

Seven verified bug fixes (including a Kaggle status enum that made every cloud
run appear to hang, and an empty `time_s` column), the Kaggle execution layer,
the drift-detection layer, 19 new regression tests, and a progressive-disclosure
rewrite that made SKILL.md smaller while covering more. See `CHANGELOG.md`.

MIT. Authorized research and education only.
