## Description:

MUST call set_agent_state via MCP on each agent state transition (thinking, idle, waiting, error). Use when connected to a workled device via MCP, controlling the agents state indicator, or configuring HID macros.

This skill is ready for commercial/non-commercial use.

## Publisher:

[git-hub-cloud](https://clawhub.ai/user/git-hub-cloud)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to control a workled device through MCP, including agent state LEDs, brightness, effects, and touch-pad HID macros. It also provides setup guidance and installer support for multiple agent clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs persistent client hooks or plugins that can control a local workled device.

Mitigation: Install only for intended clients and review the installer target before running it.

Risk: HID macros can type credentials or other sensitive text.

Mitigation: Avoid storing OS, account, or other high-value passwords in workled HID macros.

Risk: The uninstall helper is aggressive even though it is intended for workled-owned files.

Mitigation: Review uninstall targets and keep backups of client configuration before uninstalling.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/git-hub-cloud/skills/workled)
- [workled MCP Device Setup](artifact/references/device_setup.md)
- [Macro Format Reference](artifact/references/macro_format.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline tool calls, shell commands, JSON configuration, and macro JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Controls a local MCP-connected workled device and may install persistent client hooks or plugins when the user runs the installer.]

## Skill Version(s):

0.1.14 (source: server release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
