## Description:

Helps users register for PowPow, activate a subscription through Alipay, and access their account with a one-click login link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can get guided or agent-assisted account registration, email verification, subscription activation, and help with signup or payment issues. The user completes the payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent handles registration details, a password, and an email verification code.

Mitigation: Install only if comfortable sharing these details with the agent; use the manual web registration path otherwise.

Risk: One-click login links and temporary session tokens can grant access if shared.

Mitigation: Keep login links private and run cleanup after registration to remove temporary session data.

Risk: The agent handles payment checkout HTML and monitors subscription activation.

Mitigation: Complete payment yourself on the checkout page, or use the manual web payment path if you prefer not to handle checkout through the agent.

## Reference(s):

- [PowPow skill on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-tr)
- [PowPow website](https://global.powpow.online)
- [Agent flow](artifact/references/agent-flow.md)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Conversational Markdown with links and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide one-click login links and a local payment checkout page; the user completes payment.]

## Skill Version(s):

2.0.1 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
