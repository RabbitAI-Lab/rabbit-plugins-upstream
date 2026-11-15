## Description:

Control Philips Hue lights/scenes via the OpenHue CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aperdigaokbk](https://clawhub.ai/user/aperdigaokbk)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect and control Philips Hue lights and scenes through the OpenHue CLI after local Hue Bridge setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to change physical Philips Hue lights and scenes.

Mitigation: Use it only when light control is intended, and review proposed OpenHue CLI write commands before execution.

Risk: OpenHue setup may require local Hue Bridge authorization and trust in the upstream CLI package.

Mitigation: Authorize the Hue Bridge only in the intended environment and review the upstream OpenHue CLI package before installation.

## Reference(s):

- [OpenHue CLI](https://www.openhue.io/cli)
- [ClawHub Skill Page](https://clawhub.ai/aperdigaokbk/skills/openhue)
- [Publisher Profile](https://clawhub.ai/user/aperdigaokbk)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include OpenHue CLI commands that read or change Philips Hue lights and scenes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
