# Antibody humanization

## Goal and method

Generate or assess humanization candidates for an existing antibody. The principal branch is conventional antibody versus nanobody/single-domain antibody. Choose from the supplied molecule and user evidence; a filename or a generic “antibody” label alone may not resolve the branch.

`Antibody Humanization v4.7` and `Nanobody Humanization v4.7` are method-family references. Verify the available method's suitability rather than treating these labels as current availability guarantees.

## Inputs and choices

- The referenced humanization workflows accept FASTA sequences. Inspect starting sequences, chain identities, and any heavy/light-chain pairing. If the user supplies a structure, establish the intended sequence and its chain correspondence before preparing FASTA; unresolved residues in coordinates must not silently become deletions in the submitted sequence.
- Preserve the user's specified residues, regions, or other design constraints. Resolve framework, species, numbering, and mutation choices only when material to the selected method and task.
- Distinguish generating new candidates from evaluating or comparing candidates already supplied.

A sequence-only entry does not mean that the workflow lacks structural calculations: modeling and structure comparison may be internal steps. Determine their coverage from the workflow and delivered evidence rather than the entry-file format.

## Business workflow

1. Select the humanization method appropriate to the evidenced molecule class and accepted input representation.
2. Check input compatibility and resolve required preservation or modification choices. Keep the relationship to the original antibody explicit.
3. Perform the requested humanization or evaluation and obtain candidate sequences, substitutions, and reported scores.
4. Compare candidates to their own starting sequence. Preserve chain and residue correspondence when presenting changes, and distinguish method recommendations from user-imposed constraints.

## Results

Deliver candidates with their source antibody, proposed changes, reported scores, and any missing outputs. Explain trade-offs supported by the method evidence rather than selecting a winner from an undocumented combined score.

Humanization alone does not establish preserved affinity, improved developability, or reduced immunogenicity. Additional evaluations serve separate questions and should not be added automatically. A conceptual inquiry does not require collecting mutation or submission parameters.
