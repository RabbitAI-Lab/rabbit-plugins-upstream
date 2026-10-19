## Description:

Guides developers through CloudBase WeChat payment and Official Account OAuth integration, including generated functions, openid handling, callbacks, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers building or debugging WeChat Mini Program payments, virtual payments, Official Account JSAPI and Native payments, or Official Account OAuth on CloudBase use this skill for integration steps and implementation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment credentials or OAuth secrets could be exposed in code or chat.

Mitigation: Configure keys, AppSecrets, and certificates in the CloudBase console; do not embed or request them in source code or prompts.

Risk: A client-side success response or an assumed generated route could trigger incorrect fulfillment.

Mitigation: Verify generated function names and routes, and confirm payment through server callbacks or order queries before fulfillment.

Risk: OAuth user information can expose personal data beyond what the application needs.

Mitigation: Request userinfo only when necessary, obtain appropriate consent, and minimize retained profile data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage.md)
- [CloudBase Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram.md)
- [CloudBase Official Account JSAPI Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5.md)
- [CloudBase Native WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-native.md)
- [CloudBase Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth.md)
- [WeChat Mini Program virtual payment](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/virtual-payment)
- [Virtual payment guide](references/virtual-payment.md)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific integration steps and troubleshooting guidance.]

## Skill Version(s):

1.2.81 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
