## Description:

Guides agents through CloudBase WeChat payment and Official Account OAuth integrations, including setup, application code, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to build and troubleshoot CloudBase Mini Program, virtual, JSAPI, and QR-code payments and Official Account OAuth flows, including order confirmation and callback handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Merchant keys, AppSecrets, certificates, or other payment credentials could be exposed in code or chat.

Mitigation: Configure credentials in official consoles; do not put them in source code or prompts.

Risk: Incorrect payment or fulfillment logic could affect real orders.

Mitigation: Review generated code, confirm payment through server-side callbacks or queries, and test in a sandbox or with low-value orders before production use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage.md)
- [WeChat Mini Program Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram.md)
- [WeChat Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth.md)
- [WeChat virtual payment API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)
- [Packaged scenario guides and troubleshooting](artifact/references/overview.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Payment completion requires a verified server-side callback or order query.]

## Skill Version(s):

1.2.64 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
