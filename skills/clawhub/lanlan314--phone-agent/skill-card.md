## Description:

手机操控 lets an agent use USB ADB to inspect an Android device screen, analyze UI elements, and perform taps, swipes, text input, key presses, app launches, and app stops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lanlan314](https://clawhub.ai/user/lanlan314)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to control a USB-connected Android phone through ADB for app navigation, UI inspection, coordinate-based actions, and simple messaging workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad live ADB control can operate the attached Android phone and interact with sensitive apps or accounts.

Mitigation: Confirm the attached device before use and avoid banking, payment, OTP, private-message, or sensitive account screens.

Risk: Screenshots and UI XML dumps can capture sensitive on-screen content and remain in temporary files.

Mitigation: Manually remove temporary screenshot and XML files when sensitive data may have been captured.

Risk: USB debugging grants elevated control over the connected device.

Mitigation: Use the skill only with devices intentionally authorized for ADB control and disable or revoke debugging access after the workflow.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with shell command examples; script output is plain text status, coordinates, paths, and temporary PNG/XML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ADB access to an authorized Android device and may create temporary screenshot and UI XML files.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
