## Description:

Helps people register a PowPow account, verify their email, activate an Alipay subscription, and access the service through a one-click login link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

People signing up for PowPow use this skill to complete email verification, account creation, subscription activation, and login with agent assistance. Users provide their verification code and complete payment themselves on the payment page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account creation handles an email verification code and a password.

Mitigation: Share the verification code only for registration, avoid repeating the password, and keep account credentials private.

Risk: A temporary session token and account details may remain after registration.

Mitigation: Run the skill's cleanup step when finished to remove temporary session state.

Risk: Subscription setup creates a payment order.

Mitigation: Complete payment only on the official payment page; do not provide payment credentials to the agent.

## Reference(s):

- [PowPow ClawHub listing](https://clawhub.ai/durenzidu/skills/powpow-register-bn)
- [PowPow website](https://global.powpow.online)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational guidance with login and payment links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account summary and subscription expiry after activation; no payment credentials requested]

## Skill Version(s):

2.0.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
