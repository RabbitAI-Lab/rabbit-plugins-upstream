## Description:

Guides agents through CloudBase-backed WeChat Pay, virtual payment, Official Account JSAPI Pay, Native QR-code Pay, OAuth, callbacks, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add, debug, or extend WeChat payment, virtual payment, Official Account OAuth, and callback flows in CloudBase applications. It helps route agents to the right scenario guidance while keeping secrets in CloudBase configuration and payment fulfillment tied to callback or query-confirmed state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated payment, refund, callback, or fulfillment changes can affect real transactions.

Mitigation: Review generated code before production use and test first with sandbox flows or low-value transactions.

Risk: Merchant credentials, private keys, APIv3 keys, AppSecret values, or certificates could be exposed if placed in code or chat.

Mitigation: Keep credentials in CloudBase console configuration and avoid requesting or embedding secrets in source files, prompts, or documentation.

Risk: Client-side payment success can be mistaken for final business state.

Mitigation: Use server-side callbacks or order-query results as the authoritative basis for fulfillment, refunds, and status updates.

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
- [CloudBase Official Account JSAPI Pay documentation](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5.md)
- [CloudBase Native WeChat Pay documentation](https://docs.cloudbase.net/integration/wechat-pay-native.md)
- [CloudBase Official Account OAuth documentation](https://docs.cloudbase.net/integration/wechat-official-oauth.md)
- [WeChat requestVirtualPayment API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; outputs should be reviewed before applying to real payment, refund, callback, or fulfillment flows.]

## Skill Version(s):

1.2.46 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
