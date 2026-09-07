# 10/10 Docking Readiness Standard

This is the operational definition of "10/10 ready" for professional docking.

## I am 10/10 ready only when all are true
1. Target and ligands are defined.
2. Required tools pass `python verify_stack.py`.
3. Receptor structure is justified and prepared.
4. Active-site grid is justified or native-ligand-derived.
5. Ligands are standardized, protonated/tautomer-aware when needed, 3D minimized, and charged.
6. Native-ligand redocking or control validation is attempted when possible.
7. Docking is checkpointed and reproducible.
8. Descriptors, Lipinski, Veber, PAINS, and ADMET-style warnings are run in parallel.
9. Poses/interactions are inspected or extracted with PLIP/ProLIF when tools are available.
10. Final answer reports score + pose/interactions + filters + confidence + limitations.

## If any item is missing
Do not claim biological proof. Label confidence lower and state what is missing.

## Pancreatic lipase default
- PDB: 1LPB
- Native ligand for grid: MUP
- Catalytic triad: Ser152, Asp176, His263
- Important nearby residues: Phe77, Tyr114, Leu153, Leu213, Phe215, Arg256, Leu264
- Default grid: MUP centroid, fallback catalytic triad centroid

## Command sequence
```bash
cd docking_professional_stack
bash setup_mamba.sh
micromamba activate pro-docking
python verify_stack.py
python docking_10x_pipeline.py --target-pdb 1LPB --input ligands.csv --mode dry
python docking_10x_pipeline.py --target-pdb 1LPB --input ligands.csv --mode dock --exhaustiveness 8 --cpu 8
```

## 24-hour workstation run
```bash
HOURS=24 EXHAUSTIVENESS=8 CPU=16 bash run_24h_screen.sh ligands.csv
```

## 24-hour SLURM/HPC run
```bash
sbatch SLURM_24h_template.sh
```

## Final reporting language
Use: predicted binder, candidate inhibitor, prioritized for experimental validation.
Avoid: proven inhibitor, definite IC50, guaranteed activity.
