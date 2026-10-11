## Description:

Guides users through PowPow (Bubble) registration, email verification, subscription payment, and one-click login in chat.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

People signing up for PowPow use this skill to complete registration and email verification, create a subscription order, check payment status, and access their account. The user supplies their details and verification code and completes payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session-bearing registration state is stored in a shared local temporary file, creating exposure or cross-session confusion in shared environments.

Mitigation: Review before use in shared or hosted agent environments, avoid concurrent registrations under the same OS account, and clean up state after each run.

Risk: Generated one-click login links grant access to the account if disclosed.

Mitigation: Treat login links as sensitive account access links and share them only with the registering user.

Risk: The flow handles registration credentials and initiates subscription payment orders.

Mitigation: Run only when the user explicitly requests PowPow onboarding; let the user complete payment without sharing payment credentials with the agent.

## Reference(s):

- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-pcm)
- [PowPow website](https://global.powpow.online)
- [Agent flow and script contract](artifact/references/agent-flow.md)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Chat guidance with registration steps, commands, and login or payment links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Falls back to guided registration when Node.js 18 or later is unavailable.]

## Skill Version(s):

2.0.1 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
