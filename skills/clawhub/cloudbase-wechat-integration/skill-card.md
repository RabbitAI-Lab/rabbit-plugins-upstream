## Description: <br>
CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add, debug, or extend CloudBase WeChat payment and Official Account OAuth flows. It guides scenario routing, generated function calls, callback handling, order validation, idempotency, and console-based credential setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated code or guidance may affect payment and identity workflows. <br>
Mitigation: Review generated changes before production use and test payment flows with a sandbox or low-value production transaction. <br>
Risk: Merchant keys, private keys, APIv3 keys, AppSecret values, or certificates could be exposed if copied into source code or chat. <br>
Mitigation: Keep credentials in CloudBase Integration Center console configuration and avoid embedding secrets in prompts, repositories, or frontend code. <br>
Risk: Frontend payment success callbacks can be mistaken for authoritative fulfillment state. <br>
Mitigation: Confirm paid state through server-side order queries or verified payment callbacks before updating business records or fulfillment. <br>
Risk: Using an assumed generated function name or route can break payment, OAuth, or callback flows. <br>
Mitigation: Inspect the CloudBase Integration Center generated function name and route paths before writing calls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration) <br>
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce/index.md) <br>
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage/index.md) <br>
- [CloudBase Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md) <br>
- [CloudBase WeChat Pay Native](https://docs.cloudbase.net/integration/wechat-pay-native/index.md) <br>
- [CloudBase WeChat Pay JSAPI H5](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md) <br>
- [CloudBase WeChat Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md) <br>
- [CloudBase WeChat Integration Overview](references/overview.md) <br>
- [Mini Program WeChat Pay](references/mini-program-pay.md) <br>
- [Native QR-Code Pay](references/native-qr-pay.md) <br>
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md) <br>
- [Official Account OAuth](references/official-account-oauth.md) <br>
- [WeChat Integration Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill produces agent guidance and implementation snippets; it does not execute code or deploy resources by itself.] <br>

## Skill Version(s): <br>
1.2.20 (source: server release metadata; artifact frontmatter version: 2.25.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
