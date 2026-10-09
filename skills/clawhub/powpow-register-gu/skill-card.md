## Description:

Helps users register for PowPow, activate an Alipay subscription, and open one-click login links through an assisted conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can complete account registration and email verification with agent assistance, then arrange subscription activation and access their account. The skill also helps troubleshoot registration and activation issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration requires an email verification code and account password.

Mitigation: Share only the details needed for signup and avoid exposing the password or verification code beyond the registration flow.

Risk: Temporary session tokens and one-click login links can grant account access.

Mitigation: Keep login links private and run cleanup after the flow to remove the temporary session token.

Risk: Subscription checkout may involve payment details and payment-order links.

Mitigation: Confirm the checkout domain before opening a payment page and enter payment credentials only on official Alipay or PayPal pages.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [PowPow registration flow](references/registration-flow.md)
- [PowPow payment and activation](references/payment-and-activation.md)
- [Agent-assisted flow](references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Conversational text with registration, payment, and login links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide a payment status update and a one-click login link.]

## Skill Version(s):

2.0.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
