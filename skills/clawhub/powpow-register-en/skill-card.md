## Description:

Helps users register for PowPow (Bubble), activate a subscription through Alipay, and access their account through one-click login links, with guidance-only fallback when assisted registration is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

People creating a PowPow account use this skill for guided registration, email verification, subscription activation, and troubleshooting. The user checks their email and completes payment directly at the cashier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration involves an email address, password, verification code, and a temporary session token.

Mitigation: Use these only for the requested registration, avoid displaying credentials again, and remove temporary session state when finished.

Risk: Subscription activation creates a payment order and opens an Alipay checkout page.

Mitigation: Confirm the user's plan choice and have the user complete payment at the cashier; do not request payment credentials or pay on their behalf.

## Reference(s):

- [PowPow Register on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-en)
- [PowPow homepage](https://global.powpow.online)
- [Agent-assisted flow](references/agent-flow.md)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Conversational Markdown with account and payment links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Assisted flow requires Node.js 18 or newer; guidance-only fallback is available.]

## Skill Version(s):

2.0.0 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
