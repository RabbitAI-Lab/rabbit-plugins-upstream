# Maximum Readiness Checklist

## For 10k+ pancreatic lipase GI-fluid docking, the complete optimized workflow is now:

1. Verify tools:
   ```bash
   python verify_stack.py
   ```
2. Similarity-cluster the library:
   ```bash
   python library_chunker.py --input ligands.csv --out chunks_10k --target-chunk-size 500 --subchunk-size 100 --quality screen
   ```
3. Run subchunks in parallel:
   ```bash
   cd chunks_10k && JOBS=16 bash run_parallel_subchunks.sh
   ```
4. Merge all results:
   ```bash
   python ../merge_screen_results.py --root . --out merged_results.csv
   ```
5. Select top diverse hits, not just duplicate analogs:
   ```bash
   python ../select_top_diverse_hits.py --input merged_results.csv --out top_diverse_hits.csv --top-n 200 --per-cluster 5
   ```
6. Redock top hits at high quality:
   ```bash
   python ../docking_speed_pipeline.py --input top_diverse_hits.csv --mode dock --quality high --gi-mode strict
   ```
7. Run MD/MMGBSA only for finalists.
8. Report GI-fluid-aware predictions with confidence and limitations.

## One-command local workflow
```bash
bash run_10k_end_to_end.sh ligands.csv
```

## HPC workflow
1. Generate chunks.
2. Copy `SLURM_chunk_array_template.sh` into the chunk folder.
3. Set `#SBATCH --array=0-(N-1)` where N is number of lines in `subchunk_files.txt`.
4. Submit:
   ```bash
   sbatch SLURM_chunk_array_template.sh
   ```
5. Merge/select/redock.

## Remaining scientific limits
Even maximum computational readiness does not prove inhibition. Final confirmation still requires enzymatic assay in GI-relevant medium.
