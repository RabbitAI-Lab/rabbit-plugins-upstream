## Description:

Guides developers in adding, debugging, and extending CloudBase WeChat payment, virtual payment, and Official Account OAuth flows using the Integration Center.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to implement and troubleshoot Mini Program, Official Account JSAPI, Native QR-code, virtual payment, OAuth, and payment callback flows in CloudBase, including console setup and reliable order-state handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A production payment test may charge real money without requiring explicit approval.

Mitigation: Prefer sandbox testing; before any production test, explain possible charges, fees, and fulfillment effects and require the user's approval.

Risk: The security scan was partial because three local references could not be resolved, so those references were not covered.

Mitigation: Review the unavailable references before relying on the scan's coverage.

## Reference(s):

- [CloudBase WeChat Integration Overview](references/overview.md)
- [Mini Program WeChat Pay](references/mini-program-pay.md)
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md)
- [Native QR-Code Pay](references/native-qr-pay.md)
- [Official Account OAuth](references/official-account-oauth.md)
- [Mini Program Virtual Payment](references/virtual-payment.md)
- [WeChat Integration Troubleshooting](references/troubleshooting.md)
- [CloudBase Integration Center Overview](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase Integration Center Usage](https://docs.cloudbase.net/integration/usage.md)
- [WeChat Mini Program Virtual Payment](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/virtual-payment)
- [wx.requestVirtualPayment API](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, API calls]

**Output Format:** [Markdown with inline code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific instructions and code examples; generated function names and paths should be confirmed from the user's CloudBase setup.]

## Skill Version(s):

1.2.89 (source: server-resolved ClawHub release; artifact frontmatter states 2.37.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
