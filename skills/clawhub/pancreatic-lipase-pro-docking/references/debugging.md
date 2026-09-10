# Debugging

Work top-down. Do not skip the preflight — most "docking is broken" reports are
environment problems that `--check` names in one line.

## 1. Preflight

```bash
python docking_professional_stack/multi_site_docking.py --check
```

Prints every dependency with a version and a `✓`, then `RESULT: OK` or
`RESULT: FAIL` (non-zero exit). A healthy box looks like:

```
python 3.11.16 · vina .../bin/vina ✓ · rdkit 2026.03.1 ✓ · meeko 0.8.0 ✓ · gemmi 0.7.5 ✓
receptor .../receptor/1LPB.pdb (exists)
RESULT: OK
```

Whatever lacks a `✓` is the problem. Nothing below matters until this passes.

## 2. Test suite

```bash
bash docking_professional_stack/run_tests.sh          # 41 tests, ~5 s, no docking
```

- **41 passed** — stack logic is sound.
- **29 passed, 12 skipped** — RDKit is absent. Chemistry tests skip by design;
  fine for CLI work, but you cannot dock until you install RDKit.
- **Any failure** — a real regression. Read the assertion; do not proceed.

## 3. Common failures

| Message / symptom | Cause | Fix |
|---|---|---|
| `vina: command not found` | binary not on PATH | `export PATH="$PWD/plenv/bin:$PATH"` |
| `ModuleNotFoundError: rdkit` | wrong interpreter | call `plenv/bin/python` explicitly, not `python3` |
| meeko/vina install resolves forever | Python 3.12+ | recreate with `python=3.11`; the stack is ≤3.11-safe |
| `receptor/1LPB.pdb not found` | run from the wrong cwd | run inside the stack dir, or pass `--receptor /abs/path/1LPB.pdb` |
| All scores identical / suspiciously round | ligand prep silently produced one variant | check `dock_results/ligprep/` for PDBQTs; re-run with `--protonation as-supplied` to isolate |
| `unstable(sd>0.5)` on many rows | exhaustiveness too low for flexible ligands | raise to `--precision max`; do not rank unstable rows |
| Scores drift vs the anchors | toolchain changed | `python scripts/selfcheck.py run` and read the `env` block |
| Empty `results_all_sites.csv` | every job failed | read the log: each Vina invocation is echoed with its stderr tail |
| OOM / killed | too many workers | `--workers` ≤ physical cores; each Vina process wants ~1 GB |
| Kernel/cloud problems | — | `references/kaggle.md` §5 |

## 4. Reproducing a single job

Every Vina call is logged verbatim (`RUN: vina --receptor ... --seed 42 ...`).
Copy that line and run it directly — this separates a stack bug from a Vina bug.
Runs are seeded (`seed + k·7919`), so a repeated command reproduces its score
exactly. If it does not, the receptor or ligand PDBQT changed underneath you.

## 5. Checkpoint / resume

`multi_site_docking.py` checkpoints per `(name, site, variant, seed)`. Re-running
the same command skips finished work (`resume: N done | pending: M`). To force a
clean run, delete `--outdir` — do not hand-edit the checkpoint.

## 6. When results look wrong rather than broken

Ask, in order:

1. Did `validate_native.py` pass? If the co-crystal ligand does not re-dock, the
   protocol is wrong and every score is suspect.
2. Do the anchors hold (ibuprofen −7.3…−7.5, caffeine −6.6…−6.8)? If not, the
   box or receptor changed.
3. Is the difference you are reporting larger than ~0.5 kcal/mol? If not, it is
   within Vina's noise and is not a result.
4. Is the ligand in the applicability domain? MW ≤700, rotatable bonds ≤20.
   Vina degrades badly past that and the stack guards on it.

If all four pass and the number still looks odd, report it with its `score_sd`
and say it is unexplained. Do not adjust it.
