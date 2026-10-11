## Description:

Helps users register for PowPow, verify their email, activate a membership through Alipay, and obtain one-click login links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can have an agent guide or assist with account registration, email verification, membership payment, login, and common activation issues. The user supplies a verification code and completes payment on the payment page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration handles an email verification code and a chosen or generated password.

Mitigation: Share credentials only when you intend to register with PowPow; use the verification code for signup and avoid placing passwords in command arguments or saved files.

Risk: The agent creates payment orders and opens a payment page.

Mitigation: Confirm the payment page yourself and pay only on the official Alipay or PowPow page; do not give the agent control of your payment account.

Risk: A login token is temporarily stored locally during registration and activation.

Mitigation: Run the cleanup step when finished to remove temporary session data.

## Reference(s):

- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-th)
- [PowPow website](https://global.powpow.online)
- [Agent workflow](references/agent-flow.md)
- [Registration guidance](references/registration-flow.md)
- [Payment and activation guidance](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Links]

**Output Format:** [Conversational text with links and optional product screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides registration and payment status updates and one-click login links.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
