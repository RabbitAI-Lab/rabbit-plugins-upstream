## Description:

Guides Polish-speaking users through PowPow account registration, email verification, subscription activation and one-click sign-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to create a PowPow account, resolve registration issues and activate a subscription. The agent can prepare an Alipay order and check its status; the user provides the email code and completes payment personally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared temporary session file may mix or expose account tokens on shared agent hosts or during overlapping registrations.

Mitigation: Avoid shared or multi-user hosts, do not run registrations concurrently, and run cleanup after each session; prefer per-session state in a future revision.

Risk: The workflow handles registration details, a password, an email verification code, JWT sign-in links and subscription orders.

Mitigation: Use only with the user's consent, protect credentials and sign-in links, and leave the actual payment to the user.

## Reference(s):

- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-pl)
- [PowPow website](https://global.powpow.online)
- [Agent workflow](references/agent-flow.md)
- [Registration guidance](references/registration-flow.md)
- [Payment and activation guidance](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with links and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or later for assisted registration; provides manual guidance when unavailable.]

## Skill Version(s):

2.0.1 (source: ClawHub release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
