## Description:

CloudBase WeChat integration guidance for Mini Program WeChat Pay, Mini Program virtual payment, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, debug, or extend CloudBase applications that integrate with WeChat payment, virtual payment, Official Account OAuth, and generated Integration Center functions. It helps agents produce scenario-specific guidance, code, configuration steps, and troubleshooting actions while preserving payment validation and credential-handling boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated payment or callback changes can affect money movement, order state, refunds, or fulfillment.

Mitigation: Review generated code carefully and verify changes with sandbox or low-value production tests before real use.

Risk: Merchant keys, AppSecret values, AppKey material, private keys, APIv3 keys, or certificates could be exposed if copied into chat, frontend code, or source files.

Mitigation: Keep credentials in CloudBase, WeChat, or merchant console configuration and avoid placing secrets in prompts or code.

Risk: Trusting frontend payment success callbacks can mark unpaid or unconfirmed orders as fulfilled.

Mitigation: Use payment callbacks or server-side order queries as the authoritative payment state before updating business data.

Risk: Assuming example generated function names or routes can produce broken payment and OAuth flows.

Mitigation: Confirm the actual generated function name, route path, CloudBase environment ID, and WeChat app binding before writing calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
- [CloudBase WeChat Integration Overview](references/overview.md)
- [Mini Program WeChat Pay](references/mini-program-pay.md)
- [Mini Program Virtual Payment](references/virtual-payment.md)
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md)
- [Native QR-Code Pay](references/native-qr-pay.md)
- [Official Account OAuth](references/official-account-oauth.md)
- [WeChat Integration Troubleshooting](references/troubleshooting.md)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage.md)
- [CloudBase Mini Program WeChat Pay documentation](https://docs.cloudbase.net/integration/wechat-pay-miniprogram.md)
- [CloudBase Native WeChat Pay documentation](https://docs.cloudbase.net/integration/wechat-pay-native.md)
- [CloudBase Official Account JSAPI Pay documentation](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5.md)
- [CloudBase Official Account OAuth documentation](https://docs.cloudbase.net/integration/wechat-official-oauth.md)
- [WeChat wx.requestVirtualPayment API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)
- [WeChat Mini Program virtual payment guide](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/virtual-payment)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific guidance should preserve credential boundaries, generated callback verification, idempotent order handling, and callback or query-based payment confirmation.]

## Skill Version(s):

1.2.53 (source: ClawHub release metadata; artifact frontmatter version: 2.34.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
