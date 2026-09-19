## Description:

Build and configure AI agents inside Cargo by creating agents, choosing model settings, writing prompts, attaching knowledge for retrieval, connecting MCP tool servers, managing memories, and deploying releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cargo AI agent resources from the CLI, including agent creation, release configuration, knowledge attachment, MCP setup, and memory maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a mutable global npm install for @cargo-ai/cli.

Mitigation: Use a pinned, reviewed CLI version where possible before installing or running commands.

Risk: The skill documents credentialed operations that can change agents, releases, memories, MCP servers, and other workspace state.

Mitigation: Confirm the active Cargo workspace with cargo-ai whoami, use least-privileged or short-lived tokens, and review remove, deploy, memory, and MCP changes before execution.

Risk: Direct curl examples depend on CARGO_API_BASE and bearer-token configuration.

Mitigation: Verify CARGO_API_BASE and token scope before running direct API calls.

## Reference(s):

- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills)
- [ClawHub cargo-ai Skill](https://clawhub.ai/cargo-ai/skills/cargo-ai)
- [Response Shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [Agent Examples](references/examples/agents.md)
- [MCP Server Examples](references/examples/mcp-servers.md)
- [AI Template Examples](references/examples/templates.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, API calls]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands generally return JSON; workspace-changing operations require Cargo authentication and should be reviewed before execution.]

## Skill Version(s):

2.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
