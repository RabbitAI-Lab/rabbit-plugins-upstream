# Professional Docking Stack

This folder contains install and runner files for a serious docking workstation/cloud VM.

## Important limitation
The Arena workspace is not a persistent HPC server. I cannot keep a 24-hour job running here reliably. Use these scripts on your own Linux machine, cloud VM, or HPC node.

## Install
Recommended:

```bash
cd docking_professional_stack
bash setup_mamba.sh
micromamba activate pro-docking   # or mamba/conda activate pro-docking
python verify_stack.py
```

## Input file
CSV with:

```csv
name,smiles
compound_1,CCO
compound_2,c1ccccc1
```

## 24-hour run

```bash
cd docking_professional_stack
HOURS=24 EXHAUSTIVENESS=8 CPU=8 bash run_24h_screen.sh ligands.csv
```

Outputs:

```text
logs/<run_id>/live.log
pro_runs/<run_id>/descriptors.csv
pro_runs/<run_id>/final_ranked_results.csv
```

## Stack included
- RDKit: ligand standardization/descriptors
- Open Babel: format conversion/3D generation
- Meeko: PDBQT preparation
- AutoDock Vina: docking
- OpenMM/PDBFixer/AmberTools: MD and preparation foundation
- MDAnalysis/MDTraj/ProLIF/PLIP: trajectory/contact analysis
- PubChem/ChEMBL clients: public chemical data

## Professional layers still requiring extension per project
- native-ligand redocking RMSD
- PLIP/ProLIF contact extraction into the final table
- receptor ensemble docking
- OpenMM production MD
- MM/GBSA rescoring
- FEP/RBFE for congeneric lead optimization


## 10x upgraded runner

Use the more complete checkpointed runner:

```bash
python docking_10x_pipeline.py --target-pdb 1LPB --input ligands.csv --mode dry
python docking_10x_pipeline.py --target-pdb 1LPB --input ligands.csv --mode dock --exhaustiveness 8 --cpu 8
```

It produces:

```text
10x_runs/<run_id>/metadata.json
10x_runs/<run_id>/final_ranked_results.csv
10x_runs/<run_id>/report.html
```

For HPC clusters, adapt:

```bash
sbatch SLURM_24h_template.sh
```

## Full upgraded library stack

For maximum readiness, use the full environment instead of the lighter one:

```bash
cd docking_professional_stack
bash setup_full_stack.sh
micromamba activate pro-docking-full
python verify_full_stack.py
```

Main files:

```text
environment_full.yml
requirements_full_pip.txt
setup_full_stack.sh
verify_full_stack.py
Dockerfile
OPTIONAL_TOOLS_MANIFEST.md
```

The full stack adds broader ligand preparation, receptor preparation, docking alternatives, MD, MM/GBSA/FEP foundations, pocket detection, scaling tools, and large-table tools.
