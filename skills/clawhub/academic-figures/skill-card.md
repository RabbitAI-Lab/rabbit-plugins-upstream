## Description:

Helps create publication-ready scientific charts and diagrams from JSON, CSV, or Excel data using local Python tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to turn study data into journal-style figures, multi-panel layouts, and supplementary legends, with optional PDF quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local generator reads selected data files and writes figures or reports to chosen paths.

Mitigation: Check input and output paths before running it, especially where existing files could be replaced.

Risk: Optional environment setup checks the local system and cleans the matplotlib font cache.

Mitigation: Run setup_env.py only after accepting those local environment changes.

Risk: The separately advertised Pro cloud service may require uploading data.

Mitigation: Keep sensitive data in the local workflow unless cloud upload has been separately approved.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Getting started](references/quickstart.md)
- [Data formats](references/data-formats.md)
- [Limits and compatibility](references/limits.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Files]

**Output Format:** [Text guidance and commands; generated PNG, PDF, TIFF, SVG, or EPS figures and optional text legends]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional multi-format export and PDF overlap or font-size checks]

## Skill Version(s):

3.9.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
