---
name: pancreatic-lipase-pro-docking
version: 101.0.5
author: orionshaowswmw
license: MIT
categories: [research]
topics: [drug-discovery, molecular-docking, pancreatic-lipase, virtual-screening, kaggle]
type: command
metadata: {"openclaw":{"emoji":"🧬"}}
description: Docks small molecules against human pancreatic lipase (PDB 1LPB, lipase+colipase+Ca2+) across 5 validated sites with AutoDock Vina — pH 7.4 protonation, tautomer/stereoisomer enumeration, multi-seed consensus, native re-dock RMSD gate, and calibration drift detection. Runs locally or on free Kaggle CPU kernels. Use when the user asks to dock, screen, or rank compounds against pancreatic lipase, PNLIP, hPL, or for anti-obesity/lipase-inhibitor virtual screening.
---

# pancreatic-lipase-pro-docking

Deterministic Vina screening against human pancreatic lipase. **Scores come from Vina, never from a language model.**

## Rule 0 — do not invent numbers

Report only scores that appear in a generated CSV. If a tool did not run, say so.
No estimated affinities, no remembered values, no "typical" numbers. Every claim
traces to `dock_results/results_all_sites.csv` or it is not made.

If `vina` is missing, the run fails loudly — that is intended. Do not substitute
a guess and do not describe a dry run as if it were docking.

## Decide the route first

Run `command -v vina micromamba conda` first, then:

| Situation | Route |
|---|---|
| `vina` present, or `micromamba`/`conda` available to build the env | **Local** (below) — build the env, do not skip to Kaggle |
| No local toolchain **and** no conda/micromamba, or >200 ligands | **Kaggle** → `references/kaggle.md` |
| Something is broken | `references/debugging.md` |

## Local run

```bash
# 0. env (once). Python must be <=3.11.
micromamba create -p plenv -c conda-forge python=3.11 rdkit meeko vina gemmi openbabel pytest
export PATH="$PWD/plenv/bin:$PATH"

# 1. preflight — MUST print RESULT: OK before docking
python docking_professional_stack/multi_site_docking.py --check

# 2. dock (ligands.csv needs columns: name,smiles)
python docking_professional_stack/multi_site_docking.py \
  --ligands ligands.csv --precision balanced --workers 4 --outdir dock_results

# 3. gate the output — non-zero exit means do not report the numbers
python docking_professional_stack/validate_results.py \
  --results dock_results/results_all_sites.csv
```

Tiers: `fast` = ex4/1 seed (triage) · `balanced` = ex8/1 (default) · `max` =
ex24/3 seeds + consensus (publication).

Read `dock_results/results_all_sites.csv` — one row per (ligand, site): `score`
is the best affinity in kcal/mol (more negative = better); treat
`unstable(sd>0.5)` rows as unranked.

## The 5 sites

`catalytic_triad` (Ser152-Asp176-His263) · `oxyanion_hole` (backbone N of Phe77+Leu153)
· `lid` (~239-259) · `hydrophobic_pocket` (hydrophobes ≤8 Å of Ser152-OG) ·
`colipase_interface` (41 cross-chain contacts ≤5 Å).

Centres are computed from the real coordinates at run time. Quote
`catalytic_triad` for inhibitor ranking unless asked otherwise.

## Trust the numbers before reporting them

```bash
# protocol gate: re-dock the co-crystallized MUP inhibitor (run once per receptor change)
python docking_professional_stack/validate_native.py        # PASS <=2 A, WARN <=3 A

# drift gate: docks ibuprofen+caffeine and compares against calibration/baseline.json
python scripts/selfcheck.py run --python plenv/bin/python   # exit 0 = calibrated, exit 1 = DRIFT
```

`validate_native.py`: RMSD ≤2 Å PASS · ≤3 Å WARN (proceed, disclose it) ·
**>3 Å FAIL — stop, do not dock, do not report scores.** The protocol is wrong.

`selfcheck.py run` performs the anchor check for you; you do not dock the
controls by hand. **Exit 1 means do not publish** until the drift is explained.
Its stored anchors at the catalytic site: **ibuprofen −7.3 to −7.5**,
**caffeine −6.6 to −6.8** kcal/mol.

Vina's own reproducibility band is ~0.5 kcal/mol. Differences smaller than that
between two ligands are **not** a ranking. Say so instead of ranking noise.

## Interpreting honestly

- Coarse filter, not binding free energies: rank order within a congeneric
  series is meaningful, absolute numbers are not. No score proves inhibition.
- Ser152 is a nucleophilic serine — covalent/mechanism-based inhibitors (e.g.
  orlistat's real mechanism) are **not** modelled by Vina. Say so.

## What this skill does to the machine

Declared up front so nothing below is a surprise.

| Capability | When | Scope |
|---|---|---|
| **Extract archive** | `restore_and_run.sh` | unpacks the bundled stack into `docking_professional_stack/` beside the skill. Inspect it first: `unzip -l` the payload block, or read the extracted `.py` files. |
| **Install packages** | only the `micromamba create` line you run yourself | into the `plenv/` prefix in your cwd (~2 GB, persists until you delete it). conda-forge packages, **not** hash-pinned. No `sudo`, no shell-profile edits. |
| **Optional installers (opt-in)** | only if you run them | `setup_mamba.sh` downloads micromamba into `$HOME/micromamba` when no conda is present. `arena_auto_run.py` can `pip install --user --upgrade` 8 packages into your **account-wide** site-packages — this is **disabled by default** and requires `HPL_ALLOW_PIP_BOOTSTRAP=1`. Prefer the `plenv/` route above; neither is needed. |
| **Write files** | docking | `--outdir` (default `dock_results/`), `calibration/`, and `selfcheck_work/`. Nothing outside the working directory. |
| **Execute binaries** | docking | `vina`, and `obabel`/`meeko` for ligand prep. No other subprocesses. |
| **Network — PubChem** | only `resolve_names.py` | sends the compound *names* you pass it. Skip it and supply SMILES to stay fully offline. |
| **Network — Kaggle** | only `scripts/kaggle_dock.py` | **uploads your ligand CSV and the stack to a Kaggle kernel** under your account, and the kernel downloads micromamba + conda-forge packages at run time. Kernels are private by default (`--public` opts out). `--extra` is allow-listed and the kernel runs the docking command without a shell. Do not use this route for confidential structures. |
| **Network — none else** | — | docking, scoring, prep and validation are fully local and involve **no LLM calls**. |

Not used: no sudo, no system package manager, no writes outside the working
directory, no credentials read except the Kaggle token you point at, no
telemetry.

## Everything else

| Need | File |
|---|---|
| Kaggle: run in the cloud, API keys, debugging kernels | `references/kaggle.md` |
| Failures, error messages, environment problems | `references/debugging.md` |
| Full CLI surface, every flag, output schemas | `references/reference.md` |
| Report generation, name→SMILES, large screens | `references/workflows.md` |

Authorized research and education only.
