## Description:

Speak text aloud through a Linux device's physical speaker using OpenClaw Talk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frussen-robotics](https://clawhub.ai/user/frussen-robotics)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when an assistant should speak selected text aloud through a Linux device speaker using the configured OpenClaw Talk provider.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text passed to the skill is sent through the configured OpenClaw Talk provider path.

Mitigation: Do not use it for secrets, credentials, private prompts, or sensitive content unless that provider path is trusted.

Risk: The skill runs local commands and plays audio on the device speaker.

Mitigation: Install it only on Linux devices where OpenClaw, Python 3, and ALSA playback are expected and where audible output is appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/frussen-robotics/skills/speak)
- [Publisher profile](https://clawhub.ai/user/frussen-robotics)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Text guidance with shell command invocation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces spoken WAV audio through ALSA via the configured OpenClaw Talk provider.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
