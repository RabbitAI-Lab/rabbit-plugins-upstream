## Description:

ClickUp MCP helps an agent read, create, and update ClickUp data through the OOMOL oo CLI connector instead of calling the ClickUp API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate ClickUp workspaces through an OOMOL-connected account, including reading workspace data, searching tasks and docs, creating or updating tasks, commenting, and sending ClickUp Chat messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup asks users or agents to run an unverified remote installer directly in a shell.

Mitigation: Review the oo CLI installer before running it, prefer a signed or package-manager installation path if available, and do not run the installer from an elevated shell.

Risk: Write actions can change ClickUp tasks or send ClickUp Chat messages.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write actions; require explicit approval before any destructive action.

## Reference(s):

- [ClickUp MCP documentation](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clickup-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
