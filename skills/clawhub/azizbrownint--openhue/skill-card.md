## Description:

Control Philips Hue lights and scenes via the OpenHue CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for OpenHue CLI commands that list and control Philips Hue lights, rooms, and scenes through a local Hue Bridge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OpenHue CLI commands can change real lights, rooms, and scenes on the user's local network.

Mitigation: Review generated commands before execution and confirm the intended room, light, scene, brightness, color, and on/off state.

Risk: The CLI requires access to a local Hue Bridge and first-run pairing.

Mitigation: Pair only with the intended Hue Bridge and install the Homebrew tap/package only after reviewing its source.

## Reference(s):

- [OpenHue CLI documentation](https://www.openhue.io/cli)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/openhue)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands assume the OpenHue CLI is installed, a Hue Bridge is reachable on the local network, and target lights, rooms, or scenes exist.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
