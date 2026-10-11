## Description:

Helps people register for PowPow, activate a subscription through user-completed checkout, and sign in from the conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Prospective PowPow users can get conversational help with account registration, email verification, subscription activation, sign-in, and common onboarding problems. The user completes payment at the checkout rather than giving payment credentials to the agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account setup handles email, password, verification code, and session information.

Mitigation: Share only the details needed for registration, protect credentials and sign-in links, and run cleanup after onboarding.

Risk: Subscription activation involves an Alipay order and payment status.

Mitigation: Complete payment yourself at the official checkout; do not give payment credentials to the agent.

## Reference(s):

- [PowPow Register on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-or)
- [PowPow website](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [PowPow subscription](https://global.powpow.online/subscription)

## Skill Output:

**Output Type(s):** [Text, Guidance, Links]

**Output Format:** [Conversational text with links and status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can provide sign-in and checkout links; falls back to instructions if Node.js 18+ is unavailable.]

## Skill Version(s):

2.0.1 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
