## Description:

ClickUp MCP lets agents operate an authorized ClickUp workspace through OOMOL's clickup_mcp connector to read, search, create, update, comment on tasks, and send ClickUp Chat messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent interact with authorized ClickUp workspaces: inspect workspace hierarchy and members, search workspace content, and perform confirmed task, comment, and chat write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute remote installer scripts before the user has reviewed or verified them.

Mitigation: Review the installer source before first-time setup and prefer an official signed or package-manager installation path when available.

Risk: Write actions can create tasks, add comments, send chat messages, or update task properties in the connected ClickUp workspace.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

## Reference(s):

- [ClickUp MCP documentation](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
