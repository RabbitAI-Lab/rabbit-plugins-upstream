## Description:

Full control of a remote machine via Remote Claws MCP: screenshots, mouse/keyboard, browser automation, run commands, read/write files on the remote host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wentbackward](https://clawhub.ai/user/wentbackward)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent control an intended remote desktop host through Remote Claws MCP while the agent itself remains sandboxed. It supports remote browser work, desktop interaction, command execution, and remote file handling when allowed by server policy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote-control access can run commands, control a browser, and read or change files on the remote host.

Mitigation: Install it only for a machine the agent is intended to control, require a strong bearer token, and use narrow IP, host, and per-action allowlists.

Risk: Broad file writes, file deletion, command execution, or authenticated browser access can create higher operational impact if enabled unnecessarily.

Mitigation: Avoid enabling those permissions unless the task requires them, and keep server policy as narrow as practical.

Risk: Confusing remote tools with local gateway tools can cause actions to run in the wrong environment.

Mitigation: Use only remote_* tools for remote-host actions, screenshot before desktop interaction, and treat permission-denied responses as final unless the user changes the policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wentbackward/skills/remote-claws)
- [Remote Claws homepage](https://github.com/wentbackward/remote-claws)
- [Remote Claws OpenClaw setup guide](https://github.com/wentbackward/remote-claws/blob/master/remote-claws-openclaw-setup-guide.md)
- [Remote Claws security documentation](https://github.com/wentbackward/remote-claws#security)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown and tool-call guidance with command, configuration, browser, desktop, and file operation details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference screenshots, short-lived file URLs, base64 file chunks, process IDs, and permission-denied results returned by the remote server.]

## Skill Version(s):

1.2.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
