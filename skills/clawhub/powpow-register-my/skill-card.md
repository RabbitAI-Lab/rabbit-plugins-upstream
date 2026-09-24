## Description:

Helps Burmese-speaking users register and activate a PowPow account by introducing the product, guiding signup and subscription activation, and troubleshooting common registration, login, and pending-payment issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External Burmese-speaking PowPow users use this skill to understand the service, open a registration flow, complete subscription activation, and troubleshoot verification, login, and payment-status issues. The agent provides guidance only; users complete account, verification, and payment actions directly in PowPow pages or apps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users could share passwords, verification codes, or payment credentials in chat while following registration or subscription steps.

Mitigation: Keep all account, verification, and payment entry inside PowPow or payment-provider pages and explicitly avoid requesting secrets in chat.

Risk: The listing may blur platform capabilities, such as posting travel records or creating digital humans, with what this guide-only skill can perform.

Mitigation: State that the skill only guides registration, activation, and troubleshooting; direct creation or posting workflows to the appropriate PowPow flow or separate skill.

Risk: Payment activation paths can involve asynchronous provider or manual review delays, especially WeChat QR activation.

Mitigation: Set expectations that activation may not be immediate, advise users to wait or retry login/status checks, and route unresolved payment issues to platform support.

## Reference(s):

- [PowPow homepage](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [PowPow overview video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [Registration Flow Reference](artifact/references/registration-flow.md)
- [Payment and Activation Reference](artifact/references/payment-and-activation.md)
- [Screenshots Reference](artifact/references/screenshots.md)
- [ClawHub skill listing](https://clawhub.ai/durenzidu/skills/powpow-register-my)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Links]

**Output Format:** [Markdown text with step-by-step guidance, troubleshooting notes, and external links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guide-only output; no scripts, local execution, account automation, or credential handling.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
