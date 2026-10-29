## Description:

Connect an OpenClaw gateway to a Meshtastic LoRa mesh node in minutes — install the maintained channel plugin (@fintlp/openclaw-meshtastic), run the probe-first setup wizard, and verify the first DM over radio. Use when a user wants their AI agent reachable via Meshtastic, off-grid messaging, or LoRa mesh comms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fintlp](https://clawhub.ai/user/fintlp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw gateway operators use this skill to connect an agent to a Meshtastic LoRa mesh, configure safe messaging access, and verify radio-based direct messaging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party channel plugin introduces a dependency that should be reviewed.

Mitigation: Review the plugin before installation.

Risk: A local radio connection does not establish that AI processing stays local.

Mitigation: Check where the gateway sends prompts and messages for AI processing.

Risk: Allowing unpaired contacts or broadcasts can permit unwanted access or radio transmissions.

Mitigation: Keep contact pairing enabled and broadcasts disabled unless deliberately needed.

## Reference(s):

- [Meshtastic Connect on ClawHub](https://clawhub.ai/fintlp/skills/meshtastic-connect)
- [Plugin issues and support](https://github.com/fintlp/openclaw-meshtastic/issues)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
