# Molecular dynamics

## Goal and routes

Simulate the user's molecular system or analyze an existing trajectory to answer a stated question. Distinguish new simulation, readiness assessment, and analysis of existing results before preparing inputs.

For new simulations, choose a protein-only or protein–ligand-complex workflow from the observed system composition. `Protein MD Simulation v2.1` and `Protein-Ligand Complex MD Simulation` identify relevant workflow families; verify their supported systems and preparation requirements.

## Inputs and choices

- Molecular structures and the intended system, including the identity and role of any ligand.
- Evidence of preparation readiness. Do not invent protonation, repair missing residues, remove a ligand, or assume force-field readiness merely to satisfy an input format.
- Required environment, preparation, and simulation-duration choices, guided by the user's question and the chosen workflow's documented settings.
- For trajectory analysis, corresponding topology/reference information and the question the analysis should address.

## Business workflow

1. Inspect the actual system and identify concrete preparation gaps or mismatches with the selected workflow.
2. Resolve required scientific choices and preserve the system definition through preparation. Avoid replacing a protein–ligand task with protein-only simulation.
3. For a new simulation, run the selected workflow and retrieve the trajectory and declared supporting outputs. For an existing-trajectory request, use the supplied results without starting a new simulation.
4. Relate analysis to the user's question and available evidence. Keep trajectory, topology, time interval, selections, and analysis settings associated with each reported metric.

## Results

Deliver the relevant trajectory or analysis outputs with the effective system and simulation settings. Distinguish the requested duration from the completed trajectory and indicate incomplete runs or unavailable analysis.

Describe observed conformational changes and computed metrics within the sampled interval. Do not promote those observations into unsupported thermodynamic or experimental conclusions. A general explanation of molecular dynamics does not require collecting simulation parameters.
