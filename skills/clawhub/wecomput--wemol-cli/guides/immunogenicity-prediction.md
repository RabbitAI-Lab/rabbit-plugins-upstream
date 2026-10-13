# Immunogenicity prediction

## Goal and method

Assess supplied molecular sequences with the intended immunogenicity prediction method and explain the resulting evidence. The preferred method family for this task is WeADApt v4.3. This preference does not establish that a particular platform entry is available, latest, or suitable for every molecule.

Consider older WeADApt or AlphaMHC methods when the user requests comparison, needs a historical workflow, or the preferred method is unavailable. Establish any alternative's suitability and changed scope before using it; method names alone do not establish equivalence.

## Inputs and choices

- Inspect sequence format, actual contents, record identities, and the intended molecule.
- Resolve species or other scientific context only where material to the method and user objective.
- Distinguish new prediction, input-suitability assessment, comparison, and interpretation of an existing report.

Do not infer molecule type or scientific purpose solely from a filename, and do not silently alter sequences to satisfy input requirements.

## Business workflow

1. Establish that the preferred method supports the supplied molecule and intended assessment.
2. Resolve required scientific choices and prepare the compatible input representation with stable candidate identities.
3. Perform the requested prediction and obtain the declared score or report outputs.
4. Map results back to the supplied records. For comparisons, retain method versions and effective settings and establish whether the reported quantities are comparable.

## Results

Deliver per-record predictions with their documented meanings, applicable settings, and missing coverage. Explain only fields supported by the actual report and method evidence; do not invent thresholds or interpret missing values as low risk.

Distinguish computational predictions from experimental or clinical validation. Existing-result interpretation does not imply permission to rerun the analysis.
