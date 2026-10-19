## Description:

Generates publication-ready scientific charts from local data in journal-friendly image formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and analysts use this skill to turn JSON, CSV, or Excel data into publication-ready figures, including clinical and statistical charts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional dependency repair downloads Python packages.

Mitigation: Use --fix only when you intend to install dependencies; review the environment first.

Risk: Reproducibility bundles copy input data, which may be sensitive.

Mitigation: Review data sensitivity and output location before using --repro or sharing its bundle.

Risk: Regression tests may run commands embedded in modified templates.

Mitigation: Review template _command fields before running tests on modified templates.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Getting started and chart selection](references/quickstart.md)
- [Input data formats](references/data-formats.md)
- [Known limitations](references/limits.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [PNG, PDF, TIFF, SVG, or EPS figures; optional JSON audit and reproducibility bundle]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local rendering; journal presets and optional overlap checks.]

## Skill Version(s):

5.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
