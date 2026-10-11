## Description:

Helps users register for PowPow, activate a subscription through Alipay, and sign in using one-click links while troubleshooting registration and activation issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can ask an agent to guide or assist with account registration, email verification, subscription payment setup, and login. The user supplies their own details and verification code and completes payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration passwords and email verification codes can be exposed in conversation history.

Mitigation: Share credentials only in a trusted session; keep transcripts private and avoid repeating or publishing passwords and codes.

Risk: One-click login links and temporary account state contain sensitive session access.

Mitigation: Treat links and tokens like passwords, do not share them publicly, and run cleanup after the flow.

Risk: The agent can create and track a subscription payment order.

Mitigation: Confirm the plan and checkout details before proceeding; the user should complete payment directly in the payment checkout.

## Reference(s):

- [PowPow skill release](https://clawhub.ai/durenzidu/skills/powpow-register-pt)
- [PowPow website](https://global.powpow.online)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)
- [Agent flow](artifact/references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Login links]

**Output Format:** [Conversational text with links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can share product screenshots and account or payment status.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
