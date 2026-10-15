## Description:

Guides users through PowPow account registration, email verification, Alipay or PayPal subscription activation, and one-click login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users and their agents use this skill to create an account, troubleshoot registration, and activate a subscription through Alipay or PayPal. Users provide an email verification code and complete payment themselves; posting content and creating digital humans are outside its scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account details, verification codes, and session tokens are handled during registration.

Mitigation: Review before installing, use only on a trusted single-user machine, and complete cleanup after use.

Risk: Generated login URLs carry a session token and could grant account access if shared.

Mitigation: Do not share generated login URLs; avoid use where browser launching is not well controlled.

Risk: Subscription orders and temporary local files involve sensitive account and payment context.

Mitigation: Complete payment yourself at the payment provider and avoid use where local temporary directories are not well controlled.

## Reference(s):

- [PowPow registration skill on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-or)
- [PowPow website](https://global.powpow.online)
- [Registration flow](references/registration-flow.md)
- [Agent flow](references/agent-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Links]

**Output Format:** [Markdown text with commands and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or newer for assisted registration; otherwise provides manual guidance.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
