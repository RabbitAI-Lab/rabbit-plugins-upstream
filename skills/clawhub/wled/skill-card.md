## Description: <br>
Control WLED LED controllers via HTTP API for power, brightness, RGB color, effects, palettes, presets, and device status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rowbotik](https://clawhub.ai/user/rowbotik) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and home-automation users use this skill to let an agent inspect and control WLED LED strips or matrices on the same network. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can immediately change the state of the targeted WLED lights if the host, hostname, alias, or WLED_HOST value points to a device. <br>
Mitigation: Confirm the target IP address, hostname, alias, or WLED_HOST value before running control commands. <br>


## Reference(s): <br>
- [WLED HTTP API Reference](references/api.md) <br>
- [ClawHub Wled skill page](https://clawhub.ai/rowbotik/skills/wled) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON configuration examples, and command output text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can issue HTTP requests to a selected WLED host and can read optional local device-alias configuration files.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
