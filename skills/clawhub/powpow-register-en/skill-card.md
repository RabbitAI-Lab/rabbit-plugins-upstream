## Description:

Helps users register for PowPow (Bubble), activate a subscription through Alipay, and sign in using one-click links, with guided fallback when the assisted flow is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

People signing up for PowPow use this skill to complete email verification, optional avatar upload, subscription payment setup, and login with an agent's help. It also guides users through common registration and activation problems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The registration flow handles a password and email verification code.

Mitigation: Share the code only for the intended registration, save any generated password securely, and avoid exposing either in shared conversations.

Risk: One-click login links can grant access to the account.

Mitigation: Treat login links as private, do not forward them, and run cleanup after registration to remove temporary local token state.

Risk: An avatar file may be uploaded during registration.

Mitigation: Provide only an avatar path for an image you intend to upload.

Risk: Subscription setup creates a payment order and opens a cashier page.

Mitigation: Confirm the plan and the expected PowPow/Alipay payment flow before paying; enter payment details only at the cashier.

## Reference(s):

- [PowPow Register on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-en)
- [PowPow official site](https://global.powpow.online)
- [Agent-assisted flow](references/agent-flow.md)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with links and status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include session-bearing one-click login links; Node 18 or newer enables assisted registration, otherwise guidance is provided.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
