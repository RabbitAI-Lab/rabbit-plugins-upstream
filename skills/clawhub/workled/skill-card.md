## Description:

Controls a workled device over MCP so an agent can update LED state indicators and configure touch-pad HID macros.

This skill is ready for commercial/non-commercial use.

## Publisher:

[git-hub-cloud](https://clawhub.ai/user/git-hub-cloud)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect supported agent clients to a workled device, show agent lifecycle states through LEDs, and configure touch-pad macros for local workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer behavior can add persistent hooks or plugins across multiple agent clients.

Mitigation: Install a single explicit client target, review the files the installer will change, and uninstall the same explicit target when removing the skill.

Risk: The configured MCP endpoint may point to a placeholder or an unintended workled device.

Mitigation: Set WORKLED_MCP_URL to the intended device endpoint before installation and verify status after configuration.

Risk: Touch-pad HID macros can type sensitive content or trigger workstation actions.

Mitigation: Avoid password or workstation-unlock macros unless the user fully understands the HID behavior and local security impact.

## Reference(s):

- [ClawHub workled skill page](https://clawhub.ai/git-hub-cloud/skills/workled)
- [workled repository](https://github.com/git-hub-cloud/workled)
- [workled issues](https://github.com/git-hub-cloud/workled/issues)
- [workled MCP Device Setup](references/device_setup.md)
- [Macro Format Reference](references/macro_format.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown instructions with inline shell commands, JSON examples, and MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in persistent client hook or plugin configuration when installation commands are followed.]

## Skill Version(s):

0.1.13 (source: server release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
