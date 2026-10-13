## Description:

Helps users register a PowPow account in chat, complete email verification, activate an Alipay or PayPal subscription, and sign in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow users and their agents use this skill to register an account, troubleshoot verification or activation, and complete subscription setup while the user authorizes payment on the payment provider's page. It does not create posts or digital people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration details are sent to PowPow, and a session token is temporarily stored on disk.

Mitigation: Use on a single-user machine and run the skill's cleanup step after registration.

Risk: Payment helper files open a checkout page in the browser.

Mitigation: Check that the payment page is on the expected Alipay or PayPal domain before approving payment.

Risk: The skill runs a local Node.js helper during assisted registration.

Mitigation: Review the helper before installation, or use the guidance-only flow instead.

## Reference(s):

- [PowPow skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-am)
- [PowPow website](https://global.powpow.online)
- [Registration flow](artifact/references/registration-flow.md)
- [Payment and activation](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Links]

**Output Format:** [Conversational Markdown with registration and payment links and optional product screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Assisted registration requires Node.js 18 or newer; otherwise the skill provides guidance only.]

## Skill Version(s):

2.1.0 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
