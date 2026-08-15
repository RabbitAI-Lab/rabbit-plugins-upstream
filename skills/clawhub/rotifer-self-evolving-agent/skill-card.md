## Description:

Evolve AI agents with Rotifer Protocol. Use when you want to scan local agent capabilities, compare Genes in the Arena, inspect fitness scores, or upgrade weak capabilities with stronger alternatives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agent operators use this skill to inspect an agent's local capabilities, compare them against Rotifer Arena rankings, and plan or apply upgrades to stronger alternatives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan verdict is suspicious because the integration can perform broad local execution, publishing, credential, telemetry, and persistent-write actions that are not fully disclosed in the skill materials.

Mitigation: Review the skill and pinned MCP package before installation, use a disposable workspace first, and install only where local writes, publishing workflows, credential storage, and telemetry are acceptable.

Risk: Runtime use can install or overwrite local project Gene files and create or run local Agents.

Mitigation: Require explicit review of proposed changes before approving installs or upgrades, and keep backups or version control for local agent configuration.

Risk: The skill runs @rotifer/mcp-server@0.11.0 through npx and uses outbound network access.

Mitigation: Verify the npm package version and integrity before first use and restrict execution to networks and workspaces where Rotifer cloud communication is allowed.

## Reference(s):

- [Rotifer Protocol](https://rotifer.dev)
- [Rotifer Documentation](https://rotifer.dev/docs)
- [Rotifer MCP Server package](https://www.npmjs.com/package/@rotifer/mcp-server/v/0.11.0)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)
- [ClawHub skill page](https://clawhub.ai/xiaoba-dev/skills/rotifer-self-evolving-agent)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and ranked recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call a runtime MCP server through npx and may propose or perform local Gene installation after user confirmation.]

## Skill Version(s):

2.3.1 (source: frontmatter, clawhub metadata, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
