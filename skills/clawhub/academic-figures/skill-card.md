## Description:

Helps create publication-ready scientific charts from local data using journal presets, statistical annotations, and multi-format export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to prepare scientific figures and journal-ready exports from local datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running local Python scripts on research data requires installing scientific Python dependencies.

Mitigation: Review the scripts and dependencies, then install and run them only in an environment you trust.

Risk: Batch or pipeline runs can write multiple output files to selected paths.

Mitigation: Review output paths and pipeline manifests before running them.

Risk: The optional setup script may clear the matplotlib font cache.

Mitigation: Run setup only when needed and account for its local environment changes.

## Reference(s):

- [Academic Figures on ClawHub](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Getting started](references/quickstart.md)
- [Data formats](references/data-formats.md)
- [Limits and compatibility](references/limits.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Text instructions and locally generated figure files (PNG, PDF, TIFF, SVG, EPS)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports journal presets, quality checks, and multi-format export.]

## Skill Version(s):

4.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
