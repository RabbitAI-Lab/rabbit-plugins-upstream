## Description:

Guides users through PowPow account registration, email verification, Alipay or PayPal subscription activation, and one-click login within a conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Prospective PowPow users use this skill to register an account, resolve registration issues, and activate a subscription. The agent can prepare registration and payment orders, while the user supplies an email verification code and completes payment on the payment page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated login links contain session access and may expose the account if shared.

Mitigation: Keep login links private and open them only on a trusted device.

Risk: The registration flow retains session state locally while creating an account and subscription order.

Mitigation: Run on a trusted machine and use the cleanup command when finished; choose manual web registration if agent-managed session state is not acceptable.

Risk: The agent can create subscription orders on the user's behalf.

Mitigation: Confirm the chosen payment method and plan before creating an order, and complete payment yourself on the payment page.

## Reference(s):

- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-bn)
- [PowPow website](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with links and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides registration progress, payment-page links, and session-bearing login links; requires Node.js 18+ for agent-run registration, with a manual web-guidance fallback.]

## Skill Version(s):

2.1.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
