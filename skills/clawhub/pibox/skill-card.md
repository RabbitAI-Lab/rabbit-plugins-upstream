## Description:

Install, configure, or run pi-coding-agent through the pibox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to set up and operate a containerized coding agent in a workspace, or connect clients through its API, MCP, Telegram, and scheduled-run interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unauthenticated API or MCP endpoint can grant access to agent execution and workspace files.

Mitigation: Use separate non-empty API and MCP bearer tokens; restrict access to localhost or an authenticated proxy.

Risk: Workspace mounts and network access give the coding agent broad control over local data and connected services.

Mitigation: Mount only intended workspaces, avoid host networking unless necessary, and review the image or installer source before production use.

Risk: Deletion, scheduled tasks, Telegram access, and remote calls can affect files or runs beyond the current task.

Mitigation: Treat these as administrative capabilities; restrict access and confirm the specific target before any destructive action.

## Reference(s):

- [pibox setup guide](references/setup.md)
- [pibox project](https://github.com/psyb0t/docker-pibox)
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)
- [ClawHub pibox release](https://clawhub.ai/psyb0t/skills/pibox)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance can lead to agent execution and workspace changes when followed.]

## Skill Version(s):

0.19.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
