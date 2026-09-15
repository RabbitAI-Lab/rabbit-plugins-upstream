## Description:

CloudBase WeChat integration guide for Mini Program WeChat Pay, Mini Program virtual payment, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add, debug, or extend WeChat payment, virtual payment, Official Account OAuth, and callback flows in CloudBase applications while keeping credentials and payment state handling on trusted backend paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth examples or implementations may expose more token data to browser code than necessary.

Mitigation: Keep access and refresh tokens on the backend, return only minimal client-safe data or establish a secure server-managed session, and add single-use OAuth state validation.

Risk: Payment or virtual-payment fulfillment may be incorrectly triggered from frontend success callbacks.

Mitigation: Treat callbacks or server-side order queries as authoritative, persist pending orders, validate amount and ownership on the backend, and make fulfillment idempotent.

Risk: Merchant keys, AppSecrets, APIv3 keys, AppKeys, certificates, or session keys may be copied into source code or chat.

Mitigation: Configure secrets in CloudBase Integration Center or trusted backend configuration and avoid placing them in client code, repository files, prompts, or examples.

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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CloudBase console setup guidance, scenario-specific implementation checks, and troubleshooting steps.]

## Skill Version(s):

1.2.50 (source: server release metadata; artifact frontmatter version is 2.34.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
