## Description:

Give your AI agent an identity it owns - a real email inbox, a US phone number for SMS and voice, and an encrypted credential vault.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diyanbogdanov](https://clawhub.ai/user/diyanbogdanov)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill to provision and operate an Anima-managed agent identity for email, phone, SMS, voice, webhooks, and credential-vault workflows under human verification and plan controls.

### Deployment Geography for Use:

Global; phone-number examples and claims are scoped to US numbers.

## Known Risks and Mitigations:

Risk: The skill gives an agent an external communication identity and broad outbound messaging capability.

Mitigation: Install it only for agents that should communicate externally, and require explicit approval before third-party signups, 2FA handling, SMS, or voice calls.

Risk: Anima API key exposure could let another party impersonate the agent identity.

Mitigation: Keep the API key out of general chat and broad memory, store it as a secret, and send it only to https://api.useanima.sh endpoints.

Risk: Relaying verification OTPs through the agent can weaken human control over activation.

Mitigation: Prefer console-based human verification and plan management when possible.

Risk: Phone, voice, credential-vault, and webhook workflows can affect real users and external services.

Mitigation: Use human approval, consent checks, and plan controls before enabling or exercising those capabilities.

## Reference(s):

- [Anima homepage](https://useanima.sh)
- [Anima documentation](https://docs.useanima.sh)
- [Anima agent documentation feed](https://docs.useanima.sh/llms.txt)
- [ClawHub release page](https://clawhub.ai/diyanbogdanov/skills/anima-identity)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include API request examples for provisioning identity, email, phone, voice, vault, and webhook capabilities.]

## Skill Version(s):

1.0.1 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
