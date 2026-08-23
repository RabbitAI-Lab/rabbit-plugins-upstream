## Description:

CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement, extend, or troubleshoot CloudBase WeChat Pay and Official Account OAuth flows. It helps agents choose the correct scenario reference, keep payment and identity credentials in CloudBase Integration Center, and rely on callback or order-query state before fulfillment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports real payment and identity-data workflows where mishandled secrets or callbacks could affect production systems.

Mitigation: Keep merchant keys, AppSecrets, certificates, and APIv3 keys in CloudBase console configuration, review generated payment and callback code, and test with sandbox or low-value transactions before production use.

Risk: Client-side payment success can be mistaken for final business confirmation.

Mitigation: Use server-side payment callbacks or explicit order queries as the authoritative payment state before fulfillment.

Risk: Generated function names and routes can differ from examples in the skill references.

Mitigation: Inspect the actual CloudBase Integration Center function name and route paths before generating or changing calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce/index.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage/index.md)
- [CloudBase WeChat Pay for Mini Program](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)
- [CloudBase WeChat Pay Native](https://docs.cloudbase.net/integration/wechat-pay-native/index.md)
- [CloudBase WeChat Pay JSAPI H5](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md)
- [CloudBase WeChat Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md)
- [Mini Program WeChat Pay](references/mini-program-pay.md)
- [Native QR-Code Pay](references/native-qr-pay.md)
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md)
- [Official Account OAuth](references/official-account-oauth.md)
- [CloudBase WeChat Integration Overview](references/overview.md)
- [WeChat Integration Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code blocks, checklists, and scenario-specific guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include client or cloud function code shapes and troubleshooting steps; should not include merchant keys, AppSecrets, certificates, or APIv3 keys.]

## Skill Version(s):

1.2.35 (source: server release metadata; artifact frontmatter declares 2.31.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
