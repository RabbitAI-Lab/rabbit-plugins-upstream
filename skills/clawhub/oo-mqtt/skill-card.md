## Description:

Operates MQTT through OOMOL's oo CLI connector for publishing UTF-8 or base64 messages and receiving bounded subscription messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to interact with MQTT through an OOMOL-connected account, including publishing messages and receiving newly published messages from bounded subscriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing to the wrong MQTT topic, payload, encoding, or environment can change downstream system behavior.

Mitigation: Confirm the exact publish_message topic, payload, encoding, and target environment with the user before execution.

Risk: Setup, authentication, or connection commands can initiate account or connector changes when run unnecessarily.

Mitigation: Run CLI install, login, or MQTT connection steps only after a command fails with the matching setup, authentication, or connection error.

## Reference(s):

- [MQTT homepage](https://mqtt.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mqtt)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before building action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
