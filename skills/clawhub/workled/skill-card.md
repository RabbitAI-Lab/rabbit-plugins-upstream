## Description:

workled helps agents control a workled MCP device by updating LED state on agent transitions and configuring touch-pad HID macros.

This skill is ready for commercial/non-commercial use.

## Publisher:

[git-hub-cloud](https://clawhub.ai/user/git-hub-cloud)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use workled to connect supported AI coding clients to a workled device, keep a physical LED indicator synchronized with agent state, and configure touch-pad macros.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs persistent hooks into agent clients and can modify client configuration.

Mitigation: Review the exact target client and installer changes before running the installer, and uninstall unused hooks.

Risk: HID macros can type passwords, unlock sequences, or other sensitive input on a paired computer.

Mitigation: Avoid password or unlock macros unless the physical-access and credential risks are accepted; inspect each macro JSON before saving it.

Risk: A placeholder or incorrect MCP URL can point hooks at the wrong or unreachable device endpoint.

Mitigation: Configure a real device hostname or static IP and verify reachability with the status command before relying on the LED state indicator.

## Reference(s):

- [workled MCP Device Setup](references/device_setup.md)
- [Macro Format Reference](references/macro_format.md)
- [Video Demo](https://www.bilibili.com/video/BV1FK4k6WEKe)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown instructions with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes MCP tool-call arguments, client installer commands, and macro JSON examples.]

## Skill Version(s):

0.1.15 (source: server release metadata and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
