## Description:

Helps deploy a Zalo Bot webhook bridge to receive messages in OpenClaw, configure HTTPS and bot credentials, and register the webhook with Zalo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thinhbuiii](https://clawhub.ai/user/thinhbuiii)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to deploy a local Zalo Bot webhook receiver for OpenClaw, connect it through a public HTTPS endpoint, and register and test the webhook.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The sample webhook accepts requests with no secret header even when a secret is configured.

Mitigation: Require the configured secret on every webhook request and reject missing or incorrect headers before processing messages.

Risk: Full webhook payloads are stored in local logs and the last-event file.

Mitigation: Restrict file permissions and set retention or redact sensitive message content.

Risk: Deployment registers a webhook and enables a persistent service using a bot token.

Mitigation: Use only a bot token you control and review the service and webhook registration before enabling them.

## Reference(s):

- [ENT Zalo Bridge release on ClawHub](https://clawhub.ai/thinhbuiii/skills/ent-zalo-bridge)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with JavaScript, shell, and configuration code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes deployment and webhook testing steps.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
