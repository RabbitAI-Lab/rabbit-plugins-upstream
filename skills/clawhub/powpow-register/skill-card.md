## Description:

Helps users register a PowPow account, activate a subscription through Alipay or PayPal, and obtain a sign-in link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

People signing up for PowPow can use this skill to complete email-verified registration, choose an Alipay or PayPal subscription, check activation, and receive a sign-in link. If automated registration is unavailable, it offers guided steps instead.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration uses personal details, an email verification code, and a temporary PowPow session token.

Mitigation: Share the code only for PowPow registration and run cleanup after the flow to remove local session state.

Risk: Subscription activation opens an Alipay or PayPal checkout page.

Mitigation: Complete payment directly with the payment provider; do not give the agent payment credentials.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [PowPow subscriptions](https://global.powpow.online/subscription)
- [Agent registration flow](references/agent-flow.md)
- [Payment and activation guidance](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Links]

**Output Format:** [Markdown guidance and sign-in or checkout links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Automated flow requires Node.js 18 or later; offers guided registration otherwise. Payment is completed by the user at the payment provider.]

## Skill Version(s):

2.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
