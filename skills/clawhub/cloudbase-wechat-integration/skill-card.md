## Description:

Guides developers through CloudBase integrations for WeChat payments, virtual goods payments, Official Account OAuth, and payment callback handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and troubleshoot WeChat payment and Official Account flows in CloudBase apps, including order creation, OAuth, callbacks, and fulfillment checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Merchant secrets or OAuth credentials could be exposed in source code or chat.

Mitigation: Configure credentials in the CloudBase console and keep them out of generated code, commits, and prompts.

Risk: Trusting a client-side payment success response could trigger incorrect fulfillment or refunds.

Mitigation: Review payment and refund changes before production; verify paid state through server-side callbacks or order queries and enforce idempotency.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce.md)
- [Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram.md)
- [Official Account JSAPI Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5.md)
- [Native QR-code Pay](https://docs.cloudbase.net/integration/wechat-pay-native.md)
- [Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth.md)
- [WeChat Mini Program virtual payment API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapt generated examples to the actual CloudBase environment and integration routes.]

## Skill Version(s):

1.2.67 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
