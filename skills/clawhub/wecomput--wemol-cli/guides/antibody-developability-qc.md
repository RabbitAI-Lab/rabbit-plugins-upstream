# Antibody developability QC

## Goal and method

Screen existing antibody candidates for the developability risks covered by the selected QC method. Distinguish conventional antibodies from nanobodies using user evidence and inspected inputs.

`Antibody QC v1.1` and `Nanobody QC v1.0` identify relevant method families. Their input requirements, covered checks, and thresholds need not be identical.

## Inputs and choices

- Candidate FASTA sequences, with identities and chain pairing where applicable, are the execution inputs for the referenced QC workflows. A supplied structure can inform input assessment but is not a substitute for the required sequence; resolve sequence completeness and chain correspondence before deriving FASTA from it.
- Molecule class and the user's specific screening or comparison objective.
- Method-required inputs and any justified threshold choices. Use documented defaults where applicable; do not invent universal pass/fail thresholds.

An entry accepting only sequences does not establish whether internal checks use structures. Determine actual check coverage from the workflow and result definitions, and retain the numbering scheme used when interpreting residue-level flags.

## Business workflow

1. Choose the QC method that matches the evidenced molecule class and available representation.
2. Establish which requested checks that method actually covers and identify unavailable evidence before execution.
3. Evaluate the supplied candidates without silently redesigning their sequences or changing their molecular identity.
4. Match each reported flag or metric to its candidate, documented definition, and threshold. Preserve distinctions between a completed check with no flag, a missing check, and a failed evaluation.

## Results

Deliver a per-candidate screening summary with reported metrics, flags, covered checks, and gaps. Compare candidates only across equivalent checks and settings. Use an overall score only if the method provides a documented interpretation; do not manufacture a universal “QC passed” verdict.

Explain findings in their documented context and identify experimental follow-up where warranted. Computational flags do not establish manufacturing suitability, safety, or clinical outcomes. General questions about QC do not require files or computation.
