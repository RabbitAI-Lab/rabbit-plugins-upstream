# Small-molecule docking

## Goal and method

Explore receptor–small-molecule binding poses and compare results under a defined preparation and docking setup. `Molecular Docking (SMINA)` identifies the intended method family; establish its compatibility with the user's receptor, ligands, and binding-site strategy.

## Inputs and choices

- Receptor structure and its intended prepared state.
- Ligand structures, identities, and relevant states supported by the method.
- Binding-site or search-region specification, including the coordinate reference it belongs to.
- The comparison objective and any user-imposed constraints.

Inspect receptor, ligand, and site evidence before judging readiness. Do not assume protonation, receptor preparation, ligand state, docking-box dimensions, or a known binding site. Resolve only choices required for the actual task; do not request setup details for a conceptual explanation.

## Business workflow

1. Establish that the supplied receptor, ligands, and site definition describe the intended docking problem.
2. Resolve incompatible or missing preparation/site requirements using available evidence and the user's scientific choices. Preserve ligand identities and the relationship between site coordinates and receptor structure.
3. Run the selected docking method and obtain its poses and scores.
4. Match each pose and score to its ligand and receptor/setup. When comparing results, establish comparable preparation, search regions, and scoring settings; explain differences rather than silently combining unlike scores.

## Results

Deliver pose structures, corresponding ligand identities and scores, and the setup needed to interpret them. Report missing or failed ligand results separately from successful docking outputs.

Scores and poses provide computational prioritization, not measured affinity or proof of binding. Explain preparation, scoring, and sampling limitations. Interpret existing docking results without starting replacement calculations unless that serves an explicit execution request.
