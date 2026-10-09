## Description:

Helps users register a PowPow account, activate a membership through Alipay, and obtain a one-click login link within a guided conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can use this skill to set up an account, resolve registration issues, purchase an Alipay membership, and receive a login link. The user supplies an email verification code and completes payment at the cashier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The registration flow handles passwords and email verification codes.

Mitigation: Use a trusted, single-user agent environment and review how credentials are handled before installation.

Risk: A live login token is temporarily stored locally and can grant account access.

Mitigation: Avoid shared agent environments and run cleanup as soon as the flow completes.

Risk: The agent creates and tracks Alipay payment orders.

Mitigation: Check the payment page and order details before paying; complete payment yourself at the cashier.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [PowPow registration flow](artifact/references/registration-flow.md)
- [PowPow payment and activation](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text and Markdown with inline shell commands and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can provide relevant product screenshots; requires Node.js 18+ for assisted registration and otherwise gives guidance only.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
