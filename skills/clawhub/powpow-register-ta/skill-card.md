## Description:

Helps users register a PowPow account, activate an Alipay or PayPal subscription, and obtain a one-click login link through a guided conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can get conversational help registering an account, verifying their email, paying for a subscription at the provider's checkout, and signing in. Posting travel notes and creating digital humans are outside this skill's scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One-click login links and temporary state can expose live sign-in tokens.

Mitigation: Treat login links as secrets, avoid sharing screenshots or logs that contain them, and run cleanup when finished.

Risk: Registration and subscription setup involve an email verification code and a payment order.

Mitigation: Share the verification code only for the intended registration; complete payment yourself at the provider's checkout and do not provide payment credentials to the agent.

Risk: The listing describes social and chat features that this skill does not provide.

Mitigation: Use this skill only for registration, subscription activation, and sign-in; use a separate skill for posting or digital-human features.

## Reference(s):

- [PowPow Register ClawHub release](https://clawhub.ai/durenzidu/skills/powpow-register-ta)
- [PowPow homepage](https://global.powpow.online)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text with checkout and login links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include packaged product screenshots; one-click login links are sensitive.]

## Skill Version(s):

2.1.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
