## Description:

Install, configure, or run pi-coding-agent through the pibox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use pibox to run pi-coding-agent against selected workspaces and connect it to scripts, HTTP clients, MCP tools, Telegram, or scheduled jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed API or MCP service without its own bearer token can grant agent execution and workspace file access to anyone who can reach it.

Mitigation: Set distinct API and MCP tokens and bind ports to loopback; add stronger access controls before any shared or public exposure.

Risk: Piping an installer into a shell, using an unpinned image, or deploying with host networking increases installation and exposure risks.

Mitigation: Inspect the installer first, pin the Docker image by digest, and prefer explicit loopback port bindings to host networking.

Risk: Agent access to broad workspace mounts and destructive file or run operations can cause irrecoverable data loss.

Mitigation: Mount only necessary workspaces, back up important data, and require explicit confirmation of a specific target before deletion.

## Reference(s):

- [pibox setup guide](artifact/references/setup.md)
- [pibox project homepage](https://github.com/psyb0t/docker-pibox)
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)
- [pibox on ClawHub](https://clawhub.ai/psyb0t/skills/pibox)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run an agent that reads and changes files in a selected workspace.]

## Skill Version(s):

0.19.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
