## Description:

Ranks an Agent's Rotifer Genes against Arena data, compares local capabilities, and proposes stronger replacements that require user approval before installation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and agent operators use this skill to assess locally installed Rotifer Genes against live Arena rankings, compare alternatives, and approve upgrades or rollbacks for project-scoped agent capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch a pinned npm MCP server and run Rotifer Agent workflows.

Mitigation: Review the npm package and proposed commands before use; run only in projects where Rotifer execution and network access are acceptable.

Risk: Approved upgrades can install third-party Gene code into the current project's Genes directory.

Mitigation: Inspect each proposed Gene swap before approving it, and use the documented rollback path if the replacement is not desired.

Risk: Rotifer usage records or install counters may be sent depending on login and telemetry settings.

Mitigation: Set ROTIFER_TELEMETRY=0 when telemetry and install-count reporting should be disabled.

## Reference(s):

- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Documentation](https://rotifer.dev/docs)
- [Rotifer Capability Marketplace](https://rotifer.ai)
- [Rotifer MCP Server npm package](https://www.npmjs.com/package/@rotifer/mcp-server/v/0.16.1)
- [Rotifer MCP Server source](https://github.com/rotifer-protocol/rotifer-mcp-server)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose project file changes for Genes or Agent definitions only after user approval.]

## Skill Version(s):

2.4.5 (source: ClawHub release metadata, clawhub.json, and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
