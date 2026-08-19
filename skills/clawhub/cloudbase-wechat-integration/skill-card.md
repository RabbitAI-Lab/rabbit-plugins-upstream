## Description:

CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add, debug, or extend WeChat payment and Official Account OAuth flows in CloudBase apps. It guides scenario routing, generated function usage, callback-based payment confirmation, and safe handling of merchant and official-account credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment and OAuth changes can affect orders, tokens, and fulfillment.

Mitigation: Use the skill only for CloudBase WeChat Pay or Official Account OAuth work, confirm generated function names, and require server-side callback or query confirmation before changing business state.

Risk: Merchant secrets, private keys, APIv3 keys, AppSecret values, or certificates could be exposed if copied into source code or chat.

Mitigation: Keep credentials in the CloudBase console Integration Center configuration and avoid requesting or storing secrets in generated code, examples, commits, or prompts.

Risk: Generated function names and route paths may vary across CloudBase Integration Center setups.

Mitigation: Inspect the actual generated function name and route paths before writing client calls, backend wrappers, or callback logic.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce/index.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage/index.md)
- [Mini Program WeChat Pay](references/mini-program-pay.md)
- [Native QR-Code Pay](references/native-qr-pay.md)
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md)
- [Official Account OAuth](references/official-account-oauth.md)
- [CloudBase WeChat Integration Overview](references/overview.md)
- [WeChat Integration Troubleshooting](references/troubleshooting.md)
- [CloudBase Mini Program WeChat Pay documentation](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)
- [CloudBase Native WeChat Pay documentation](https://docs.cloudbase.net/integration/wechat-pay-native/index.md)
- [CloudBase Official Account JSAPI Pay documentation](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md)
- [CloudBase Official Account OAuth documentation](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific guidance should be grounded in the matching packaged reference and official CloudBase documentation.]

## Skill Version(s):

1.2.31 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
