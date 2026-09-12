## Description:

Give your AI agent an identity it owns - a real email inbox, a US phone number for SMS and voice, and an encrypted credential vault.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anima](https://clawhub.ai/user/anima)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to provision and manage an agent-controlled Anima email identity, with human verification before broader communication capabilities. It also guides agents through plan-gated phone, SMS, voice, vault, webhook, and account-management workflows.

### Deployment Geography for Use:

Global; phone examples and provisioning are described for US numbers.

## Known Risks and Mitigations:

Risk: The skill enables agent-controlled real-world communications through email, SMS, and voice.

Mitigation: Require explicit human approval before sending messages beyond the human verifier, placing calls, or configuring webhooks.

Risk: The skill involves an Anima API key that can impersonate the agent identity if exposed.

Mitigation: Store the API key only in a secret manager or protected environment variable, and rotate or revoke it if exposed.

Risk: Agents may use received verification codes or account access to create or control third-party accounts.

Mitigation: Require human approval before creating third-party accounts or using received verification codes.

## Reference(s):

- [Anima documentation](https://docs.useanima.sh)
- [Anima homepage](https://useanima.sh)
- [ClawHub skill page](https://clawhub.ai/anima/skills/anima-identity)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON examples and bash curl commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes API endpoint examples, authentication handling, verification steps, capability limits, and human approval guidance.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
