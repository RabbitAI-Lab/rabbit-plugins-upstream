## Description:

Guides users through PowPow account registration, email verification, subscription activation via Alipay or PayPal, and one-click login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users use this skill to register an account, verify their email, select and pay for a subscription through the payment provider, and receive a login link. The agent can troubleshoot signup and activation or provide manual guidance when its Node.js workflow is unavailable; it does not publish posts or create digital humans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials and verification codes may be exposed during assisted signup.

Mitigation: Do not share Alipay or PayPal credentials in chat; use the official checkout and handle account passwords and email verification codes carefully.

Risk: Generated login links contain reusable session tokens, and local signup state may remain on a shared machine.

Mitigation: Treat login links as session-sensitive, run cleanup when finished, and prefer manual web registration and payment on shared or managed machines.

Risk: Subscription setup can lead to an unintended recurring payment.

Mitigation: Review the plan and payment terms at the provider checkout before authorizing payment.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [PowPow subscription](https://global.powpow.online/subscription)
- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-hi)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational guidance with registration, checkout, and login links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account and subscription status updates; requires Node.js 18 or newer for assisted operation, with manual guidance otherwise.]

## Skill Version(s):

2.1.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
