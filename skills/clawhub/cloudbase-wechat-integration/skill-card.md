## Description:

CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, debug, or extend WeChat payment and Official Account OAuth flows in CloudBase applications. It helps route work across Mini Program Pay, Official Account JSAPI Pay, Native QR-code Pay, callback handling, openid handling, and CloudBase Integration Center generated functions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated payment and OAuth code can affect real orders and user identifiers.

Mitigation: Keep merchant keys, AppSecrets, certificates, and APIv3 keys in CloudBase console configuration; confirm fulfillment through callback or order-query state; test with sandbox or low-value payments before production use.

Risk: Using the wrong generated function name, route, or openid type can break payment or OAuth flows.

Mitigation: Confirm the actual CloudBase environment ID, generated function name, route path, and scenario-specific openid before changing client or backend code.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce/index.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage/index.md)
- [CloudBase WeChat Mini Program Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)
- [CloudBase WeChat Native Pay](https://docs.cloudbase.net/integration/wechat-pay-native/index.md)
- [CloudBase WeChat JSAPI H5 Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md)
- [CloudBase WeChat Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md)
- [Mini Program WeChat Pay](references/mini-program-pay.md)
- [Native QR-Code Pay](references/native-qr-pay.md)
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md)
- [Official Account OAuth](references/official-account-oauth.md)
- [CloudBase WeChat Integration Overview](references/overview.md)
- [WeChat Integration Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with inline code and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific guidance for CloudBase WeChat payment and Official Account OAuth flows.]

## Skill Version(s):

1.2.37 (source: ClawHub release metadata; artifact frontmatter reports 2.32.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
