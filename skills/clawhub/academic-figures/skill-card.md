## Description:

Creates publication-ready scientific figures from data using local chart rendering, journal presets, and multi-format export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to turn JSON, CSV, or Excel data into journal-ready figures, including statistical and multi-panel visualizations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local rendering reads user-supplied data files and writes figure outputs.

Mitigation: Review input and output paths, and use the reviewed local artifact for sensitive data.

Risk: An optional repository-based MCP install fetches code at install time.

Mitigation: Review the fetched source before installation or prefer the reviewed local artifact.

Risk: Figures and statistical annotations can be mistaken for validated scientific findings.

Mitigation: Check source data, statistical methods, and annotations independently before publication.

## Reference(s):

- [Academic Figures release on ClawHub](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Getting started](references/quickstart.md)
- [Data formats](references/data-formats.md)
- [Limits and compatibility](references/limits.md)
- [Color guide](references/color-guide.md)
- [Multi-figure guide](references/combo-guide.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [PNG, TIFF, PDF, SVG, or EPS figures; text guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports multi-format export, composite figures, and optional batch reports.]

## Skill Version(s):

4.7.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
