## Description:

Helps agents generate publication-ready scientific charts from local data using journal presets, statistical plots, and multi-format exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to turn CSV, JSON, or Excel data into publication-ready figures, including statistical plots and multi-panel layouts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running local charting scripts on sensitive input data and installing plotting dependencies requires trust in the release and its dependencies.

Mitigation: Review the release and dependencies before running; keep sensitive data in the intended local environment.

Risk: Optional localhost MCP mode or separate cloud/pro offerings may change how figure generation is accessed or where data is handled.

Mitigation: Review the optional MCP behavior before enabling it, and use cloud/pro offerings only after separately assessing their data handling.

## Reference(s):

- [Academic Figures on ClawHub](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Quickstart](references/quickstart.md)
- [Data formats](references/data-formats.md)
- [Limits and compatibility](references/limits.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands produce local figure files in formats such as PNG, PDF, and TIFF; optional figure descriptions are available.]

## Skill Version(s):

4.3.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
