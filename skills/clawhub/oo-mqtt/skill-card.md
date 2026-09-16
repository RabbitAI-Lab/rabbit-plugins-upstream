## Description:

Operates MQTT through an OOMOL-connected account to publish messages and receive bounded subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to interact with MQTT systems through the OOMOL connector, including publishing payloads and collecting newly received messages from bounded subscriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell installers that execute immediately under the user's account.

Mitigation: Review and trust OOMOL's installer channel before running setup; prefer a verified package or signed release when available.

Risk: Publishing MQTT messages changes external system state.

Mitigation: Confirm the exact topic, payload, encoding, and expected effect with the user before running write actions.

## Reference(s):

- [MQTT homepage](https://mqtt.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub MQTT skill page](https://clawhub.ai/oomol/skills/oo-mqtt)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses containing MQTT action data and an execution id.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
