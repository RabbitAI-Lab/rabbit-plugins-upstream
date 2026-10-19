## Description:

Guides users through connecting an OpenClaw agent to a Meshtastic radio node, configuring access, and verifying direct messages over the mesh.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fintlp](https://clawhub.ai/user/fintlp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to connect an agent to a reachable Meshtastic node for local, off-grid direct messaging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external messaging plugin can introduce supply-chain or access risks.

Mitigation: Review the plugin before use when stronger assurance is needed, and retain pairing or allowlist access unless broader access is intentional.

Risk: Group transmissions consume shared radio airtime and cannot be recalled.

Mitigation: Keep group transmission disabled unless its radio-use impact is acceptable.

Risk: Transmitting without the correct LoRa region setting can breach local radio requirements.

Mitigation: Set the node's region appropriately before enabling transmission.

## Reference(s):

- [Meshtastic Connect on ClawHub](https://clawhub.ai/fintlp/skills/meshtastic-connect)
- [Meshtastic plugin support issues](https://github.com/fintlp/openclaw-meshtastic/issues)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Installation, access-policy, and connection-verification steps]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
