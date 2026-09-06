## Description:

CloudBase WeChat Integration guides agents through adding, debugging, and extending Mini Program WeChat Pay, virtual payment, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement and troubleshoot CloudBase WeChat payment and Official Account OAuth flows. It helps identify the correct scenario, load the matching reference material, keep credentials in CloudBase console configuration, and add callback or query based fulfillment checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated payment changes can affect money movement, refunds, and fulfillment.

Mitigation: Verify the CloudBase environment, generated function names, callback routes, credential configuration, idempotency, amount validation, and callback or query based paid-state checks before relying on generated changes.

Risk: Frontend payment success can be mistaken for final business fulfillment.

Mitigation: Use server-side callback handling or order-query results as the authoritative paid state, then test with sandbox or a low-value production payment as applicable.

Risk: Credential handling mistakes can expose merchant secrets or break callback verification.

Mitigation: Keep merchant credentials, private keys, APIv3 keys, AppSecret values, and certificates in CloudBase Integration Center configuration, and preserve generated verification and decryption logic when extending functions.

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

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline code examples and implementation checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific guidance for CloudBase WeChat payment and OAuth flows]

## Skill Version(s):

1.2.43 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
