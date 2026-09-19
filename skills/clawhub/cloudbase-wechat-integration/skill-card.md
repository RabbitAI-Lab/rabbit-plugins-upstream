## Description:

CloudBase WeChat integration guide for Mini Program WeChat Pay, Mini Program virtual payment, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, debug, or extend CloudBase WeChat payment and Official Account OAuth flows, including generated function calls, order persistence, callback handling, idempotency, fulfillment, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill helps modify payment, refund, callback, and OAuth code where mistakes can affect business state or customer transactions.

Mitigation: Review generated code before production use and verify behavior with function logs, callback logs, sandbox tests, or low-value production tests.

Risk: Merchant keys, AppSecrets, private keys, APIv3 keys, AppKeys, session keys, and certificates could be mishandled during implementation.

Mitigation: Keep secrets in CloudBase console or managed configuration, never in source code, browser code, commits, prompts, or chat.

Risk: Frontend payment success callbacks can be mistaken for authoritative payment confirmation.

Mitigation: Use server-side payment callbacks or order queries as the business source of truth, and implement idempotent order updates and fulfillment.

Risk: CloudBase Integration Center generated function names and route paths may differ from examples.

Mitigation: Inspect the actual generated function name and HTTP routes before writing calls or changing callback handlers.

## Reference(s):

- [CloudBase WeChat Integration Overview](references/overview.md)
- [Mini Program WeChat Pay](references/mini-program-pay.md)
- [Mini Program Virtual Payment](references/virtual-payment.md)
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md)
- [Native QR-Code Pay](references/native-qr-pay.md)
- [Official Account OAuth](references/official-account-oauth.md)
- [WeChat Integration Troubleshooting](references/troubleshooting.md)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage.md)
- [CloudBase Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram.md)
- [CloudBase Official Account JSAPI Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5.md)
- [CloudBase Native WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-native.md)
- [CloudBase Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth.md)
- [WeChat Mini Program virtual payment](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/virtual-payment)
- [wx.requestVirtualPayment API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks and scenario-specific checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CloudBase console steps, generated-function call shapes, troubleshooting actions, and implementation self-checks.]

## Skill Version(s):

1.2.51 (source: server release metadata; artifact frontmatter reports 2.34.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
