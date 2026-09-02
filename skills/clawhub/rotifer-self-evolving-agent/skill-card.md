## Description:

Rank an Agent's Rotifer Genes against the Arena, compare local capabilities with fitness scores, and replace weaker Genes only after user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to inspect Rotifer Gene fitness, discover stronger alternatives, and make approved upgrades to a project's local Agent capabilities. It also supports creating and running local Agents from installed Genes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill fetches and runs the pinned @rotifer/mcp-server package through npx.

Mitigation: Review the package source or verify the npm package integrity before use, and run it only in environments where this dependency is acceptable.

Risk: Upgrades can install third-party Genes and change what a local Agent does at runtime.

Mitigation: Review each proposed replacement before approving it, use the skill only in projects where Gene changes are intended, and use rollback when a replacement should be undone.

Risk: The skill can write project Gene and Agent files and execute local Agents.

Mitigation: Run it in the intended project workspace, confirm the destination directory before upgrades, and avoid running Agents unless execution is expected.

Risk: Rotifer usage reporting or install-count calls may occur as described by the release evidence.

Mitigation: Set ROTIFER_TELEMETRY=0 when usage reporting and install-count calls are not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoba-dev/skills/rotifer-self-evolving-agent)
- [Publisher profile](https://clawhub.ai/user/xiaoba-dev)
- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer documentation](https://rotifer.dev/docs)
- [Rotifer MCP Server package](https://www.npmjs.com/package/@rotifer/mcp-server/v/0.17.0)
- [Rotifer MCP Server source](https://github.com/rotifer-protocol/rotifer-mcp-server)
- [Rotifer Protocol specification](https://github.com/rotifer-protocol/rotifer-spec)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with command examples, ranked comparisons, and approval prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose project file changes, Gene installation, rollback commands, or local Agent execution steps that require explicit user approval.]

## Skill Version(s):

2.4.7 (source: server release evidence, SKILL.md frontmatter, clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
