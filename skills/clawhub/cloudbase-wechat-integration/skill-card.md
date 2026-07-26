## Description: <br>
CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add, debug, or extend WeChat payment and Official Account OAuth flows on CloudBase. It guides scenario selection, generated function usage, callback handling, order-state validation, credential placement, and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payment fulfillment could be triggered from frontend success signals instead of authoritative server-side payment state. <br>
Mitigation: Use payment callbacks or explicit order queries before updating business records or fulfilling orders. <br>
Risk: Merchant secrets, APIv3 keys, private keys, AppSecret values, or certificates could be exposed in source code, generated examples, commits, or chat. <br>
Mitigation: Keep credentials in CloudBase Integration Center configuration and preserve generated credential handling when extending functions. <br>
Risk: Generated CloudBase function names and routes may differ from examples such as pay-common or offiaccount-common. <br>
Mitigation: Inspect the actual Integration Center generated function name and route before generating calls or troubleshooting code. <br>
Risk: Official Account and Mini Program openid values can be confused, causing payment or OAuth failures. <br>
Mitigation: Confirm the client context and AppID binding, then use the openid from the matching Mini Program or Official Account flow. <br>


## Reference(s): <br>
- [CloudBase WeChat Integration Skill Page](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration) <br>
- [CloudBase Integration Center Overview](https://docs.cloudbase.net/integration/introduce/index.md) <br>
- [CloudBase Integration Center Usage](https://docs.cloudbase.net/integration/usage/index.md) <br>
- [CloudBase WeChat Pay Mini Program](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md) <br>
- [CloudBase WeChat Pay JSAPI H5](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md) <br>
- [CloudBase WeChat Pay Native](https://docs.cloudbase.net/integration/wechat-pay-native/index.md) <br>
- [CloudBase WeChat Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md) <br>
- [Mini Program WeChat Pay](artifact/references/mini-program-pay.md) <br>
- [Native QR-Code Pay](artifact/references/native-qr-pay.md) <br>
- [Official Account JSAPI Pay](artifact/references/official-account-jsapi-pay.md) <br>
- [Official Account OAuth](artifact/references/official-account-oauth.md) <br>
- [WeChat Integration Troubleshooting](artifact/references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with code snippets, checklists, and configuration steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scenario-specific output depends on the selected WeChat Pay or Official Account OAuth flow.] <br>

## Skill Version(s): <br>
1.2.14 (source: server release metadata; artifact frontmatter reports 2.24.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
