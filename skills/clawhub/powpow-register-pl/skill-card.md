## Description:

Guides PowPow users through account registration, email verification, subscription activation via Alipay or PayPal, and one-click sign-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Prospective PowPow users use this skill to create and activate an account with agent assistance, or to troubleshoot registration and subscription issues. The user retrieves the email code and completes payment in the official checkout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent handles registration details, a one-time email code, a password, and a temporary session token.

Mitigation: Share these only as needed for registration, keep the password out of command arguments, and ask the agent to run cleanup when finished.

Risk: Subscription checkout involves a payment order; PayPal subscriptions renew automatically.

Mitigation: Review the plan and renewal terms before approving payment, and complete payment yourself in the official Alipay or PayPal checkout.

## Reference(s):

- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-pl)
- [PowPow official website](https://global.powpow.online)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Conversational text with sign-in and checkout links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Falls back to browser-only guidance when Node.js 18 or later is unavailable.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
