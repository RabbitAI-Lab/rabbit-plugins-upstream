## Description:

Guides users through PowPow account registration, subscription activation, and one-click login, with troubleshooting when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users can create a PowPow account, verify their email, activate a paid subscription, and obtain a login link. The skill can guide users through registration and activation problems; it does not create travel posts or digital people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may see or generate an account password and receive an email verification code in chat.

Mitigation: Use a unique password and share a verification code only if comfortable providing it in chat.

Risk: One-click login links and a temporarily stored session token can grant account access.

Mitigation: Keep login links private and run the provided cleanup step after registration.

Risk: The skill creates a payment order and directs the user to a checkout page.

Mitigation: Verify that checkout uses the official PowPow/Alipay flow and complete payment yourself.

## Reference(s):

- [PowPow registration skill on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-de)
- [PowPow official website](https://global.powpow.online)
- [Registration flow reference](artifact/references/registration-flow.md)
- [Payment and activation reference](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with login links and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes registration guidance, payment-status updates, and an account summary.]

## Skill Version(s):

2.0.1 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
