## Description:

Helps users register a PowPow account, activate a subscription, and sign in through a guided conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can ask an agent to guide account registration, email verification, subscription checkout, and login, or get troubleshooting guidance when registration or activation stalls. The user supplies the verification code and completes payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent handles registration credentials and email verification codes.

Mitigation: Use only with a trusted agent runtime and the official PowPow service; do not disclose credentials or codes to others.

Risk: Session tokens are stored in a shared temporary state file that may remain accessible across conversations.

Mitigation: Avoid shared or multi-user runtimes until state is isolated per conversation and expires automatically; run cleanup when finished.

Risk: Generated one-click login links can grant access to the user's account.

Mitigation: Treat each login link like a password and share it only with the intended user.

Risk: Subscription checkout creates an order that requires the user's payment.

Mitigation: Have the user review the plan and complete payment themselves through the official checkout.

## Reference(s):

- [PowPow registration skill on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-id)
- [PowPow website](https://global.powpow.online)
- [Agent workflow](references/agent-flow.md)
- [Registration guidance](references/registration-flow.md)
- [Payment and activation guidance](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Links]

**Output Format:** [Conversational text with registration, checkout, and login links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can share bundled product screenshots and provide a self-service fallback when automation is unavailable.]

## Skill Version(s):

2.0.1 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
