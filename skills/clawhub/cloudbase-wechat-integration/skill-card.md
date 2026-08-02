## Description: <br>
CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add, debug, or extend CloudBase WeChat payment and Official Account OAuth flows while keeping CloudBase Integration Center setup console-first. It supports Mini Program Pay, Official Account JSAPI Pay, Native QR-code Pay, OAuth openid handling, generated-function extension, and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents using this skill may modify payment fulfillment or OAuth token-storage code where mistakes can affect money movement, account identity, or user access. <br>
Mitigation: Review generated code before production use, confirm payment state through server-side callbacks or order queries, and test with a sandbox or low-value production transaction. <br>
Risk: Merchant keys, APIv3 keys, certificates, private keys, or AppSecret values could be exposed if placed in source code or chat. <br>
Mitigation: Keep credentials in CloudBase console Integration Center configuration and avoid pasting secrets into prompts, generated examples, commits, or documentation. <br>


## Reference(s): <br>
- [CloudBase WeChat Integration Overview](references/overview.md) <br>
- [Mini Program WeChat Pay](references/mini-program-pay.md) <br>
- [Native QR-Code Pay](references/native-qr-pay.md) <br>
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md) <br>
- [Official Account OAuth](references/official-account-oauth.md) <br>
- [WeChat Integration Troubleshooting](references/troubleshooting.md) <br>
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce/index.md) <br>
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage/index.md) <br>
- [CloudBase Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md) <br>
- [CloudBase WeChat Pay Native](https://docs.cloudbase.net/integration/wechat-pay-native/index.md) <br>
- [CloudBase WeChat Pay JSAPI H5](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md) <br>
- [CloudBase WeChat Official OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline code and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scenario-specific guidance for CloudBase WeChat payment and Official Account OAuth workflows.] <br>

## Skill Version(s): <br>
1.2.18 (source: server release metadata; artifact frontmatter reports 2.25.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
