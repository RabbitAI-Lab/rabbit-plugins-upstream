## Description:

Full control of a remote machine via Remote Claws MCP: screenshots, mouse/keyboard, browser automation, run commands, read/write files on the remote host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wentbackward](https://clawhub.ai/user/wentbackward)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to control a trusted remote desktop host through permissioned MCP tools for browser automation, desktop interaction, shell execution, and remote file operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control a remote host, including browser sessions, shell processes, desktop input, and remote files.

Mitigation: Install only for trusted remote hosts and scope the MCP server with a bearer token, IP allowlists, host allowlists, and restrictive permissions.json policies.

Risk: Browser cookies and local storage persist across calls, which can expose sensitive user sessions if profiles are reused across users or tasks.

Mitigation: Reset or isolate browser profiles when switching users or tasks, and treat browser sessions as sensitive.

Risk: Large binary files or screenshots can cause excessive context usage if returned inline.

Mitigation: Use short-lived download URLs for screenshots and large file reads instead of pulling binary data directly into context.

## Reference(s):

- [Remote Claws homepage](https://github.com/wentbackward/remote-claws)
- [Remote Claws setup guide](https://github.com/wentbackward/remote-claws/blob/master/remote-claws-openclaw-setup-guide.md)
- [Remote Claws security documentation](https://github.com/wentbackward/remote-claws#security)
- [ClawHub skill page](https://clawhub.ai/wentbackward/skills/remote-claws)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown with inline tool calls and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or request short-lived download URLs for large files and screenshots rather than inline binary content.]

## Skill Version(s):

1.2.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
