## Description:

Helps users register for PowPow, activate membership through Alipay or PayPal, and access their account through a one-click login link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can ask an agent to guide or complete account registration, email verification, and membership activation. Users supply their registration details and verification code and make any payment themselves at the payment provider's checkout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent handles account credentials and an email verification code during signup.

Mitigation: Share these only when you trust the agent and avoid exposing them in shared chats or logs.

Risk: Payment links may lead to an unintended checkout.

Mitigation: Check the payment page and amount before paying; enter payment details only at the provider's checkout.

Risk: A one-click login link or temporary session token could allow account access if disclosed.

Mitigation: Treat login links as secrets, do not forward them, and run cleanup after registration.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [PowPow membership](https://global.powpow.online/subscription)
- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-th)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with payment and login links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include product screenshots and account setup instructions.]

## Skill Version(s):

2.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
