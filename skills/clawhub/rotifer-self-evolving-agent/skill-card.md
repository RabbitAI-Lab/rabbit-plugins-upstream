## Description:

Rank an Agent's Rotifer Genes against the Arena and swap in stronger ones after explicit user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to compare project-local Rotifer Genes with live Arena rankings, review stronger candidates, and approve upgrades or rollbacks for agent capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can replace project Genes with third-party Gene code during an approved upgrade.

Mitigation: Review the proposed swap, destination directory, and Gene source before approving; use rollback for the last replacement if needed.

Risk: The runtime uses a pinned npm MCP server package and may execute local Agent Genes through Rotifer tooling.

Mitigation: Review @rotifer/mcp-server@0.15.0 and the Gene being run or installed before use in sensitive projects; keep sandbox-disabling options unavailable.

Risk: Logged-in Rotifer usage can report tool-call telemetry.

Mitigation: Stay logged out or set ROTIFER_TELEMETRY=0 when logged-in telemetry is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xiaoba-dev/skills/rotifer-self-evolving-agent)
- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Documentation](https://rotifer.dev/docs)
- [Rotifer Capability Marketplace](https://rotifer.ai)
- [Rotifer MCP Server npm Package](https://www.npmjs.com/package/@rotifer/mcp-server/v/0.15.0)
- [Rotifer MCP Server Source](https://github.com/rotifer-protocol/rotifer-mcp-server)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline commands and structured upgrade recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose project-scoped Gene or Agent file changes through Rotifer tooling; replacements require explicit user approval and support rollback.]

## Skill Version(s):

2.4.2 (source: server release metadata, SKILL.md frontmatter, clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
