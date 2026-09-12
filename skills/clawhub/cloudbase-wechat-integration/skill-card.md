## Description:

CloudBase WeChat Integration guides agents through CloudBase WeChat Pay, Mini Program virtual payment, Official Account JSAPI Pay, Native QR-code Pay, OAuth, openid handling, callbacks, and generated Integration Center functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, debug, or extend WeChat payment, virtual-payment, Official Account OAuth, callback, and order-status flows in CloudBase applications while keeping credentials in managed configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment and OAuth guidance can affect money movement and user identifiers.

Mitigation: Review generated code before deployment and validate payment state through verified backend callbacks or order queries.

Risk: Merchant credentials, API keys, certificates, AppSecret values, or AppKey values could be exposed if copied into source code or chat.

Mitigation: Keep sensitive values in CloudBase or WeChat console configuration and avoid embedding them in generated files or prompts.

Risk: Frontend payment success can be mistaken for final fulfillment.

Mitigation: Drive fulfillment from callback handling or explicit order-status queries with idempotency, amount checks, and order validation.

## Reference(s):

- [CloudBase WeChat Integration Overview](references/overview.md)
- [Mini Program WeChat Pay](references/mini-program-pay.md)
- [Mini Program Virtual Payment](references/virtual-payment.md)
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md)
- [Native QR-Code Pay](references/native-qr-pay.md)
- [Official Account OAuth](references/official-account-oauth.md)
- [WeChat Integration Troubleshooting](references/troubleshooting.md)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce/index.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage/index.md)
- [CloudBase Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)
- [CloudBase Native WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-native/index.md)
- [CloudBase Official Account JSAPI Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md)
- [CloudBase Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md)
- [WeChat Mini Program Virtual Payment](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/virtual-payment)
- [wx.requestVirtualPayment API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may propose client and backend changes, but generated payment or OAuth behavior should be reviewed before deployment.]

## Skill Version(s):

1.2.45 (source: ClawHub release metadata; artifact frontmatter reports 2.33.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
