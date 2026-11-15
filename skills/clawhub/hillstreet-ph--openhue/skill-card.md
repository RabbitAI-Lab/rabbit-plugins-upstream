## Description:

Control Philips Hue lights and scenes via the OpenHue CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to control Philips Hue lights, rooms, and scenes through OpenHue CLI, including power, brightness, color, temperature, and scene selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A command may change the wrong light, room, or scene, or apply a setting broader than intended.

Mitigation: Confirm the target device or room and the requested setting before issuing a control command.

## Reference(s):

- [OpenHue CLI documentation](https://www.openhue.io/cli)
- [ClawHub OpenHue skill page](https://clawhub.ai/hillstreet-ph/skills/openhue)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require the OpenHue CLI and a Hue Bridge reachable on the local network; initial pairing requires pressing the bridge button.]

## Skill Version(s):

1.0.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
