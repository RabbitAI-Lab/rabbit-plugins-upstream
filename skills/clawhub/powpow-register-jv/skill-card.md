## Description:

Helps users register for PowPow, verify their email, activate a paid subscription, and sign in through guided chat.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

People signing up for PowPow use the agent to complete registration, troubleshoot verification or activation issues, and reach the subscription checkout. The user retrieves the email code and makes any payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-assisted registration handles account passwords and email verification codes.

Mitigation: Use a unique password and share account details only if you trust the publisher and PowPow; never give the agent Alipay credentials or payment secrets.

Risk: Generated login links grant access to the account if shared.

Mitigation: Treat login links as private account-access links and do not forward or publish them.

Risk: Payment activation and registration may leave temporary account state behind.

Mitigation: Complete payment yourself at checkout and run the skill's cleanup step after the flow finishes.

## Reference(s):

- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-jv)
- [PowPow website](https://global.powpow.online)
- [Agent-assisted flow](references/agent-flow.md)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Conversational text with links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide account-access login links and payment checkout links; keep them private.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
