## Description:

Guides developers through CloudBase WeChat payment, virtual payment, Official Account OAuth, callbacks, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers integrating WeChat payments or Official Account sign-in with CloudBase use this skill to select the right flow, generate client and server guidance, and troubleshoot orders, callbacks, and OAuth identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect payment confirmation could fulfill unpaid orders.

Mitigation: Verify paid status with a server-side callback or order query; validate order and amount, and make fulfillment idempotent.

Risk: Exposing merchant credentials or OAuth secrets in source code or chat.

Mitigation: Configure credentials in the CloudBase console and keep them out of code, logs, and prompts.

Risk: Unverified changes to payment or OAuth flows can disrupt transactions or account access.

Mitigation: Review generated code and test with sandbox or low-value transactions before production use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage.md)
- [Mini Program WeChat Pay](references/mini-program-pay.md)
- [Mini Program virtual payment](references/virtual-payment.md)
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md)
- [Native QR-code Pay](references/native-qr-pay.md)
- [Official Account OAuth](references/official-account-oauth.md)
- [WeChat integration troubleshooting](references/troubleshooting.md)
- [WeChat integration overview](references/overview.md)
- [WeChat virtual payment API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapt examples to the actual CloudBase environment and generated function names.]

## Skill Version(s):

1.2.66 (source: ClawHub release; artifact frontmatter: 2.35.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
