## Description:

Помогает зарегистрироваться в PowPow, активировать подписку через Alipay или PayPal и получить ссылку для входа в диалоге с агентом.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Пользователи PowPow и их агенты используют навык для регистрации аккаунта, подтверждения адреса электронной почты, оформления и проверки оплаты подписки, а затем входа в аккаунт. Если Node.js недоступен, агент может сопровождать пользователя пошагово без автоматизации.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One-click login links and temporary files contain sensitive account access information.

Mitigation: Treat login links as secrets, avoid sharing them, and run the cleanup step when finished.

Risk: The registration flow handles an email verification code and creates payment orders.

Mitigation: Share the verification code only for the intended registration and complete payment only in the official Alipay or PayPal checkout.

## Reference(s):

- [PowPow](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [PowPow subscription](https://global.powpow.online/subscription)
- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-ru)
- [Registration flow](references/registration-flow.md)
- [Payment and activation](references/payment-and-activation.md)
- [Agent flow](references/agent-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Links, Text]

**Output Format:** [Conversational text with commands and account, checkout, and login links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Registration and payment status updates; requires Node.js 18 or later for automated steps, otherwise provides guided instructions.]

## Skill Version(s):

2.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
