## Description:

Helps users register for PowPow, activate an Alipay or PayPal subscription, and access their account through one-click sign-in links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can ask an agent to guide or perform account registration, email verification, and subscription setup while they complete verification and payment themselves. The skill also helps troubleshoot signup and activation issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One-click login links contain live session tokens, and temporary account state may remain on the machine.

Mitigation: Keep sign-in links private and run the cleanup command when finished; choose manual registration if local token storage is unacceptable.

Risk: Delegated signup handles an email verification code, a password, and an optional profile image.

Mitigation: Only provide these details if comfortable with agent-assisted registration; otherwise use the manual guidance mode.

Risk: Subscription setup opens payment checkout pages; PayPal subscriptions may renew automatically.

Mitigation: Review the official checkout terms and complete payment yourself; do not give the agent payment credentials.

## Reference(s):

- [PowPow skill release on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-tr)
- [PowPow official site](https://global.powpow.online)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)
- [Agent flow](references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Markdown with sign-in and checkout links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guided mode is available when Node.js 18 or newer is unavailable.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
