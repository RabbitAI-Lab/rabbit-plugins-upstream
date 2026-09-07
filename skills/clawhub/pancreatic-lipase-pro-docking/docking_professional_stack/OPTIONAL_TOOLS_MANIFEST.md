# Optional Tools Manifest — Do Not Miss Workflow Components

This stack is designed in layers. Core docking should work with RDKit + OpenBabel + Meeko + Vina. Advanced simulation requires more.

## Core required for docking
- RDKit: SMILES handling, descriptors, PAINS, fingerprints, clustering
- Open Babel: 3D generation and format conversion
- Meeko: PDBQT ligand/receptor preparation
- AutoDock Vina: docking engine
- pandas/numpy/scipy/sklearn: ranking, tables, clustering, statistics

## Better docking / alternatives
- Smina: Vina fork with useful scoring/minimization features
- Gnina: CNN rescoring/docking; install separately if GPU/CUDA desired
- QuickVina / AutoDock-GPU: optional high-throughput alternatives
- Commercial options if licensed: Glide, GOLD, MOE

## Protein preparation
- PDBFixer: missing atoms/residues, cleanup
- pdb-tools, Gemmi, Biopython: PDB/mmCIF parsing and manipulation
- PropKa/PDB2PQR: pKa/protonation support
- Reduce: hydrogen placement; often installed separately

## GI-fluid / pH-state preparation
- Dimorphite-DL: protonation states by pH
- Gypsum-DL: tautomers/protomers/conformers; install separately if needed
- Epik/Marvin: commercial alternatives if licensed

## Interaction analysis
- PLIP: protein-ligand interaction profiler
- ProLIF: interaction fingerprints, especially useful for MD trajectories
- ODDT: cheminformatics/docking utilities

## MD / simulation
- OpenMM: Python-native MD
- OpenMMForceFields / OpenFF Toolkit: small-molecule force fields
- AmberTools: antechamber, tleap, MMPBSA.py
- GROMACS: production MD engine
- MDTraj / MDAnalysis: trajectory analysis
- ParmEd: topology conversion

## Free energy / finalist rescoring
- gmx_MMPBSA: MM/GBSA wrapper for GROMACS
- OpenFE: open-source RBFE/FEP setup
- Cinnabar: free-energy result analysis
- Perses/YANK/BioSimSpace: optional specialized workflows

## Pocket detection / receptor ensemble
- fpocket: pocket detection
- MDAnalysis/MDTraj: generate receptor snapshots from MD
- ProDy: normal modes / structural analysis

## Scaling and workflow
- GNU parallel: local subchunk parallelization
- Snakemake: reproducible pipelines
- Dask/Distributed: Python-level scaling
- SLURM templates: HPC arrays
- DuckDB/Polars/PyArrow: large result-table handling

## Separate/manual installs often needed
Some tools are not always reliable from one conda environment:
- Gnina: download release binary from official GitHub
- AutoDock-GPU: compile/install separately
- Schrödinger/FEP+/Glide: commercial license
- GOLD/MOE: commercial license
- Gaussian/Q-Chem/ORCA: QM packages; ORCA requires free academic registration
- CUDA drivers: must match host GPU

## Reality check
No environment can literally guarantee “never miss anything.” The safeguard is:
1. maintain this manifest,
2. run `verify_full_stack.py`,
3. fail gracefully if optional tools are missing,
4. use fallback workflows,
5. report missing capabilities before claiming results.
