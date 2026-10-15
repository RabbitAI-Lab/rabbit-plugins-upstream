## Description:

Assiste gli utenti nella registrazione a PowPow (Bolla), nell'attivazione dell'abbonamento tramite Alipay o PayPal e nell'accesso all'account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

People signing up for PowPow (Bolla) use this skill to create an account, resolve registration issues, activate a subscription through Alipay or PayPal, and receive a sign-in link. The user supplies the email verification code and completes payment at the provider's checkout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account creation involves a password, email verification code, and temporary sign-in session.

Mitigation: Save any generated password immediately, share the verification code only for registration, and run cleanup after the flow.

Risk: Checkout can start a subscription with different prices and renewal terms depending on the provider.

Mitigation: Confirm the provider, price, and renewal terms before opening checkout; the user completes payment with Alipay or PayPal.

## Reference(s):

- [PowPow registration skill on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-it)
- [PowPow website](https://global.powpow.online)
- [Agent flow](references/agent-flow.md)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with sign-in and checkout links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include product screenshots and payment-status updates; the user completes checkout.]

## Skill Version(s):

2.1.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
