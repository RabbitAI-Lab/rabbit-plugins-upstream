## Description:

Helps researchers and developers turn research data into publication-ready scientific figures using local charting tools and journal presets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to generate and export scientific charts from JSON, CSV, or Excel data for papers and journal submissions, including clinical and statistical figures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server uses predictable shared temporary figure paths, which may expose or mix sensitive outputs on shared systems.

Mitigation: For sensitive patient, research, or business data, use the CLI in a private workspace and avoid the MCP server until its temporary output paths are fixed.

Risk: Optional environment repair and MCP installation can download dependencies from the network.

Mitigation: Review and approve dependencies before running setup_env.py --fix or installing the MCP server via uvx/git.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Getting started](references/quickstart.md)
- [Data formats](references/data-formats.md)
- [Limits and flag interactions](references/limits.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Text guidance and chart files (PNG, PDF, TIFF, SVG or EPS)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Figures are generated from local data; verify publication output before use.]

## Skill Version(s):

5.3.0 (source: server release metadata and packaged changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
