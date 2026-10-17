## Description:

Helps users register a PowPow account, activate a subscription through Alipay or PayPal, and sign in through a guided conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users can complete account registration, resolve verification or activation issues, and receive guidance through subscription payment and sign-in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration handles an email address, verification code, password, and optional profile image.

Mitigation: Provide these only for the intended PowPow registration flow; do not share the password or verification code beyond that flow.

Risk: A temporary session token and checkout files may remain on the local device.

Mitigation: Run the skill's cleanup step after onboarding and remove temporary checkout files when no longer needed.

Risk: Subscription activation involves a payment checkout.

Mitigation: Review the checkout and authorize payment yourself through Alipay or PayPal.

## Reference(s):

- [PowPow website](https://global.powpow.online)
- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-ln)
- [Agent-assisted registration flow](references/agent-flow.md)
- [Registration guidance](references/registration-flow.md)
- [Payment and activation guidance](references/payment-and-activation.md)
- [Product screenshots guide](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Links]

**Output Format:** [Conversational text with registration, checkout, and sign-in links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include account setup and subscription status updates.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
