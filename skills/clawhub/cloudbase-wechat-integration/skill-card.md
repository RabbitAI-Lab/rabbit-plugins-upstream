## Description:

CloudBase WeChat integration guide for Mini Program WeChat Pay, Mini Program virtual payment (虚拟支付, wx.requestVirtualPayment), Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions. This skill should be used when users ask to add, debug, or extend WeChat payment, virtual payment, or official-account flows on CloudBase.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to implement, debug, and extend WeChat Mini Program and Official Account payment or OAuth flows on CloudBase. It guides them to choose the matching integration path and handle payment confirmation and callbacks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production payment tests may create real charges.

Mitigation: Use sandbox flows where available; otherwise use a deliberate low-value test and confirm the merchant setup before testing.

Risk: Security analysis was partial because three local references could not be resolved, leaving some reference checks incomplete.

Mitigation: Review the relevant reference material and current official CloudBase or WeChat documentation before implementing a payment flow.

## Reference(s):

- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage.md)
- [Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram.md)
- [Native WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-native.md)
- [Official Account JSAPI Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5.md)
- [Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth.md)
- [WeChat Mini Program virtual payment](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/virtual-payment)
- [Virtual payment client API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, API calls]

**Output Format:** [Markdown with JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific integration guidance and code examples; no fixed output length.]

## Skill Version(s):

1.2.86 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
