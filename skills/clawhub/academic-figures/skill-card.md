## Description:

Creates publication-ready scientific figures from JSON, CSV, or Excel data using a local chart-generation tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to turn research data into publication-ready charts, multi-panel figures, and journal submission graphics with local rendering and optional PDF checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rendering reads local research data and writes figure files.

Mitigation: Review input and output paths and use appropriate access controls for sensitive data.

Risk: The separately advertised cloud edition may handle data differently from local rendering.

Mitigation: Assess the cloud product separately; do not assume the local privacy statement applies to it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Quick start](artifact/references/quickstart.md)
- [Data formats](artifact/references/data-formats.md)
- [Limits and compatibility](artifact/references/limits.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The local tool can write figure files including PDF, PNG, TIFF, SVG, and EPS.]

## Skill Version(s):

4.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
