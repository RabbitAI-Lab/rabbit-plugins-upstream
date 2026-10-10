## Description:

Helps users register for PowPow, verify their email, activate an Alipay subscription, and sign in through a guided conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Prospective PowPow users use this skill to create an account, complete email verification, purchase a subscription, and receive sign-in links. It can also guide users manually when Node.js 18 or later is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account creation sends the user's email and optional profile image to PowPow.

Mitigation: Confirm the destination and obtain the user's consent before submitting personal information.

Risk: A temporary login token remains on disk until cleanup.

Mitigation: Run the skill's cleanup step after registration and avoid sharing sign-in links.

Risk: The skill creates a paid Alipay order and opens locally generated checkout HTML.

Mitigation: Review the order and checkout destination; have the user confirm and complete payment themselves.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-ln)
- [PowPow website](https://global.powpow.online)
- [Agent registration flow](references/agent-flow.md)
- [Registration guidance](references/registration-flow.md)
- [Payment and activation guidance](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational Markdown with sign-in and checkout links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes account setup and payment-status guidance; the user completes payment.]

## Skill Version(s):

2.0.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
