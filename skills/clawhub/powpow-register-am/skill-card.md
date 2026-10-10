## Description:

Guides users through PowPow account registration, email verification, subscription activation, and one-click sign-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Prospective PowPow users can get conversational help creating an account, resolving registration issues, and activating a subscription. The agent can prepare payment orders and sign-in links; users complete verification and payment themselves. Posting travel notes and creating digital people are outside this skill's scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reusable sign-in tokens in a shared temporary state file could expose one user's session to another user in shared agent environments.

Mitigation: Avoid shared or hosted installations until state is isolated per user or conversation, with expiration and ownership checks; protect sign-in links as account credentials.

Risk: The skill can create accounts and payment orders, which may be unexpected if users believe it only provides information.

Mitigation: Confirm the user's intent before registration or order creation, and leave payment completion to the user on the payment page.

Risk: The marketplace title suggests posting travel notes and chatting with digital people, but this skill only handles registration and activation.

Mitigation: Describe its registration-only scope clearly and correct the marketplace listing before deployment.

## Reference(s):

- [PowPow Register on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-am)
- [PowPow website](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [Registration guidance](references/registration-flow.md)
- [Payment and activation guidance](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with links and optional product screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include payment-page and one-click sign-in links.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
