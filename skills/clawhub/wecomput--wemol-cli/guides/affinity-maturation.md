# Affinity maturation

## Goal and method

Optimize an existing antibody against a specified antigen while respecting mutation and preservation constraints. This task starts from an antibody; it does not authorize replacing it with an unrelated de novo design.

`Virtual Affinity Maturation v3.4` identifies the intended method family. Verify its current input requirements, supported optimization method, mutable regions, and output meaning.

## Inputs and choices

- Starting antibody, target antigen, and their structural relationship. For the referenced workflow, prepare the PDB input and identify the chain to mutate. Binding optimization requires a supported antibody–antigen complex representation; separate sequences alone do not establish that relationship, and the workflow must not be assumed to dock them automatically.
- Optimization objective, permitted mutation scope, and residues or regions that must remain unchanged.
- Candidate or computation limits when needed by the method or the user's budget.

Inspect available evidence before requesting missing information. Do not assume the target, reconstruct an unsupported complex, or broaden mutation scope to make the task run.

Map permitted mutation positions and protected residues through structure preparation and renumbering. Distinguish author residue identifiers, sequential positions, and antibody numbering schemes. The referenced evolution method may use the full target-chain sequence when mutation positions are omitted; omission must not broaden a user-specified mutable region or include protected residues. Verify the effective positions rather than copying residue numbers between representations.

## Business workflow

1. Establish the starting antibody–antigen relationship and check readiness for the selected method.
2. Apply the resolved mutation and preservation constraints with compatible documented defaults.
3. Generate or evaluate variants and obtain their sequence changes and predicted optimization metrics.
4. Compare variants to the starting antibody when comparable baseline evidence is available. Otherwise state that the output ranks variants without establishing a measured improvement over the starting molecule.

## Results

Deliver candidate identities, substitutions, relevant scores, and the constraints under which they were produced. Use the documented ranking rule; identify incomplete evaluations and unsupported comparisons.

Predicted improvement is not measured binding affinity. Do not imply preserved specificity, stability, or developability without separate evidence. For explanation or existing-result requests, answer that scope without starting optimization.
