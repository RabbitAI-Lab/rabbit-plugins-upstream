## Description:

Helps users register a PowPow account, verify their email, choose a subscription, and activate one-click login through a guided conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to create and activate a PowPow account with guided email verification and subscription checkout. The agent can prepare registration and payment steps, while the user checks their email and completes payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account setup handles an email address, verification code, optional avatar, password, and session token.

Mitigation: Use a password appropriate for PowPow, keep account details private, and run cleanup when finished to remove the temporary session token.

Risk: Subscription onboarding can open a payment checkout page.

Mitigation: Confirm the selected plan and obtain user approval before opening checkout; the user completes payment themselves.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-pnb)
- [PowPow website](https://global.powpow.online)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)
- [Agent flow](references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Conversational Markdown with steps and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide a generated password, registration status, checkout link, and one-click login link.]

## Skill Version(s):

2.0.1 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
