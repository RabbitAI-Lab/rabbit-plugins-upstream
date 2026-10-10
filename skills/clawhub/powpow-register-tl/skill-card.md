## Description:

Guides users through PowPow account registration, subscription activation, and sign-in, with assisted form submission and payment-status checks when Node.js is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can get guided help creating an account, verifying their email, selecting a subscription, checking payment status, and signing in. The agent can fall back to manual guidance without Node.js.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration details, optional avatar, verification code, and login tokens are sent to PowPow; session data is temporarily stored locally.

Mitigation: Use only when registering with PowPow, avoid sharing login links, and run cleanup after finishing.

Risk: A subscription order can lead to a payment page and a charge selected by the user.

Mitigation: Confirm the subscription package before opening the payment page; the user completes payment with the cashier.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [PowPow registration guidance](references/registration-flow.md)
- [PowPow payment and activation guidance](references/payment-and-activation.md)
- [PowPow agent workflow](references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Links]

**Output Format:** [Conversational text with registration, payment, and sign-in links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide an account summary after activation; does not pay on the user's behalf.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
