## Description:

Guides Italian-speaking users through PowPow/Bubble account registration, common signup issues, product screenshots, and subscription activation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to understand Bubble, create a PowPow account, troubleshoot registration problems, and complete subscription activation through the platform's own web or app flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill discusses account registration and subscription activation, where users may be tempted to share passwords, verification codes, or payment evidence.

Mitigation: Keep all credential, verification, and payment actions inside the PowPow browser or app flow; the assistant should not request or handle secrets, codes, receipts, or payments.

Risk: The skill sends users to subscription and payment pages as part of account activation.

Mitigation: Use the documented PowPow subscription page and explain that payment is completed by the user through PayPal, WeChat QR confirmation, or Huawei in-app purchase, depending on the user's environment.

Risk: Public screenshot links may be used to explain the product before registration.

Mitigation: Use only the documented screenshot URLs or mirror links, send only a few relevant images, and avoid local file paths or downloaded copies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-register-it)
- [Publisher profile](https://clawhub.ai/user/durenzidu)
- [PowPow homepage](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [Product video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [Registration flow reference](references/registration-flow.md)
- [Payment and activation reference](references/payment-and-activation.md)
- [Product screenshots reference](references/screenshots.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Italian Markdown guidance with links and short next-step instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No code execution; the user completes registration, verification, subscription, and payment in the PowPow browser or app interface.]

## Skill Version(s):

1.0.0 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
