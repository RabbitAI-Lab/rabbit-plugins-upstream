## Description:

Helps users register a PowPow account, verify their email, activate a subscription, and sign in through a guided conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can complete account registration, email verification, subscription activation, and sign-in with agent assistance. The agent also helps troubleshoot registration and activation issues; the user completes payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent handles an account password and email verification code.

Mitigation: Share codes only for official registration, keep passwords out of command arguments and saved files, and do not repeat credentials in responses.

Risk: One-click login links carry account access.

Mitigation: Treat login links as secrets, send them only to the account holder, and avoid posting or forwarding them.

Risk: Avatar uploads can expose a local file chosen by the agent.

Mitigation: Use only an image the user explicitly selected; do not accept arbitrary local paths.

Risk: The agent sets up subscription orders and temporary registration state.

Mitigation: Complete payment only on the official Alipay or PayPal page, never share payment credentials with the agent, and run cleanup after registration.

## Reference(s):

- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-ml)
- [PowPow homepage](https://global.powpow.online)
- [Agent-assisted registration flow](artifact/references/agent-flow.md)
- [Registration rules and troubleshooting](artifact/references/registration-flow.md)
- [Payment and activation guidance](artifact/references/payment-and-activation.md)
- [Product screenshots](artifact/references/screenshots.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Conversational Markdown with links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide sign-in links, payment-status updates, and an account summary.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
