## Description:

ClickUp MCP (developer.clickup.com). Use this skill for ClickUp MCP requests that read, create, and update data through the OOMOL-connected connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate ClickUp through an OOMOL-connected account, including reading workspace data, creating and updating tasks, adding task comments, searching workspaces, and sending ClickUp Chat messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can run unverified code on a user's machine.

Mitigation: Install the oo CLI through a verifiable package or reviewed installer rather than piping remote scripts directly into a shell.

Risk: Write actions can create tasks, add comments, send chat messages, or update existing ClickUp tasks.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: The skill operates against ClickUp data through an OOMOL-connected account.

Mitigation: Install and use it only when the OOMOL connector and ClickUp data access are acceptable for the deployment.

## Reference(s):

- [ClickUp MCP documentation](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clickup-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce ClickUp connector calls that return JSON data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
