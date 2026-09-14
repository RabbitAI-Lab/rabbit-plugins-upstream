# Speed and Capacity Guide — Professional Docking Without Losing Quality

## Main idea
Do **not** lower quality blindly. Increase throughput by:

1. Parallelizing independent ligands.
2. Avoiding CPU oversubscription.
3. Caching receptor/ligand preparation.
4. Checkpointing every ligand.
5. Running descriptors/PAINS in parallel.
6. Using quality presets strategically.
7. Using stricter prefilters only for very large libraries.

## New optimized runner

```bash
python docking_speed_pipeline.py --input ligands.csv --target-pdb 1LPB --mode dock --quality standard --total-cpu 16 --cpu-per-dock 2
```

Outputs:

```text
speed_runs/<run_id>/descriptors.csv
speed_runs/<run_id>/partial_results.csv
speed_runs/<run_id>/final_ranked_results.csv
speed_runs/<run_id>/report.html
speed_runs/<run_id>/metadata.json
```

## Quality presets

| Preset | Exhaustiveness | Use case |
|---|---:|---|
| screen | 4 | first pass for thousands of ligands |
| standard | 8 | balanced professional default |
| high | 16 | finalists or smaller libraries |
| ultra | 32 | very small finalist set |

Override manually:

```bash
python docking_speed_pipeline.py --input ligands.csv --mode dock --exhaustiveness 12 --total-cpu 16 --cpu-per-dock 2
```

## CPU strategy

If machine has 16 CPUs:

```bash
# 8 Vina jobs x 2 CPUs each = 16 CPUs total
python docking_speed_pipeline.py --input ligands.csv --mode dock --total-cpu 16 --cpu-per-dock 2
```

If machine has 32 CPUs:

```bash
# 8 Vina jobs x 4 CPUs each = 32 CPUs total, better per-ligand sampling speed
python docking_speed_pipeline.py --input ligands.csv --mode dock --quality high --total-cpu 32 --cpu-per-dock 4
```

Avoid this:

```bash
# bad: too many jobs each using too many CPUs; causes oversubscription
--workers 32 --cpu-per-dock 8
```

## Prefilter policy

Default:

```bash
--prefilter all_valid
```

This only skips invalid SMILES and keeps unusual molecules, preserving quality.

For massive screens:

```bash
--prefilter druglike
```

For very aggressive triage:

```bash
--prefilter strict
```

Warning: strict filtering can remove real natural-product or covalent-like hits.

## Recommended two-stage professional workflow

### Stage 1: capacity screen

```bash
python docking_speed_pipeline.py \
  --input ligands.csv \
  --target-pdb 1LPB \
  --mode dock \
  --quality screen \
  --total-cpu 32 \
  --cpu-per-dock 2 \
  --prefilter all_valid
```

### Stage 2: high-quality redocking of top hits

Create a CSV of top 50–200 compounds, then:

```bash
python docking_speed_pipeline.py \
  --input top_hits.csv \
  --target-pdb 1LPB \
  --mode dock \
  --quality high \
  --total-cpu 32 \
  --cpu-per-dock 4 \
  --prefilter none
```

### Stage 3: finalists
Use MD/MMGBSA/FEP only for the best few compounds.

## Smoothness features added
- Per-ligand `done.json` checkpoints.
- `partial_results.csv` updated continuously.
- Resume by rerunning same `--run-id`.
- Separate output directories per run.
- Parallel descriptors and PAINS.
- Parallel docking with controlled CPU-per-dock.
- HTML report generation.
