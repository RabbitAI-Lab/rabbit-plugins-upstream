## Description:

Guides users through PowPow signup, email verification, Alipay or PayPal subscription activation, and one-click login in a conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can register an account, complete email verification, activate an Alipay or PayPal subscription, and open a one-click login link with agent assistance. The skill also offers guided steps when the automation is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A live login token is stored in a predictable temporary file and could expose the account on a shared machine.

Mitigation: Review before installing on shared or managed machines, use private per-run storage or a credential store where possible, and run cleanup when finished.

Risk: Passwords, email codes, and one-click login links can grant access if disclosed or reused.

Mitigation: Handle credentials privately, complete payment only at the provider checkout, and do not reuse generated login links.

## Reference(s):

- [PowPow skill release](https://clawhub.ai/durenzidu/skills/powpow-register-kn)
- [PowPow website](https://global.powpow.online)
- [Agent flow](references/agent-flow.md)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Links]

**Output Format:** [Conversational text and Markdown with commands and login or checkout links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes registration progress and payment-activation status; does not make payments for the user.]

## Skill Version(s):

2.1.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
