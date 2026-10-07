## Description:

Provides pre-install static security scans of agent skills and packages through MCP tools for verdicts, audit badges, CI gates, and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use the MCP tools to assess authorized skills or packages before installation, check CI thresholds, and review scan findings and reports before deciding whether to install.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning npm package specifications may use the network and resolve packages despite offline claims.

Mitigation: Prefer local directories or downloaded tarballs; scan arbitrary npm package specifications only in a sandbox.

Risk: Report output and related operations may write files outside the expected scan scope.

Mitigation: Review the output path and any proposed configuration changes before permitting writes.

Risk: Static scan verdicts cannot establish that an untrusted package is safe to install.

Mitigation: Review findings and package permissions independently; do not use this scanner as the sole pre-install gate.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-verify-mcp)
- [Project homepage listed in metadata](https://github.com/YottaMeta/yotta-verify-mcp)
- [Pre-install trust checklist](references/trust-checklist.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, SVG badges]

**Output Format:** [Text, JSON, Markdown, or SVG depending on the tool]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verdicts and severity findings; optional report and badge files.]

## Skill Version(s):

0.4.5 (source: ClawHub release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
