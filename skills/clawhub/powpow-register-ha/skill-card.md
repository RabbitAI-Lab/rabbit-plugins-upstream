## Description:

Guides Hausa-speaking users through PowPow (Bubble) account registration, common sign-up issues, and subscription activation without collecting credentials or performing account actions for them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for Hausa-language guidance when creating a PowPow account, resolving registration blockers, and understanding subscription activation options. It is intended for conversational guidance only; registration, verification, and payment remain inside the official PowPow, PayPal, WeChat, or Huawei flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user may share passwords, verification codes, or payment details in the conversation.

Mitigation: Keep registration, verification, password entry, and payment inside the official PowPow, PayPal, WeChat, or Huawei flows; the skill should not request or collect those secrets.

Risk: Subscription activation can be delayed or require manual confirmation, especially for WeChat payments.

Mitigation: Guide the user to the official subscription flow, set expectations about possible delays, and avoid attempting payment or activation on the user's behalf.

Risk: Outdated platform details could lead to incorrect registration guidance if PowPow changes its forms or subscription flow.

Mitigation: Treat the live PowPow interface as authoritative when it differs from the skill references, and keep troubleshooting guidance limited to the documented behavior.

## Reference(s):

- [Registration flow reference](references/registration-flow.md)
- [Payment and activation reference](references/payment-and-activation.md)
- [Product screenshots reference](references/screenshots.md)
- [PowPow website](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [Bubble introductory video](https://www.bilibili.com/video/BV1Wu826UEVz/)

## Skill Output:

**Output Type(s):** [guidance, markdown]

**Output Format:** [Conversational Markdown with links and one clear next-step action]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include 1-3 relevant product screenshot links from the documented public screenshot set.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
