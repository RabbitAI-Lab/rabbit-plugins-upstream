# Quickstart

## 1. Put your molecules in CSV

```csv
name,smiles
compound_1,CCO
compound_2,c1ccccc1
```

## 2. Install full stack on a real Linux machine/server

```bash
cd docking_professional_stack
bash setup_full_stack.sh
micromamba activate pro-docking-full
python verify_full_stack.py
```

If you only want a lighter install:

```bash
bash setup_mamba.sh
micromamba activate pro-docking
python verify_stack.py
```

## 3. Run normal pancreatic lipase screen

```bash
python docking_speed_pipeline.py \
  --input ligands.csv \
  --target-pdb 1LPB \
  --mode dock \
  --quality standard \
  --total-cpu $(nproc) \
  --cpu-per-dock 1 \
  --gi-mode intestinal \
  --executive-dashboard
```

## 4. Open output

```text
speed_runs/<run_id>/executive_dashboard.html
speed_runs/<run_id>/final_ranked_results.csv
```

## 5. For 10,000+ molecules

```bash
bash run_10k_end_to_end.sh ligands.csv
```

This chunks the library, screens in parallel, merges results, selects diverse hits, and redocks top candidates.
