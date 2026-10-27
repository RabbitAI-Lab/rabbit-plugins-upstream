## Description:

Guides users through creating, configuring, and deploying Cargo AI agents, including their knowledge resources, MCP connections, and memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace administrators use this skill to manage Cargo AI agents, configure their models and prompts, attach knowledge and MCP tools, inspect memories, and deploy releases through the Cargo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Removing agents or deploying a draft may change the wrong workspace or live configuration.

Mitigation: Confirm the active workspace, resource UUIDs, and expected impact before remove or deploy commands.

Risk: Agent memories may contain sensitive information.

Mitigation: Review memory output before sharing or storing it.

Risk: API tokens could be exposed in shared logs or transcripts.

Mitigation: Keep tokens out of shared logs and transcripts; consider pinning the CLI version in controlled environments.

## Reference(s):

- [Cargo AI skill release](https://clawhub.ai/cargo-ai/skills/cargo-ai)
- [Cargo skills project homepage](https://github.com/getcargohq/cargo-skills)
- [Agent examples](references/examples/agents.md)
- [MCP server examples](references/examples/mcp-servers.md)
- [AI template examples](references/examples/templates.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance]

**Output Format:** [Markdown with bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the Cargo CLI.]

## Skill Version(s):

2.5.1 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
