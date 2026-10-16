## Description:

به کاربران در ثبت‌نام PowPow، فعال‌سازی اشتراک با علی‌پی یا PayPal و دریافت لینک ورود در گفتگو کمک می‌کند.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users use this skill to create an account, resolve signup issues, activate a subscription, and obtain a login link. The user supplies an email verification code and completes payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification codes, passwords, login links, and temporary account state are sensitive.

Mitigation: Keep them private and run cleanup after signup to remove temporary state.

Risk: Subscription payment involves a financial transaction.

Mitigation: Review the plan and pay only on the official Alipay or PayPal page; do not give the agent payment credentials.

## Reference(s):

- [PowPow skill release on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-fa)
- [PowPow website](https://global.powpow.online)
- [Agent workflow](references/agent-flow.md)
- [Registration workflow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown chat guidance with registration, payment, and login links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can share bundled screenshots; the user retrieves an email code and completes payment on the official payment page.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
