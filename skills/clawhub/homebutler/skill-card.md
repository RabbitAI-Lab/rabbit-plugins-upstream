## Description:

Tells an agent what changed on a server since it last looked - plus status, Docker, backups, Proxmox. 44 MCP tools, each classed read, write or destructive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[higangssh](https://clawhub.ai/user/higangssh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and self-hosting administrators use this skill to let an agent inspect configured servers, summarize meaningful changes, and manage Docker, backups, Proxmox guests, alerts, and install workflows through classified MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect configured servers and return operational details such as hostnames, internal addresses, ports, processes, and logs.

Mitigation: Run reads only against requested targets and summarize relevant findings instead of exposing raw logs or broad inventory data.

Risk: The skill can perform write or destructive operations including restore, purge, stop, shutdown, restart, install, and Proxmox guest actions.

Mitigation: Require explicit operator approval for destructive actions and review configured tokens, SSH credentials, and dashboard exposure before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/higangssh/skills/homebutler)
- [Publisher profile](https://clawhub.ai/user/higangssh)
- [Homebutler repository](https://github.com/Higangssh/homebutler)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool calls or pinned install and configuration commands; destructive actions require explicit operator approval.]

## Skill Version(s):

2.3.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
