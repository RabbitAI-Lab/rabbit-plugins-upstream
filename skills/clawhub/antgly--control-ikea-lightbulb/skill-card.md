## Description:

Control IKEA/TP-Link Kasa smart bulbs (set on/off, brightness, and color). Use when you want to programmatically control a local smart bulb by IP on the LAN.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antgly](https://clawhub.ai/user/antgly)

### License/Terms of Use:


## Use Case:

Developers and smart-home users use this skill to control a local Kasa-compatible smart bulb by IP address, including power, brightness, color, and short light-show sequences on the LAN.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can visibly change the wrong local smart bulb if the provided IP address points to an unintended device.

Mitigation: Confirm the target IP belongs to the bulb you intend to control before running commands.

Risk: Dependency resolution may vary because the artifact does not include a reviewed lockfile or pinned exact dependency versions.

Mitigation: Use a reviewed lockfile or pinned dependency set when reproducible installation is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/antgly/skills/control-ikea-lightbulb)
- [Publisher profile](https://clawhub.ai/user/antgly)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and Python script behavior descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Controls are executed against a user-specified LAN IP address and may visibly change the target bulb.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; pyproject.toml declares 0.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
