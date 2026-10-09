## Description:

Helps users register a PowPow account, activate a subscription, and sign in through a guided conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to create a PowPow account, troubleshoot registration, and complete subscription activation. The agent assists with verification, order creation, and sign-in links; users provide their own details and make any payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration involves an email address, password, and possibly an avatar and verification code.

Mitigation: Provide only the requested account details, avoid sharing the password beyond registration, and remove temporary session state after completion.

Risk: Payment links and orders could expose users to an unintended checkout or requests for payment credentials.

Mitigation: Open payment pages only from the official PowPow flow; users complete Alipay payment themselves and never give the agent their Alipay credentials.

## Reference(s):

- [PowPow official site](https://global.powpow.online)
- [PowPow registration skill on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-ur)
- [Agent flow](references/agent-flow.md)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Links]

**Output Format:** [Conversational Markdown with registration, sign-in, and payment links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or later for assisted registration; otherwise provides guidance only.]

## Skill Version(s):

2.0.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
