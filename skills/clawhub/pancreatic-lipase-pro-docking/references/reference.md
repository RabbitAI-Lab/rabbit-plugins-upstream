# CLI and data reference

Every flag below is read from the tools' own argument parsers. If a flag is not
here, it does not exist — do not invent one.

## multi_site_docking.py — the docking engine

```
--ligands PATH          CSV: name,smiles (required unless --check)
--receptor PATH         default: receptor/1LPB.pdb next to the stack
--receptor-model        complex | apo          (default complex = lipase+colipase+Ca2+)
--precision             fast | balanced | max  (default balanced)
--exhaustiveness N      override the tier
--n-seeds K             override the tier
--n-poses N             poses per run
--seed N                base seed (default 42); replicate seeds = seed + k*7919
--workers N             parallel Vina processes (default 1)
--cpu-per-dock N        threads per Vina process (default 1)
--max-mw F              applicability guard, default 700
--max-rotb N            applicability guard, default 20
--protonation           rules | as-supplied    (default rules = pH 7.4 microstate)
--outdir PATH           default dock_results
--limit N               dock only the first N ligands
--sites-file PATH       override site definitions
--check                 env self-test, then exit
--debug / --log-file    verbose logging
```

Tiers: `fast` = ex4 / 1 seed / 9 poses · `balanced` = ex8 / 1 / 9 ·
`max` = ex24 / 3 seeds / 20 poses + consensus statistics.

## Other tools

```
validate_results.py --results CSV [--runs-dir DIR] [--sites 5]
                    [--max-score -2.0] [--min-score -15.0]
    Fail-closed output gate. Non-zero exit = do not report these numbers.

validate_native.py
    Re-docks the co-crystallized MUP inhibitor and reports RMSD vs the crystal
    pose. PASS <=2 A, WARN <=3 A. Run once per receptor or protocol change.

redock_high.py --results CSV [--ligands CSV] [--top 10] [--exhaustiveness 24]
               [--n-seeds 3] [--n-poses 10] [--workers 2] [--outdir DIR]
    Confirmatory re-dock of the top hits with independent seeds.

build_report.py --results CSV [--results-ex16 CSV] [--top 20] [-o REPORT.md]
    Markdown report from result CSVs.

resolve_names.py NAMES_FILE OUT_CSV [MISSING_CSV]
    PubChem name -> SMILES. Always inspect MISSING_CSV; unresolved names are
    silently absent from the screen otherwise.

run_tests.sh
    41 tests, ~5 s, no docking required.
```

## scripts/kaggle_dock.py

```
check | push | status | fetch | run
--username / --key            explicit credentials
--creds FILE --account N      JSON pool with providers.kaggle
--stack DIR                   default docking_professional_stack
--ligands CSV                 default ligands.csv
--slug / --title              slug is derived from title (Kaggle's rule)
--precision / --workers       forwarded to the docking engine
--extra "..."                 extra flags for multi_site_docking.py
--gpu                         not recommended: Vina is CPU-only
--public                      default is a private kernel
--out DIR                     download target (default kaggle_out)
--timeout S / --poll S        run-command polling (default 3600 / 30)

exit: 0 ok · 2 usage · 3 auth · 4 kernel error · 5 timeout · 6 quota
```

## scripts/selfcheck.py

```
run       dock the reference set, compare with baseline   exit 1 = DRIFT
baseline  overwrite the baseline with current numbers
history   list recorded runs
show      print the active baseline
--python PATH        interpreter owning rdkit/meeko/vina
--tolerance F        kcal/mol, default 0.5 (Vina's reproducibility band)
--precision          fast | balanced | max (default fast)
```

## Output schemas

`dock_results/results_all_sites.csv` — one row per (ligand, site):

| column | meaning |
|---|---|
| `name` | ligand name as supplied |
| `site` | one of the 5 site keys |
| `status` | `ok` or a failure token |
| `score` | best affinity, kcal/mol (more negative = better) |
| `time_s` | wall seconds summed over that ligand/site's replicates |
| `best_variant` | which tautomer/stereoisomer won (`v0`, `v1`, …) |
| `n_replicates` | number of seed replicates aggregated |
| `score_mean` | mean across replicates |
| `score_sd` | sd across replicates |
| `stability` | `stable` or `unstable(sd>0.5)` — never rank on unstable rows |

`dock_results/runs_detail.csv` — one row per (name, site, variant, seed) with
`score`, `rmsd_lb`, `rmsd_ub`, `n_modes`, `time_s`.

`dock_results/versions.json` — tool versions and seeds for the run. Include this
when reporting results; it is what makes a number reproducible.

`calibration/baseline.json` + `calibration/history.jsonl` — drift memory written
by `selfcheck.py`.

## Ligand input

CSV with a header. `name` and `smiles` are required; extra columns are carried
through and ignored.

```csv
name,smiles
ibuprofen,CC(C)Cc1ccc(cc1)C(C)C(=O)O
orlistat,CCCCCCCCCCCC(CC1C(=O)OC1CCCCCC)OC(=O)C(CC(C)C)NC=O
```

Names with unicode or commas must be quoted. Use `resolve_names.py` when you
have names but no structures — never hand-write a SMILES from memory.
