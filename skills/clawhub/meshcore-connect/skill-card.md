## Description:

Connect an OpenClaw gateway to a MeshCore LoRa mesh node in minutes — install the maintained channel plugin (@fintlp/openclaw-meshcore), run the probe-first setup wizard, and verify the first DM over radio. Use when a user wants their AI agent reachable via MeshCore, off-grid messaging, or LoRa mesh comms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fintlp](https://clawhub.ai/user/fintlp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and MeshCore users use this skill to connect an OpenClaw gateway to a reachable MeshCore node and verify off-grid direct messaging. It guides plugin installation, probe-first setup, configuration, and safe peer approval.

### Deployment Geography for Use:

Global, where MeshCore radio bands and local regulations permit operation.

## Known Risks and Mitigations:

Risk: The third-party channel plugin's safeguards are not independently verified, and approved contacts may be able to use the agent's available tools.

Mitigation: Trust the plugin before installing, keep pairing enabled, and approve only peers trusted with the agent's available tools.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/fintlp/skills/meshcore-connect)
- [Plugin support issues](https://github.com/fintlp/openclaw-meshcore/issues)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup instructions require a reachable MeshCore companion node and a radio band permitted for the user's location.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
