## Description:

Helps users sign up for PowPow, activate a subscription, and access their account through a guided conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Prospective PowPow users can register an account, receive help with email verification, create an Alipay subscription order, and get sign-in links. The user supplies their details and verification code and completes payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration shares personal details with PowPow and temporarily stores a session token during setup.

Mitigation: Proceed only with the user's consent, run cleanup after activation, and avoid shared machines unless the local account environment is trusted.

Risk: Creating an Alipay checkout order may lead to a paid subscription.

Mitigation: Explain the selected plan and checkout step; the user, not the agent, completes payment.

## Reference(s):

- [PowPow skill on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-ja)
- [PowPow official site](https://global.powpow.online)
- [Agent-assisted registration flow](references/agent-flow.md)
- [Registration guidance](references/registration-flow.md)
- [Payment and activation guidance](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Images]

**Output Format:** [Conversational guidance with sign-in and checkout links and optional product screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The user completes email verification and payment; Node.js 18 or later enables assisted registration, with guidance-only fallback.]

## Skill Version(s):

2.0.1 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
