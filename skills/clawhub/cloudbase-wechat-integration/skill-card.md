## Description:

Guides agents through CloudBase Integration Center work for Mini Program WeChat Pay, virtual payment, Official Account JSAPI Pay, Native QR-code Pay, OAuth, openid handling, callbacks, and generated payment functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, debug, or extend WeChat payment, virtual payment, and Official Account OAuth flows in CloudBase applications while keeping credentials in managed configuration and relying on callback or query state for fulfillment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment, refund, fulfillment, or token-storage changes could affect production business state if accepted without review.

Mitigation: Require explicit confirmation before changing those flows and review generated payment code before deployment.

Risk: Merchant keys, private keys, APIv3 keys, AppSecret values, certificates, AppKey values, or session keys could be exposed if copied into source code or chat.

Mitigation: Keep credentials in CloudBase console Integration Center configuration or server-side secret storage, and avoid requesting or persisting secrets in prompts, client code, examples, or commits.

Risk: Frontend payment success callbacks can be mistaken for authoritative payment or fulfillment state.

Mitigation: Use server-side payment callbacks or explicit order queries, with idempotent order updates, before fulfilling goods or updating business records.

Risk: Incorrect generated function names, route paths, payment scenario selection, or openid type can break WeChat payment and OAuth flows.

Mitigation: Inspect the actual CloudBase Integration Center function names and routes, and distinguish Mini Program openid from Official Account openid before writing calls.

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
- [WeChat Mini Program virtual payment](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/virtual-payment)
- [wx.requestVirtualPayment API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline code blocks and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific guidance selected from packaged references; no hidden execution behavior.]

## Skill Version(s):

1.2.44 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
