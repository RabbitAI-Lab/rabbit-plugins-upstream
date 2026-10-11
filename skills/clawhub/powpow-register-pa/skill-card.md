## Description:

Guides users through PowPow account registration, email verification, subscription activation, and login in a conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

New PowPow users can get guided help with registration, troubleshooting, Alipay subscription activation, and login; the user checks their email code and completes payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration involves an email verification code and a password.

Mitigation: Only share the code for the intended registration and pass the password through an environment variable.

Risk: Subscription activation creates a payment order.

Mitigation: Review the order and complete payment yourself at the Alipay checkout; do not give the agent payment credentials.

Risk: A session token may be stored locally during onboarding.

Mitigation: Run the skill's cleanup step after registration and activation.

## Reference(s):

- [PowPow ClawHub release](https://clawhub.ai/durenzidu/skills/powpow-register-pa)
- [PowPow website](https://global.powpow.online)
- [Agent registration flow](artifact/references/agent-flow.md)
- [Registration and troubleshooting](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Links]

**Output Format:** [Conversational text with registration, payment, and login links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Payment must be completed by the user.]

## Skill Version(s):

2.0.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
