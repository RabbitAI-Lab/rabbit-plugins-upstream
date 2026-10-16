## Description:

Helps users register for PowPow, activate a subscription through Alipay or PayPal, and access their account through a one-click login link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users can register a PowPow account, confirm their email, choose an Alipay or PayPal subscription, and get help with activation and login issues. The user completes payment on the payment provider's page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One-click login links grant access to live account sessions if shared.

Mitigation: Treat login links like passwords; share them only with the intended user and do not repost them.

Risk: The agent handles registration details, email codes, and a temporary session token during signup and payment activation.

Mitigation: Use the manual web flow if the user does not want the agent handling session tokens, and ensure temporary session data is cleaned up afterward.

## Reference(s):

- [PowPow registration skill on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-pa)
- [PowPow website](https://global.powpow.online)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)
- [Agent flow](references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Links]

**Output Format:** [Conversational text with payment and login links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides registration progress and subscription activation status.]

## Skill Version(s):

2.1.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
