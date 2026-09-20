## Description:

CloudBase WeChat integration guide for Mini Program WeChat Pay, Mini Program virtual payment, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, debug, or extend WeChat payment, virtual payment, Official Account OAuth, and callback flows in CloudBase applications. It helps route work to the relevant CloudBase Integration Center scenario while preserving payment-state, credential, and generated-function safety boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment or OAuth implementation changes may mishandle merchant credentials, AppSecrets, private keys, APIv3 keys, certificates, AppKeys, or session keys.

Mitigation: Keep secrets in CloudBase console or managed server-side configuration, never in chat, client code, examples, commits, or generated source.

Risk: Payment fulfillment may be triggered from frontend success callbacks before payment state is authoritative.

Mitigation: Use server-side payment callbacks or order-query results for fulfillment, and make order updates idempotent.

Risk: Generated CloudBase Integration Center function names, routes, or credential environment variables may be assumed incorrectly.

Mitigation: Inspect the actual generated function name, route paths, console configuration, and logs before writing or changing calls.

Risk: Virtual payment flows may be confused with WeChat Pay merchant flows or use sandbox credentials in production.

Mitigation: Confirm whether the scenario uses wx.requestVirtualPayment or wx.requestPayment, keep sandbox AppKeys out of production, and test with sandbox or low-value production flows before launch.

## Reference(s):

- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage.md)
- [CloudBase Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram.md)
- [CloudBase Native WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-native.md)
- [CloudBase Official Account JSAPI Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5.md)
- [CloudBase Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth.md)
- [WeChat Mini Program virtual payment](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/virtual-payment)
- [wx.requestVirtualPayment API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)
- [Mini Program WeChat Pay reference](references/mini-program-pay.md)
- [Mini Program virtual payment reference](references/virtual-payment.md)
- [Official Account OAuth reference](references/official-account-oauth.md)
- [Troubleshooting reference](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific references and implementation checklists for CloudBase WeChat payment and OAuth flows]

## Skill Version(s):

1.2.52 (source: ClawHub release metadata; artifact frontmatter reports 2.34.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
