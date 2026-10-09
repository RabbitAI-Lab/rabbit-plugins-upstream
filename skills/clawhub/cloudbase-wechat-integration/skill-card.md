## Description:

Guides developers through WeChat payment, virtual payment, and Official Account OAuth integration with CloudBase.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to build and troubleshoot CloudBase-based WeChat checkout, payment callbacks, virtual-goods purchases, and Official Account sign-in flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated payment or refund code could mishandle order status or fulfillment.

Mitigation: Review callbacks, refunds, idempotency, and order verification; confirm payment server-side before fulfillment.

Risk: Merchant credentials or OAuth secrets could be exposed in code or chat.

Mitigation: Configure secrets in CloudBase or the WeChat console rather than source files or prompts.

Risk: Payment flows may fail or behave unexpectedly in production.

Mitigation: Test with a sandbox or low-value transactions before production use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage.md)
- [Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram.md)
- [Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth.md)
- [WeChat virtual payment API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires review and testing before using generated payment or fulfillment code in production.]

## Skill Version(s):

1.2.61 (source: ClawHub release metadata; packaged skill frontmatter says 2.35.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
