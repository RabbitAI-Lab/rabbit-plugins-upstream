## Description:

Guides developers through CloudBase WeChat payments and Official Account integration, including client flows, generated functions, OAuth, callbacks, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers building or debugging CloudBase apps use this skill to integrate Mini Program and Official Account payments, virtual purchases, OAuth, and reliable order fulfillment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Merchant credentials or certificates could be exposed in source code or chat.

Mitigation: Configure secrets in CloudBase Integration Center; do not embed or request them in prompts or generated code.

Risk: Client-side payment success or unvalidated amounts could trigger incorrect fulfillment.

Mitigation: Validate orders and amounts on the server, confirm payment by callback or server-side query, and fulfill idempotently.

Risk: Changes to generated payment functions could break callback verification or credential handling.

Mitigation: Preserve generated verification and credential logic, and review and test changes before live use.

## Reference(s):

- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage.md)
- [CloudBase Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram.md)
- [CloudBase Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth.md)
- [WeChat Mini Program virtual payment](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/virtual-payment)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific integration and troubleshooting guidance; no payment confirmation without server-side verification.]

## Skill Version(s):

1.2.71 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
