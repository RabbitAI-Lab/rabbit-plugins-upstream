## Description:

Guides users through PowPow account registration, email verification, Alipay subscription activation, and one-click sign-in in a Marathi-language conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to create and activate a PowPow account through guided registration and payment onboarding. The agent handles form submission and payment-status checks; the user retrieves the email code and completes payment at the Alipay cashier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email verification codes and temporary session tokens can grant access to the account.

Mitigation: Use the code only for PowPow registration, share sign-in links only with the intended user, and clear temporary session state after onboarding.

Risk: Payment onboarding could expose sensitive payment credentials if handled in chat.

Mitigation: Keep payment and payment credentials inside the official Alipay cashier; let the agent create an order and check its status only.

## Reference(s):

- [PowPow official website](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [PowPow subscription](https://global.powpow.online/subscription)
- [Agent-assisted flow](references/agent-flow.md)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)
- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-mr)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with sign-in links and next-step instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides an account summary after activation; requires Node.js 18 or newer for assisted operation, with a guidance-only fallback.]

## Skill Version(s):

2.0.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
