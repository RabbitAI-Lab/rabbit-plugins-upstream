## Description:

Guides users through PowPow Bubble account registration, email verification, Alipay activation, and one-click sign-in in Yoruba.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to create and activate a PowPow Bubble account, resolve common registration problems, and receive sign-in links. Users provide an email verification code and complete payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared temporary file containing live login state may expose one user's account link to another conversation on the same host.

Mitigation: Review before use on shared or multi-user hosts; use only on a trusted host, avoid concurrent registrations, and run cleanup immediately after completion.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-yo)
- [PowPow website](https://global.powpow.online)
- [Agent workflow](artifact/references/agent-flow.md)
- [Registration guidance](artifact/references/registration-flow.md)
- [Payment and activation guidance](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Links]

**Output Format:** [Conversational text with commands and sign-in or checkout links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or newer for assisted registration; otherwise provides manual guidance. Users complete their own payment.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
