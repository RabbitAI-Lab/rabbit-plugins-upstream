## Description:

workled controls a connected workled device over MCP to show agent state on LEDs and configure touch-pad HID macros.

This skill is ready for commercial/non-commercial use.

## Publisher:

[git-hub-cloud](https://clawhub.ai/user/git-hub-cloud)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use workled to keep a physical LED indicator synchronized with agent states and to configure touch-pad macros for a paired workled device.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs persistent agent hooks or plugins across supported clients.

Mitigation: Install only for the client you actually use and review the exact hook or plugin paths before installation or uninstallation.

Risk: HID macros can type stored password values or trigger keyboard and mouse actions on a paired host.

Mitigation: Avoid configuring password or unlock macros unless you fully trust the device and host context, and review macros before saving them.

## Reference(s):

- [workled ClawHub Skill Page](https://clawhub.ai/git-hub-cloud/skills/workled)
- [workled MCP Device Setup](artifact/references/device_setup.md)
- [Macro Format Reference](artifact/references/macro_format.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, MCP tool calls, Guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce MCP tool-call instructions and JSON strings for LED effects or HID macros.]

## Skill Version(s):

0.1.4 (source: release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
