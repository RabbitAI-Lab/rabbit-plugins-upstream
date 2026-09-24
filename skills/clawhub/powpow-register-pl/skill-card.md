## Description:

Polish-language informational assistant that introduces PowPow, guides users through account registration, helps troubleshoot registration issues, and explains subscription activation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for Polish-language guidance when creating and activating a PowPow account. The skill explains the product, registration form, common registration errors, and subscription activation while leaving all account, code, and payment actions to the user on official PowPow or payment-provider pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user could mistakenly share a password, verification code, or payment detail with the agent while asking for registration help.

Mitigation: The skill should keep all account, code, and payment entry on the official PowPow, PayPal, WeChat, or Huawei flows and should not request or process those secrets.

Risk: A user could treat delayed payment activation as immediate failure, especially for manual WeChat confirmation or delayed subscription status updates.

Mitigation: The skill should explain expected activation timing and direct the user to retry login, wait for manual confirmation, or use official platform support when the referenced flow says activation may be delayed.

## Reference(s):

- [PowPow registration flow reference](references/registration-flow.md)
- [PowPow payment and activation reference](references/payment-and-activation.md)
- [PowPow screenshot reference](references/screenshots.md)
- [PowPow homepage](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [PowPow product video](https://www.bilibili.com/video/BV1Wu826UEVz/)

## Skill Output:

**Output Type(s):** [guidance, markdown]

**Output Format:** [Markdown conversational guidance with links and step-by-step instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Polish-language user-facing responses; may include 1-3 product screenshot links relevant to the current step.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
