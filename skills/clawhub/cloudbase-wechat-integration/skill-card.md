## Description:

Guides CloudBase developers through WeChat payment, virtual payment, and Official Account OAuth integrations, including callbacks and order verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to implement and troubleshoot CloudBase WeChat Pay, virtual goods payments, and Official Account sign-in while handling order state and callbacks safely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment credentials or OAuth secrets may be exposed in source code or chat.

Mitigation: Configure credentials in the CloudBase console; do not paste secrets into chat or commit them to source code.

Risk: Frontend success alone may be mistaken for a completed payment, leading to incorrect fulfillment.

Mitigation: Validate orders server-side and confirm fulfillment from verified callbacks or server-side payment queries.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage.md)
- [WeChat virtual payment API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)
- [Payment and OAuth troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tailored to the selected WeChat payment or OAuth flow.]

## Skill Version(s):

1.2.80 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
