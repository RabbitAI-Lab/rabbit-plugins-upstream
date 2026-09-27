## Description:

Install, configure, or run Claude Code through the claudebox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use claudebox to run Claude Code in a Docker container for coding tasks, or connect other tools to its HTTP, MCP, Telegram, and scheduled-job interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Claude Code runs with broad shell and file permissions inside the container.

Mitigation: Use only with trusted prompts and workspaces; isolate the container before handling untrusted input.

Risk: HTTP and MCP modes can expose agent execution and workspace files without authentication if tokens are unset.

Mitigation: Set distinct API and MCP bearer tokens and bind services to localhost or a trusted network.

Risk: Mounting the Docker socket can grant host-level container control.

Mitigation: Avoid mounting /var/run/docker.sock unless necessary, and restrict access to trusted users.

Risk: Remote install scripts and changing images or packages can introduce unexpected behavior.

Mitigation: Review downloaded installers before execution and consider pinning images and packages for production use.

## Reference(s):

- [claudebox on ClawHub](https://clawhub.ai/psyb0t/skills/claudebox)
- [claudebox project homepage](https://github.com/psyb0t/docker-claudebox)
- [claudebox setup guide](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.4.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
