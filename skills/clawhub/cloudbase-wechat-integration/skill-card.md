## Description:

CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, debug, or extend CloudBase WeChat payment and Official Account OAuth flows, including generated function calls, callback handling, order persistence, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment and OAuth work can affect business records if an agent treats client-side success as final payment state.

Mitigation: Confirm paid state through server-side callbacks or order queries, and add idempotent order updates before fulfillment.

Risk: Merchant keys, certificates, APIv3 keys, AppSecret values, and other secrets could be exposed if pasted into chat or committed to source code.

Mitigation: Keep secrets in CloudBase Integration Center console configuration and avoid placing them in prompts, examples, generated files, or commits.

Risk: Generated function names, route paths, and WeChat openid contexts may differ across installations and payment scenarios.

Mitigation: Inspect the actual CloudBase environment, generated function name, route path, and scenario-specific reference before generating or modifying code.

## Reference(s):

- [CloudBase WeChat Integration Overview](references/overview.md)
- [Mini Program WeChat Pay](references/mini-program-pay.md)
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md)
- [Native QR-Code Pay](references/native-qr-pay.md)
- [Official Account OAuth](references/official-account-oauth.md)
- [WeChat Integration Troubleshooting](references/troubleshooting.md)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce/index.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage/index.md)
- [CloudBase Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)
- [CloudBase Native WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-native/index.md)
- [CloudBase JSAPI H5 WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md)
- [CloudBase WeChat Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code snippets, checklists, and troubleshooting steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific guidance for CloudBase WeChat payment and Official Account OAuth work]

## Skill Version(s):

1.2.30 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
