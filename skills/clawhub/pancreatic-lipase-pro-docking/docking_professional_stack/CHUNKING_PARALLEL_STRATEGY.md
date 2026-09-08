# Similarity-Based Chunking Strategy for 10,000+ Molecule Docking

## Key idea
For 10,000 similar molecules, do not feed them as one flat list. Split them into chemically meaningful and walltime-balanced groups:

```text
library
→ similarity clusters
→ balanced chunks
→ smaller subchunks
→ parallel docking jobs
→ merge/rank
```

This improves:
- parallel execution
- checkpoint/resume behavior
- balanced CPU usage
- review of congeneric series
- later high-quality redocking/FEP decisions

## Mathematical basis
1. Convert SMILES to Morgan/ECFP fingerprints.
2. Compute Tanimoto similarity.
3. Cluster with Butina clustering.
4. Estimate docking cost:

```text
cost ≈ heavy_atoms + 3 × rotatable_bonds + 0.5 × ring_count
```

5. Split clusters into chunks using greedy bin packing by estimated cost.
6. Split chunks into subchunks for job arrays or GNU parallel.

## Create chunks

```bash
cd docking_professional_stack
python library_chunker.py \
  --input ligands.csv \
  --out chunks_10k \
  --similarity-threshold 0.65 \
  --target-chunk-size 500 \
  --subchunk-size 100 \
  --target-pdb 1LPB \
  --quality standard \
  --cpu-per-dock 1
```

Outputs:

```text
chunks_10k/manifest.json
chunks_10k/all_chunked_ligands.csv
chunks_10k/chunk_00000.csv ...
chunks_10k/subchunks/chunk_00000_sub_000.csv ...
chunks_10k/run_parallel_subchunks.sh
chunks_10k/run_all_subchunks.sh
```

## Run parallel subchunks

```bash
cd chunks_10k
JOBS=8 bash run_parallel_subchunks.sh
```

Each subchunk calls:

```bash
python ../docking_speed_pipeline.py --input subchunk.csv --mode dock --quiet --no-html
```

## HPC / SLURM array idea
Use `subchunk_files.txt` as the array input list:

```bash
FILE=$(sed -n "$((SLURM_ARRAY_TASK_ID+1))p" subchunk_files.txt)
python ../docking_speed_pipeline.py --input "$FILE" --target-pdb 1LPB --mode dock --quality standard --total-cpu $SLURM_CPUS_PER_TASK --cpu-per-dock 1 --quiet --no-html
```

## Best 10k workflow

### Stage 1: Chunk and screen
```bash
python library_chunker.py --input ligands.csv --out chunks_10k --target-chunk-size 500 --subchunk-size 100 --quality screen
cd chunks_10k && JOBS=16 bash run_parallel_subchunks.sh
```

### Stage 2: Merge results, select top molecules per cluster
Do not take only global top scores. Keep cluster diversity.

### Stage 3: High-quality redocking
Redock top 1–5% or top N per cluster:

```bash
python docking_speed_pipeline.py --input top_diverse_hits.csv --mode dock --quality high --cpu-per-dock 2 --gi-mode strict
```

### Stage 4: MD/MMGBSA/FEP only for finalists
Run expensive simulation only on chemically diverse top candidates.
