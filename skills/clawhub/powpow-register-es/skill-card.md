## Description:

Guides PowPow users through account registration, email verification, Alipay or PayPal subscription activation, and one-click sign-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users can register for PowPow, resolve registration issues, activate a subscription through Alipay or PayPal, and receive a sign-in link. The agent assists with the process while the user supplies the email code and approves payment at checkout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent handles an email verification code, password, and account session during registration.

Mitigation: Use only if you trust the publisher and PowPow; keep credentials private and run cleanup after the flow.

Risk: One-click sign-in links contain session tokens that can grant account access.

Mitigation: Do not share generated sign-in links; open them only in a trusted browser.

Risk: Creating an Alipay or PayPal order can lead to a real charge or a renewing subscription.

Mitigation: Confirm the plan and each payment step yourself at the official checkout before authorizing payment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-es)
- [PowPow website](https://global.powpow.online)
- [Agent flow](references/agent-flow.md)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Links]

**Output Format:** [Conversational text with checkout and sign-in links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sign-in links can contain session tokens; payment is completed by the user.]

## Skill Version(s):

2.1.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
