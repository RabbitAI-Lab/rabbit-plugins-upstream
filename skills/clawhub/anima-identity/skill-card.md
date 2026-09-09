## Description:

Anima Identity gives an AI agent a real email inbox, a US phone number for SMS and voice, and an encrypted credential vault, with human verification and plan controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diyanbogdanov](https://clawhub.ai/user/diyanbogdanov)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to provision and operate an agent-owned communications identity for email, SMS, voice calls, webhook notifications, and credential storage under human verification and plan controls.

### Deployment Geography for Use:

Global, with phone provisioning described for US numbers.

## Known Risks and Mitigations:

Risk: The skill can send real email, SMS, and voice calls, creating consent and compliance risk for high-impact external actions.

Mitigation: Use it only after the operator confirms intended recipients, phone consent, and applicable calling or messaging obligations before each external send or call.

Risk: An Anima API key leak can let another party impersonate the agent identity.

Mitigation: Store the API key only in a protected environment variable or secrets manager and never send it to any host other than api.useanima.sh.

Risk: The signup and verification flow can expose a human email address, OTPs, credentials, and vault-related secrets to the service or to agent memory.

Mitigation: Disclose the human email address only when intended, avoid retaining OTPs or secrets in general memory, and keep vault or master-key actions under human approval.

Risk: Webhook subscriptions can expose organization-wide message, phone, call, and vault events if endpoints are misconfigured.

Mitigation: Use HTTPS endpoints controlled by the operator, verify event destinations before enabling subscriptions, and limit subscribed events to those required for the workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/diyanbogdanov/skills/anima-identity)
- [Anima Documentation](https://docs.useanima.sh)
- [Anima Homepage](https://useanima.sh)
- [Anima API Base](https://api.useanima.sh)
- [Anima Agent Skill Manifest](https://useanima.sh/skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with curl commands and JSON request/response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce credentials, message metadata, webhook configuration, and call transcript retrieval guidance for real external communications.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
