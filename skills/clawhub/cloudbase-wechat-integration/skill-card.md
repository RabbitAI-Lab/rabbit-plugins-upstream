## Description: <br>
CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add, debug, or extend CloudBase WeChat payment and Official Account OAuth flows, including Mini Program Pay, JSAPI Pay, Native QR-code Pay, generated function extensions, callbacks, and openid handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payment and identity flows may expose merchant keys, AppSecret values, certificates, or other credentials if users place them in chat or source code. <br>
Mitigation: Configure merchant and official-account credentials in CloudBase Integration Center, keep secrets out of prompts and repositories, and preserve generated credential handling. <br>
Risk: Frontend payment success can be mistaken for authoritative fulfillment state. <br>
Mitigation: Confirm payment state through server-side callbacks or order queries, validate order amounts server-side, and make callback updates idempotent before fulfillment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration) <br>
- [CloudBase WeChat Integration Overview](references/overview.md) <br>
- [Mini Program WeChat Pay](references/mini-program-pay.md) <br>
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md) <br>
- [Native QR-Code Pay](references/native-qr-pay.md) <br>
- [Official Account OAuth](references/official-account-oauth.md) <br>
- [WeChat Integration Troubleshooting](references/troubleshooting.md) <br>
- [CloudBase Integration Center Overview](https://docs.cloudbase.net/integration/introduce/index.md) <br>
- [CloudBase Integration Center Usage](https://docs.cloudbase.net/integration/usage/index.md) <br>
- [CloudBase Mini Program WeChat Pay Docs](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md) <br>
- [CloudBase WeChat Pay Native Docs](https://docs.cloudbase.net/integration/wechat-pay-native/index.md) <br>
- [CloudBase WeChat Pay JSAPI H5 Docs](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md) <br>
- [CloudBase Official Account OAuth Docs](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions] <br>
**Output Format:** [Markdown guidance with checklists and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scenario-specific guidance for CloudBase WeChat payment and OAuth flows.] <br>

## Skill Version(s): <br>
1.2.17 (source: server release metadata; artifact frontmatter reports 2.25.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
