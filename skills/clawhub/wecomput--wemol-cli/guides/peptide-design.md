# Peptide design

## Goal and method

Generate peptide candidates for the user's target and design objective. Preserve the requested molecular product: protein-binder design is a separate route, not an interchangeable implementation of peptide design.

`Peptide Design (PepCraft)` identifies the peptide method family. Consider `Protein Binder Design (BindCraft)` only when the user requests protein binders or the desired product is genuinely unresolved. Do not reopen an explicit peptide choice just because both methods exist.

## Inputs and choices

- For PepCraft, one receptor sequence, the desired peptide length, and a binding hotspot are required. A receptor structure alone does not supply the sequence-based input and hotspot mapping.
- Hotspots refer to receptor-sequence positions numbered from 1. Map any structure-based site to that sequence, accounting for chain selection, missing residues, and numbering changes; do not copy author residue numbers directly. An unspecified hotspot is an unresolved input for this route, not permission to invent a site.
- Intended product class, peptide chemistry, and any user-specified interface or preservation constraints supported by the method.
- Candidate count or other design settings only when needed for the requested execution.

Inspect supplied targets before judging compatibility. A generic word such as “binder” does not by itself resolve the product class or justify changing it.

## Business workflow

1. Establish the intended peptide product and target and select a compatible method.
2. Resolve the method-required target and design constraints without inventing an objective or changing the user's molecule class.
3. Generate the requested candidates and obtain their sequences, structures where provided, and method-reported scores.
4. Preserve candidate and target identities, and compare only outputs for compatible objectives and settings. Identify missing outputs rather than silently replacing them with a different design route.

## Results

Deliver candidates, the constraints used, and the evidence supporting any prioritization. Additional evaluation should answer an identified question within the user's scope.

Generated sequences and structures are computational candidates. Do not claim measured binding, specificity, stability, or safety from generation alone. For informational requests, explain the relevant route differences without gathering execution parameters.
