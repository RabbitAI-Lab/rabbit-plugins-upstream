# Arena Agent Instructions — Self-Contained Docking Program

You are inside Arena.ai Agent Mode and this folder contains a complete professional molecular-docking workflow. If the user uploads molecules, use these instructions without asking for external setup unless a required executable is missing.

## Primary use case
Professional virtual screening for **pancreatic lipase inhibition**, optimized for gastrointestinal-tract-fluid relevance.

Default target:
- Human pancreatic lipase
- PDB: `1LPB`
- Active-site grid: native ligand `MUP` centroid when available
- Fallback grid: catalytic triad centroid
- Catalytic triad: Ser152, Asp176, His263
- GI mode: intestinal

## Expected input molecules
Preferred file: CSV with columns:

```csv
name,smiles
compound_1,CCO
compound_2,c1ccccc1
```

Accepted SMILES column names:
- `smiles`
- `SMILES`
- `canonical_smiles`

If duplicate names exist, the pipeline auto-renames them internally.

## First step every time
Run the linter:

```bash
cd docking_professional_stack
python workflow_linter.py --ligands /path/to/ligands.csv --check-tools
```

If `vina` or `obabel` are missing, do not claim real docking was performed. Run dry mode or tell the user which tool is missing.

## Fast professional run
Use this for a normal uploaded file:

```bash
python docking_speed_pipeline.py \
  --input /path/to/ligands.csv \
  --target-pdb 1LPB \
  --mode dock \
  --quality standard \
  --total-cpu $(nproc 2>/dev/null || echo 4) \
  --cpu-per-dock 1 \
  --gi-mode intestinal \
  --executive-dashboard
```

If docking tools are unavailable, use dry mode:

```bash
python docking_speed_pipeline.py \
  --input /path/to/ligands.csv \
  --target-pdb 1LPB \
  --mode dry \
  --gi-mode intestinal \
  --executive-dashboard
```

## Large library, e.g. 10,000 molecules
Use chunking:

```bash
python library_chunker.py \
  --input /path/to/ligands.csv \
  --out chunks_10k \
  --target-pdb 1LPB \
  --quality screen \
  --target-chunk-size 500 \
  --subchunk-size 100 \
  --total-cpu 1 \
  --cpu-per-dock 1 \
  --gi-mode intestinal

python workflow_linter.py --chunks chunks_10k
cd chunks_10k
JOBS=8 bash run_parallel_subchunks.sh || bash run_all_subchunks.sh
cd ..
python merge_screen_results.py --root chunks_10k --out chunks_10k/merged_results.csv
python select_top_diverse_hits.py --input chunks_10k/merged_results.csv --out chunks_10k/top_diverse_hits.csv --top-n 200 --per-cluster 5
python docking_speed_pipeline.py --input chunks_10k/top_diverse_hits.csv --target-pdb 1LPB --mode dock --quality high --cpu-per-dock 2 --gi-mode strict --executive-dashboard --run-id redock_top_diverse_hits
```

## Output files to present to user
For standard runs, present:

```text
speed_runs/<run_id>/executive_dashboard.html
speed_runs/<run_id>/final_ranked_results.csv
speed_runs/<run_id>/metadata.json
```

For large chunked runs, present:

```text
chunks_10k/merged_results.csv
chunks_10k/top_diverse_hits.csv
speed_runs/redock_top_diverse_hits/executive_dashboard.html
```

## Scientific language rules
Say:
- predicted binder
- candidate inhibitor
- prioritized for experimental validation
- docking suggests

Do NOT say:
- proven inhibitor
- guaranteed activity
- exact IC50 unless experimentally measured

## Confidence rules
High confidence requires:
- successful tool verification
- actual docking completed
- plausible active-site pose/score
- acceptable GI-fluid flags
- preferably redocking/control validation

If tools are missing or only dry mode was run, confidence is low.


## Zero-instruction Arena autorun
If this package is restored in Arena.ai and the user provides a ligand CSV, the first command to try is now:

```bash
cd docking_professional_stack
python arena_auto_run.py --input /path/to/ligands.csv
```

This script automatically attempts to install the minimal Python docking stack (`rdkit`, `meeko`, `vina`, `gemmi`) into the Arena user environment. It then runs real docking if possible. By default it **refuses dry-mode output** if real docking dependencies remain unavailable. Use `--allow-dry` only for a non-docking preview.

Alternative wrapper:

```bash
bash run_uploaded_molecules.sh /path/to/ligands.csv
```

For preview-only mode when Arena cannot install docking dependencies:

```bash
ALLOW_DRY=1 bash run_uploaded_molecules.sh /path/to/ligands.csv
```

## v100.2.0 — multi-site docking + report pipeline
1. Provide either molecule NAMES (txt) or a ligands CSV (name,smiles).
2. Names: `python3 resolve_names.py names.txt molecules_resolved.csv`
3. Dock all 5 sites: `python3 multi_site_docking.py --ligands molecules_resolved.csv --workers 2`
4. Re-dock top hits at high resolution: `python3 redock_high.py --results dock_results/results_all_sites.csv --top 10`
5. Report: `python3 build_report.py --results dock_results/results_all_sites.csv --results-ex16 dock_results_ex16/results_ex16.csv`
6. Or end-to-end: `bash run_pipeline.sh molecules.txt`
- Receptor: receptor/1LPB.pdb next to the stack (or --receptor PATH). Sites are auto-detected.
- Memory guards (--max-mw 700, --max-rotb 20) prevent OOM on small boxes.

## v100.3.0 — debugging best practices
- Before debugging a job: `python multi_site_docking.py --check` (env self-test).
- Use `--debug --log-file run.log` for full structured logs (commands + tails on failure).
- After a run: `python validate_results.py --results dock_results/results_all_sites.csv` (fail-closed gate).
- Run tests after any change: `bash run_tests.sh`.
- Never fix by guessing: reproduce from versions.json + logged command line.
