## Description:

Helps people register for PowPow, activate an account through an Alipay or PayPal subscription, and obtain a one-click login link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can ask an agent to guide registration, troubleshoot verification or activation, and arrange subscription checkout while completing payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared temporary session file may expose one user's account or login link to another conversation on the same machine.

Mitigation: Use only in a single-user, trusted runtime; avoid shared agents or OS accounts and run cleanup immediately after the flow.

Risk: Token-bearing one-click links grant access to the account if disclosed.

Mitigation: Share login links only with the intended user and do not retain or forward them beyond the registration flow.

Risk: Registration and subscription checkout involve account credentials and real payments.

Mitigation: Pass the password through an environment variable and let the user complete payment at the checkout themselves.

## Reference(s):

- [PowPow official website](https://global.powpow.online)
- [PowPow registration flow](references/registration-flow.md)
- [Agent-assisted flow](references/agent-flow.md)
- [Payment and activation](references/payment-and-activation.md)
- [Product screenshots](references/screenshots.md)
- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-ja)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with login and checkout links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The user confirms their email code and pays at the checkout; the agent does not make the payment.]

## Skill Version(s):

2.1.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
