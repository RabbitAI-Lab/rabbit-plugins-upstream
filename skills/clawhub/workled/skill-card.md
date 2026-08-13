## Description:

workled lets an agent control a workled device over MCP to show agent state with LEDs and configure touch-pad HID macros.

This skill is ready for commercial/non-commercial use.

## Publisher:

[git-hub-cloud](https://clawhub.ai/user/git-hub-cloud)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use workled to connect a local workled device to supported agent clients, keep a visible LED state indicator in sync with agent activity, and configure touch-pad macros.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can add persistent hooks or plugin entries for agent clients.

Mitigation: Install only for the client you use, avoid all-client installation unless broad persistent hooks are intended, and review generated agent configuration changes.

Risk: HID macros can type text, passwords, and unlock sequences into a workstation.

Mitigation: Treat macros as privileged workstation automation and do not store real passwords or unlock sequences unless the device and workflow are fully trusted.

Risk: Device provisioning places the workled hardware on a local Wi-Fi network.

Mitigation: Prefer a guest or IoT Wi-Fi network for provisioning and operation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/git-hub-cloud/skills/workled)
- [Device setup guide](device_setup.md)
- [Macro format reference](macro_format.md)
- [Project repository listed in skill documentation](https://github.com/git-hub-cloud/workled)
- [Issue tracker listed in skill documentation](https://github.com/git-hub-cloud/workled/issues)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, MCP API calls, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON examples, shell commands, and MCP tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update client configuration during install; touch-pad macro definitions are JSON arrays.]

## Skill Version(s):

0.1.8 (source: server release evidence and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
