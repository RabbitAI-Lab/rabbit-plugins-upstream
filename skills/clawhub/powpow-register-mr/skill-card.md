## Description:

Guides users through PowPow account registration, email verification, Alipay or PayPal activation, and one-click sign-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users use this skill to create and activate an account with agent assistance, or to follow a guided manual registration flow when automation is unavailable. The user supplies their email verification code and completes payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent handles account credentials and a temporary session token; sharing one-click sign-in links could expose the account.

Mitigation: Do not share one-click links or put passwords in command-line arguments; run cleanup when the registration flow ends.

Risk: Creating or reopening Alipay or PayPal checkout orders could result in unintended payment or subscription activity.

Mitigation: Confirm with the user before creating or recreating an order, check that checkout follows the official PowPow/Alipay/PayPal path, and leave payment to the user.

Risk: Users may not want an agent involved in their verification or payment flow.

Mitigation: Offer the manual PowPow registration and payment pages as an alternative.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [PowPow ClawHub listing](https://clawhub.ai/durenzidu/skills/powpow-register-mr)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Links]

**Output Format:** [Conversational text and Markdown with checkout and sign-in links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-assisted flow requires Node.js 18 or newer; manual web guidance is available otherwise.]

## Skill Version(s):

2.1.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
