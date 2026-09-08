# Common Docking/Simulation Pipeline Bug Hotspots and Applied Fixes

This checklist is based on recurring failure patterns in cheminformatics, docking, MD, and HPC workflows.

## Hotspots
1. **File/path bugs**: relative paths fail after `cd`, generated scripts assume one launch directory.
2. **Shell quoting bugs**: GNU parallel, `$JOBS`, `$stem`, and `{}` expansion are easy to quote incorrectly.
3. **CPU oversubscription**: `JOBS × CPUs per job` silently exceeds available cores and makes runs slower.
4. **Tiny chunk explosion**: clustering diverse libraries can produce thousands of singleton jobs.
5. **Duplicate ligand names**: output folders/checkpoints collide.
6. **Invalid/ambiguous SMILES**: bad inputs waste docking jobs or crash ligand preparation.
7. **Non-atomic result writes**: interrupted jobs can leave corrupted CSVs.
8. **Missing executables**: scripts fail late instead of warning early.
9. **Version differences**: Vina/OpenBabel/Meeko flags and outputs vary.
10. **Overclaiming**: a good score is treated as biological proof.

## Fixes added
- Runner scripts now `cd` to their own directory.
- Chunk paths are relative to the chunk directory.
- Generated scripts use absolute path to the pipeline script.
- GNU parallel scripts validate that `parallel` exists.
- Chunk defaults avoid CPU oversubscription.
- Small similarity clusters are packed together instead of producing thousands of tiny jobs.
- Duplicate ligand names are automatically made unique.
- Checkpoint writing frequency is configurable.
- Merge script searches nested result layouts.
- `workflow_linter.py` checks inputs, tools, chunks, and shell syntax before long runs.

## Rule
Before any large run:
```bash
python workflow_linter.py --ligands ligands.csv --check-tools
python library_chunker.py --input ligands.csv --out chunks_10k
python workflow_linter.py --chunks chunks_10k
```
