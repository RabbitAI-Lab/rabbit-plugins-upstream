## Description:

Helps people register for PowPow, verify their email, activate a subscription through Alipay or PayPal, and sign in through a one-click link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can use this Swahili-language assistant to learn about the service, register an account, complete email verification, choose a subscription payment route, and resolve common registration or activation issues. The user completes payment at the cashier; the agent does not pay on their behalf.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials, email verification codes, and one-click sign-in links can grant access to the user's account if disclosed.

Mitigation: Keep passwords and sign-in links private, enter verification codes only for PowPow registration, and clear temporary registration state when finished.

Risk: A substituted or misleading cashier page could result in payment to the wrong destination.

Mitigation: Confirm the cashier destination before paying, and complete payment personally through the expected Alipay or PayPal flow.

## Reference(s):

- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-sw)
- [PowPow website](https://global.powpow.online)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)
- [Agent flow](artifact/references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Conversational Markdown with sign-in and cashier links, images, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides registration progress and troubleshooting guidance; Node.js 18 or newer is needed for automated assistance, with manual guidance otherwise.]

## Skill Version(s):

2.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
