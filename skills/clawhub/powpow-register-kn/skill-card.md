## Description:

Helps users register a PowPow account, verify their email, activate a subscription through the official cashier, and sign in through a guided conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this Kannada-language skill to create and activate a PowPow account, with help entering registration details, resolving sign-up problems, and following the subscription and login steps. The user supplies the verification code and completes payment at the official cashier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration requires an email address, password, and email verification code.

Mitigation: Only share these for the intended PowPow sign-up; use the verification code solely for registration and keep the password private.

Risk: Subscription activation involves payment.

Mitigation: Pay only in the official Alipay or PayPal cashier; never give payment credentials to the agent.

Risk: Generated one-click login links and temporary sign-up state can grant account access.

Mitigation: Treat login links as sensitive session links and run cleanup after finishing.

## Reference(s):

- [PowPow official website](https://global.powpow.online)
- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-kn)
- [Agent-assisted registration flow](references/agent-flow.md)
- [Registration flow and troubleshooting](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)
- [Product screenshot guide](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Conversational text and Markdown with links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide one-click login links and relevant product screenshots; does not produce posts or digital humans.]

## Skill Version(s):

2.0.1 (source: server-resolved ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
