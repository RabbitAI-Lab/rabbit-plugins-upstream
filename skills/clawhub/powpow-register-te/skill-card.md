## Description:

Helps users register a PowPow account, activate an Alipay or PayPal subscription, troubleshoot onboarding, and access their account through one-click login links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users and their agents use this skill to complete account registration and subscription activation in conversation. The user supplies an email verification code and completes payment on the payment page; creating posts or digital humans is outside this skill's scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent handles account passwords and session tokens during registration.

Mitigation: Run only in a trusted, private environment; keep passwords out of chat logs and shared terminals, and clean up temporary state when finished.

Risk: One-click login links embed account tokens and can grant access if shared.

Mitigation: Treat login links as passwords; send them only to the intended user and avoid storing or forwarding them.

Risk: The agent creates subscription orders and handles payment state.

Mitigation: Confirm the selected provider and plan with the user; have the user pay on the official payment page, or use the website manually if agent handling is unwanted.

## Reference(s):

- [PowPow Register ClawHub listing](https://clawhub.ai/durenzidu/skills/powpow-register-te)
- [PowPow website](https://global.powpow.online)
- [Agent flow](artifact/references/agent-flow.md)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Links, Shell commands]

**Output Format:** [Markdown with account and payment links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Login links contain account session tokens; the user completes payment separately.]

## Skill Version(s):

2.1.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
