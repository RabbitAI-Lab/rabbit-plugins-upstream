## Description:

Guides developers through CloudBase WeChat payment and Official Account OAuth integrations, including order handling, callbacks, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to implement and troubleshoot WeChat payment, virtual payment, and Official Account OAuth flows in CloudBase applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment credentials may be exposed in code or chat.

Mitigation: Configure credentials in the CloudBase console; keep secrets out of generated code and conversations.

Risk: A frontend success response may be mistaken for confirmed payment.

Mitigation: Confirm payment through a server-side callback or order query before fulfillment.

Risk: Generated payment business logic may be incorrect or incomplete.

Mitigation: Review order validation, callback handling, and idempotency before deployment.

## Reference(s):

- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage.md)
- [Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram.md)
- [Official Account JSAPI Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5.md)
- [Native QR-code Pay](https://docs.cloudbase.net/integration/wechat-pay-native.md)
- [Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth.md)
- [WeChat Mini Program virtual payment](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/virtual-payment)
- [WeChat virtual payment client API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with code and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific payment and OAuth guidance]

## Skill Version(s):

1.2.78 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
