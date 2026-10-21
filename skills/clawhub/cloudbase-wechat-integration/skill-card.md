## Description:

Guides developers through WeChat payments and Official Account OAuth integrations on CloudBase.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add, debug, and extend CloudBase WeChat Mini Program and virtual payments, Official Account JSAPI and OAuth flows, Native QR payments, and related order and callback handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Merchant and Official Account credentials could be exposed or mishandled during setup.

Mitigation: Keep credentials in the CloudBase console Integration Center; do not paste secrets into chat or application code.

Risk: Unreviewed payment or deployment changes and uncoordinated live tests may affect transactions.

Mitigation: Review payment and deployment changes, agree on any live payment tests, and verify current virtual-payment settings and fees against official documentation.

Risk: Treating client-side payment success as proof of payment could trigger incorrect fulfillment.

Mitigation: Confirm payment state using server-side callbacks or order queries before updating business data or fulfilling orders.

## Reference(s):

- [CloudBase WeChat Integration Overview](references/overview.md)
- [Mini Program WeChat Pay](references/mini-program-pay.md)
- [Mini Program Virtual Payment](references/virtual-payment.md)
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md)
- [Native QR-Code Pay](references/native-qr-pay.md)
- [Official Account OAuth](references/official-account-oauth.md)
- [WeChat Integration Troubleshooting](references/troubleshooting.md)
- [CloudBase Integration Center Overview](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase Integration Center Usage](https://docs.cloudbase.net/integration/usage.md)
- [CloudBase Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram.md)
- [CloudBase Native WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-native.md)
- [CloudBase Official Account JSAPI Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5.md)
- [CloudBase Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth.md)
- [WeChat Mini Program Virtual Payment](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/virtual-payment)
- [wx.requestVirtualPayment API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration]

**Output Format:** [Markdown with inline code, checklists, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific integration guidance and examples; confirm current platform documentation and generated function details before use.]

## Skill Version(s):

1.2.82 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
