## Description:

Helps users register a PowPow account in conversation, verify their email, and receive a one-click login link, with optional subscription guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

People signing up for PowPow use this skill to complete registration and email verification through an agent, then access their account through a login link. It can also guide an optional Alipay or PayPal subscription when requested or required for access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration sends personal account details to PowPow.

Mitigation: Get the user's consent, collect only needed details, and send them only to PowPow.

Risk: One-click login links contain live session tokens and can grant account access.

Mitigation: Treat links as password-equivalent secrets, do not share links or chat transcripts, and run cleanup after the flow.

Risk: Optional subscriptions may incur charges or recurring payments.

Mitigation: Explain the chosen payment terms and let the user complete checkout themselves.

## Reference(s):

- [PowPow official site](https://global.powpow.online)
- [PowPow Register on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with account details and a one-click login link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include optional subscription instructions; login links grant access to the account.]

## Skill Version(s):

2.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
