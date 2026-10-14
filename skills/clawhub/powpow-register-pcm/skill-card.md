## Description:

Helps users register for PowPow (Bubble), activate an Alipay or PayPal subscription, and access their account through one-click login links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can get conversational help creating an account, verifying email, activating a subscription through Alipay or PayPal, and signing in. The user completes payment at the official cashier; when automation is unavailable, the skill provides step-by-step guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration sends personal details to PowPow and initiates subscription payment orders.

Mitigation: Confirm the user's intent and details; complete payment only on the official Alipay or PayPal cashier page, without sharing payment credentials with the agent.

Risk: Generated login links and locally stored session tokens can grant account access if exposed.

Mitigation: Use a private machine, do not share login links, and run cleanup when finished to remove local session state.

## Reference(s):

- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-pcm)
- [PowPow homepage](https://global.powpow.online)
- [Agent flow](references/agent-flow.md)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with links and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes registration progress, payment handoff, and one-click login links.]

## Skill Version(s):

2.1.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
