## Description:

Helps researchers create publication-ready scientific charts and journal figures from local data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to turn local research data into publication-ready charts, statistical figures, and multi-panel journal submissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local plotting code reads supplied data and writes figure files or reports.

Mitigation: Review the input data and output paths before running, especially when handling sensitive research data.

Risk: Optional localhost HTTP mode can expose sensitive data to other local clients.

Mitigation: Use the default stdio MCP mode for sensitive data; enable localhost HTTP only when needed.

Risk: Optional environment setup installs Python dependencies.

Mitigation: Run setup only when needed, after reviewing the dependencies and using an appropriate Python environment.

## Reference(s):

- [Academic Figures on ClawHub](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Getting started](artifact/references/quickstart.md)
- [Data formats](artifact/references/data-formats.md)
- [Limits and compatibility](artifact/references/limits.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance and locally generated PNG, PDF, SVG, TIFF, or EPS figures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May also write validation reports, figure legends, and alternative text.]

## Skill Version(s):

4.5.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
