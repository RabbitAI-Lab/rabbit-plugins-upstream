## Description:

Guides users through PowPow account registration, email verification, subscription activation, and one-click login, with the user completing payment at checkout.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can get conversational help creating and activating an account, including troubleshooting verification and subscription issues. The skill does not publish posts or create digital people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration involves an email address, password, verification code, and temporary session-token state.

Mitigation: Only share credentials for the intended registration flow, and run cleanup afterward to remove the temporary state file.

Risk: Account activation requires a payment checkout.

Mitigation: Review the order and complete payment yourself on the Alipay checkout page; do not give payment credentials to the agent.

Risk: Bhojpuri/Hindi guidance and Chinese platform messages may be hard to understand.

Mitigation: Confirm the meaning of unfamiliar instructions or payment messages before proceeding.

## Reference(s):

- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-bho)
- [PowPow website](https://global.powpow.online)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)
- [Agent-assisted flow](artifact/references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Conversational text and Markdown with commands and login or checkout links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+ for assisted registration; otherwise provides step-by-step guidance.]

## Skill Version(s):

2.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
