## Description:

Guides users through PowPow account registration, email verification, subscription activation via Alipay or PayPal, and one-click login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to learn about PowPow, create and activate an account, resolve signup issues, and receive login links. An agent assists with verification and subscription order setup while the user completes payment in the official cashier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials, verification codes, and session tokens are handled during registration; a login token is temporarily stored in a predictable local temp file.

Mitigation: Review before use on shared machines, keep other local users from accessing the temp directory, and run cleanup when finished.

Risk: Subscription order creation can lead to a real payment or recurring PayPal subscription.

Mitigation: Review the subscription terms and approve payment only in the official cashier.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)
- [Agent flow](references/agent-flow.md)
- [Screenshot guide](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational Markdown with links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide registration status, payment instructions, and one-click login links.]

## Skill Version(s):

2.1.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
