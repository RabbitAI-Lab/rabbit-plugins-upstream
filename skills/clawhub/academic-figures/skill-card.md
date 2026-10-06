## Description:

Generates publication-ready scientific figures from local research data, with journal presets, multiple chart types, and figure verification tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to turn local CSV, JSON, or spreadsheet data into journal-ready charts, multi-panel figures, and accessible figure descriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP mode may leave chart data and previews at predictable shared temporary paths, exposing sensitive or unpublished material.

Mitigation: Use an isolated local environment for sensitive work; clean temporary files after MCP use or avoid MCP mode until private per-request storage and cleanup are available.

Risk: Batch and pipeline files can direct local file reads, writes, and figure-rendering processes.

Mitigation: Only run trusted batch or pipeline files, and review their input and output paths before execution.

## Reference(s):

- [Academic Figures on ClawHub](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Getting started](artifact/references/quickstart.md)
- [Data formats](artifact/references/data-formats.md)
- [Limits and compatibility](artifact/references/limits.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Figure files, Text]

**Output Format:** [Local PNG, TIFF, PDF, SVG, or EPS figures; optional text legends and alt text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports multi-format export, journal presets, and optional PDF layout checks.]

## Skill Version(s):

4.4.0 (source: server release metadata and skill version history)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
