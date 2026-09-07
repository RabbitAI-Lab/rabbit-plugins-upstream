# Workflows

## A. Rank a handful of named compounds

```bash
printf 'orlistat\ncetilistat\nibuprofen\n' > names.txt
python docking_professional_stack/resolve_names.py names.txt ligands.csv missing.csv
cat missing.csv            # ALWAYS check: unresolved names vanish silently
python docking_professional_stack/multi_site_docking.py \
  --ligands ligands.csv --precision balanced --workers 4 --outdir dock_results
python docking_professional_stack/validate_results.py --results dock_results/results_all_sites.csv
```

Report the `catalytic_triad` rows unless the user asked about another site.
Quote `score` with `score_sd`, and state that differences under ~0.5 kcal/mol
are not separable.

## B. Screen then confirm (the two-stage pattern)

Cheap pass over everything, expensive pass over survivors:

```bash
# stage 1 — triage
python docking_professional_stack/multi_site_docking.py \
  --ligands library.csv --precision fast --workers 4 --outdir stage1

# stage 2 — confirm the top 10 with 3 independent seeds
python docking_professional_stack/redock_high.py \
  --results stage1/results_all_sites.csv --ligands library.csv \
  --top 10 --exhaustiveness 24 --n-seeds 3 --outdir stage2
```

Only stage-2 numbers are quotable as a ranking. Stage 1 is a filter; treat its
ordering as provisional.

## C. Full protocol for something you intend to publish

```bash
python docking_professional_stack/multi_site_docking.py --check          # 1 env
bash docking_professional_stack/run_tests.sh                             # 2 logic
python docking_professional_stack/validate_native.py                     # 3 protocol
python scripts/selfcheck.py run --python plenv/bin/python                # 4 drift
python docking_professional_stack/multi_site_docking.py \
  --ligands ligands.csv --precision max --workers 4 --outdir dock_results # 5 dock
python docking_professional_stack/validate_results.py \
  --results dock_results/results_all_sites.csv                           # 6 gate
python docking_professional_stack/build_report.py \
  --results dock_results/results_all_sites.csv -o REPORT.md              # 7 report
```

Steps 1-4 are the "before" checks, 6 is the "after" gate. Skipping them makes
the output unciteable. Ship `versions.json` alongside any reported number.

## D. Large libraries

>200 ligands: use Kaggle (`references/kaggle.md`) or split locally.

```bash
split -l 500 --numeric-suffixes=1 --additional-suffix=.csv library_body.csv batch
for f in batch*.csv; do
  sed -i '1i name,smiles' "$f"
  python docking_professional_stack/multi_site_docking.py \
    --ligands "$f" --precision fast --workers 4 --outdir "out_${f%.csv}"
done
```

Runs are checkpointed per `(name, site, variant, seed)`, so an interrupted batch
resumes on re-invocation rather than re-docking.

## E. Writing up results

Include, every time:

- the precision tier and `--seed`,
- `score` **and** `score_sd` (or the replicate count if sd is 0),
- the `validate_native.py` RMSD for the protocol,
- the anchor check (ibuprofen / caffeine) if the reader needs calibration,
- `versions.json`.

State plainly: Vina scores are a coarse filter; rank order within a congeneric
series is meaningful, absolute affinities are not; docking does not model the
covalent chemistry that a Ser152 nucleophile invites. A result the tools did not
produce does not go in the write-up.
