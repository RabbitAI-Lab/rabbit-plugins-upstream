## Description:

Guides users through PowPow account registration, email verification, Alipay or PayPal activation, and one-click sign-in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users use the agent to register a PowPow account, resolve registration or activation issues, and complete an Alipay or PayPal subscription while making the payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration transmits an email address, password, and verification code to PowPow.

Mitigation: Confirm the PowPow destination and share these credentials only if comfortable creating an account there.

Risk: Temporary session tokens and one-click sign-in links grant account access if exposed.

Mitigation: Keep sign-in links private and run cleanup when registration is complete.

Risk: The agent can open Alipay or PayPal payment pages for subscriptions.

Mitigation: Verify the payment destination and subscription terms before approving payment.

## Reference(s):

- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-yo)
- [PowPow website](https://global.powpow.online)
- [Agent flow](references/agent-flow.md)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Markdown with registration steps, commands, and sign-in or payment links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include product screenshots and account or subscription status.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
