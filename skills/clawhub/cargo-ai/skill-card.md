## Description:

Create and configure AI agents, attach knowledge for RAG, manage MCP servers, and handle agent memories using the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cargo AI agent resources from the CLI, including agent creation, release configuration and deployment, knowledge attachment, MCP server connections, templates, and memories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deploy, remove, and memory update commands can change live Cargo agent behavior or delete workspace resources.

Mitigation: Require explicit user approval before deploy, remove, MCP access, or memory changes, and verify the active workspace plus target UUIDs with discovery commands first.

Risk: The documented bearer-token API workaround can expose credentials in shared terminals, shell history, or logs.

Mitigation: Prefer CLI-mediated commands where possible, avoid pasting bearer tokens into shared environments, and redact tokens from logs and transcripts.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-ai)
- [Agent examples](references/examples/agents.md)
- [MCP server examples](references/examples/mcp-servers.md)
- [AI template examples](references/examples/templates.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require the Cargo CLI, authenticated workspace access, and valid Cargo resource UUIDs.]

## Skill Version(s):

2.2.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
