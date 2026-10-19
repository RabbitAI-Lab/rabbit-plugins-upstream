## Description:

Guides developers through connecting an OpenClaw gateway to a MeshCore LoRa node, configuring the channel plugin, and verifying a direct message over radio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fintlp](https://clawhub.ai/user/fintlp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and gateway operators use this skill to connect an OpenClaw agent to a local MeshCore radio node and confirm that it can receive and reply to direct messages.

### Deployment Geography for Use:

Global (subject to local radio frequency regulations)

## Known Risks and Mitigations:

Risk: The recommended channel plugin runs code and handles mesh messages.

Mitigation: Confirm the plugin publisher is trusted and review the plugin before installing it.

Risk: An overly permissive direct-message policy can expose the agent to unapproved senders.

Mitigation: Keep the pairing policy unless wider access is intentionally required.

Risk: Using an incorrect radio band may violate local rules.

Mitigation: Set the node's region and band for the deployment locale before use.

## Reference(s):

- [MeshCore Connect on ClawHub](https://clawhub.ai/fintlp/skills/meshcore-connect)
- [MeshCore channel plugin support](https://github.com/fintlp/openclaw-meshcore/issues)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes connection checks and direct-message verification steps.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
