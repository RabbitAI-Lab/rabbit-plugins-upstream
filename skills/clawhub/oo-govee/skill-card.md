## Description:

Operates Govee devices through an OOMOL-connected account, including listing devices, reading state, discovering scenes, and sending supported control capabilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect Govee device capabilities and state through an OOMOL-connected Govee account, then run supported Govee device actions through the oo CLI. Device-control actions should be confirmed with the user before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change connected Govee device state, while the available action list does not clearly tag the control action as write-capable.

Mitigation: Require explicit user confirmation of the exact device, payload, and expected effect before running any device-control command.

Risk: Users expecting read-only Govee access may install a skill that can also operate connected devices.

Mitigation: Review the skill before installation and restrict use to workflows where device-control behavior is acceptable.

## Reference(s):

- [ClawHub Govee Skill](https://clawhub.ai/oomol/skills/oo-govee)
- [Govee Homepage](https://www.govee.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data payload and execution metadata; device-control actions require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
