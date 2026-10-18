## Description:

Helps users register for PowPow, activate an Alipay or PayPal subscription, and sign in through a one-click link, with the agent handling registration and order setup while users provide their email verification code and complete payment themselves.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

People signing up for PowPow use this skill to set up an account, resolve registration or activation issues, and complete subscription activation through an official checkout. The agent can guide users instead when the required Node.js runtime is unavailable or the user prefers to register manually.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent handles account details, an email verification code, and a temporary session token during registration.

Mitigation: Share only the information needed to register, keep unrelated credentials private, and run cleanup after completion.

Risk: A checkout link could lead to an unexpected payment destination.

Mitigation: Verify the official Alipay or PayPal checkout domain before paying; the user should complete payment directly at checkout.

Risk: A PayPal subscription may renew automatically.

Mitigation: Review the subscription terms at checkout and cancel renewal if it is no longer wanted.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [ClawHub skill release](https://clawhub.ai/durenzidu/skills/powpow-register-id)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)
- [Agent workflow](references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational Markdown with registration, checkout, and sign-in links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can provide a guidance-only fallback when Node.js 18 or newer is unavailable.]

## Skill Version(s):

2.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
