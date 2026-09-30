## Description:

Provides pre-install static checks for agent skills and packages through an MCP server, with scan verdicts, CI gates, badges, and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to assess skills or packages before installation, review static findings, and produce reports or CI gate results. Scan verdicts require human confirmation and do not replace runtime safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Published descriptions understate possible network and filesystem effects.

Mitigation: Review the tool's effects before installing or running it in a restricted environment.

Risk: Scanning an npm package can contact the package registry.

Mitigation: Use local directories or tarballs when fully offline operation is required.

Risk: Report or badge output paths can overwrite files.

Mitigation: Only specify output paths whose existing contents may be replaced.

Risk: Global or multi-agent installation persists changes in agent skill directories.

Mitigation: Review destination directories and obtain consent before using global or multi-agent install options.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-verify-mcp)
- [Project homepage listed in ClawHub metadata](https://github.com/YottaMeta/yotta-verify-mcp)
- [Pre-install trust checklist](references/trust-checklist.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration guidance]

**Output Format:** [Scan verdicts and findings, JSON or Markdown reports, and optional SVG badges]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports and badges may be written to user-selected paths; installation and MCP configuration are optional.]

## Skill Version(s):

0.4.4 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
