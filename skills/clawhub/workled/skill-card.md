## Description:

workled helps agents control a workled MCP device by reporting agent state to an LED indicator and configuring brightness, effects, and touch-pad HID macros.

This skill is ready for commercial/non-commercial use.

## Publisher:

[git-hub-cloud](https://clawhub.ai/user/git-hub-cloud)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when a workled MCP device is connected and they want agent state reflected on the device LED or want to configure touch-pad HID macros.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can configure HID macros, including password or unlock sequences, that may type into the active computer session.

Mitigation: Avoid password and unlock macros unless explicitly required and reviewed; keep macro configuration limited to trusted workflows.

Risk: The device MCP endpoint is documented as plain HTTP on a local network.

Mitigation: Use the skill only with a trusted workled device on a trusted local network and verify the configured device URL before use.

Risk: The installer can add hooks or plugins for multiple local agent clients.

Mitigation: Install only the client integration actually needed and review generated client configuration before relying on automatic state updates.

## Reference(s):

- [workled MCP Device Setup](artifact/references/device_setup.md)
- [Macro Format Reference](artifact/references/macro_format.md)
- [Source Repository](https://github.com/git-hub-cloud/workled)
- [ClawHub Skill Page](https://clawhub.ai/git-hub-cloud/skills/workled)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, MCP tool calls, JSON]

**Output Format:** [Markdown guidance with inline commands, configuration snippets, MCP tool calls, and diagnostic JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May configure local client hooks or plugins and send MCP requests to a workled device on the local network.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
