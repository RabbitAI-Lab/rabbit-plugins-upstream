## Description:

Helps users register for PowPow (Bubble), complete email verification, activate an Alipay or PayPal subscription, and sign in through guided one-click links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

People signing up for PowPow use this skill to complete registration, troubleshoot verification issues, and activate a subscription while paying at the Alipay or PayPal cashier themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration and payment assistance stores a logged-in session token in a predictable temporary file until cleanup.

Mitigation: Use a single-user machine, run cleanup after the flow, and avoid shared systems unless state-file handling is tightened.

Risk: The skill can create an account, send verification requests, upload an optional avatar, and create subscription orders.

Mitigation: Review these actions before installing; pay only through the cashier yourself and do not share payment credentials with the agent.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-en)
- [PowPow website](https://global.powpow.online)
- [Agent-assisted flow](artifact/references/agent-flow.md)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational Markdown with registration instructions, payment links, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or later for agent-assisted actions; otherwise provides guidance without running the script.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
