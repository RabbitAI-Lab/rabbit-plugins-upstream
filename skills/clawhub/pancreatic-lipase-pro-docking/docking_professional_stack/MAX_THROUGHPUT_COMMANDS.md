# Maximum Throughput Commands

## Important
"Token/second" is an LLM text-generation metric. Docking speed should be measured as:
- ligands/hour
- CPU-hours per 1,000 ligands
- successful docked poses/hour

## Fastest quality-preserving mode
Use standard quality, maximum parallelism, quiet logs, no HTML during the run:

```bash
python docking_speed_pipeline.py \
  --input ligands.csv \
  --target-pdb 1LPB \
  --mode dock \
  --quality standard \
  --total-cpu $(nproc) \
  --cpu-per-dock 1 \
  --prefilter all_valid \
  --gi-mode intestinal \
  --quiet \
  --no-html
```

If each ligand is large/flexible, use 2 CPUs per Vina job:

```bash
python docking_speed_pipeline.py --input ligands.csv --mode dock --quality standard --total-cpu $(nproc) --cpu-per-dock 2 --quiet --no-html
```

## Two-stage throughput without quality loss
Stage 1 uses `screen` only to shortlist; final decisions are not made from this alone.

```bash
python docking_speed_pipeline.py --input ligands.csv --mode dock --quality screen --total-cpu $(nproc) --cpu-per-dock 1 --quiet --no-html
```

Then redock top hits:

```bash
python docking_speed_pipeline.py --input top_hits.csv --mode dock --quality high --total-cpu $(nproc) --cpu-per-dock 2
```

## Speed rules
1. Do not oversubscribe CPUs.
2. Keep `--cpu-per-dock 1` or `2` for large libraries.
3. Use `--quiet --no-html` for huge runs.
4. Use SSD/local disk, not network disk.
5. Reuse the same `--run-id` to resume cached ligands.
6. Do not run MD/MMGBSA on all compounds; only finalists.
