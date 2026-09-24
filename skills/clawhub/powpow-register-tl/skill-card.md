## Description:

Tumutulong ang skill na ito sa mga user na magrehistro ng PowPow (Bubble) account, maintindihan ang produkto gamit ang mga screenshot, ayusin ang karaniwang registration errors, at kumpletuhin ang subscription activation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External PowPow/Bubble users use this Tagalog guidance skill when they need step-by-step help creating an account, handling verification or login errors, and completing subscription activation. The skill provides guidance only; users complete credentials, verification codes, and payment details on the official platform or payment provider screens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user may paste passwords, verification codes, or payment details into chat while asking for registration help.

Mitigation: Keep the skill guidance-only and direct users to enter credentials, verification codes, and payment details only on official PowPow/Bubble, PayPal, WeChat, or Huawei screens.

Risk: A user may expect the agent to submit registration or payment actions for them.

Mitigation: State that all registration, subscription, and payment actions are completed by the user in the browser or app; the skill should not submit forms or initiate payments.

Risk: Subscription activation can be delayed for PayPal webhooks or WeChat manual confirmation, which may make users think activation failed.

Mitigation: Use the payment and activation reference to distinguish delayed activation from failure and guide the user to retry login or wait for manual confirmation when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-register-tl)
- [Official PowPow site](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [Bubble introduction video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [Registration Flow Reference](references/registration-flow.md)
- [Payment and Activation Reference](references/payment-and-activation.md)
- [Product Screenshots Reference](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown guidance with links, image references, and step-by-step next actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No code execution; no credential collection; user actions happen in browser or app screens.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
