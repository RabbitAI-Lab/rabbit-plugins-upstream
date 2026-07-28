## Description: <br>
CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add, debug, or extend WeChat payment and Official Account OAuth flows in CloudBase applications. It guides scenario selection, generated function usage, payment callback handling, order state validation, and credential-safe CloudBase Integration Center setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated guidance may affect real payment order status, fulfillment, callbacks, or token storage. <br>
Mitigation: Review generated code before deployment and verify behavior with function logs, callback logs, and an end-to-end sandbox or low-value production payment test. <br>
Risk: Merchant credentials, private keys, APIv3 keys, AppSecret values, or certificates could be exposed if copied into source code or chat. <br>
Mitigation: Keep credentials in CloudBase Integration Center console configuration and avoid placing secrets in code, prompts, README files, or commits. <br>
Risk: Payment fulfillment can become incorrect if frontend success callbacks are treated as authoritative. <br>
Mitigation: Use server-side payment callbacks or order queries as the source of truth, with idempotent order updates and server-side amount and order validation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration) <br>
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce/index.md) <br>
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage/index.md) <br>
- [Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md) <br>
- [Official Account JSAPI Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md) <br>
- [Native QR-Code Pay](https://docs.cloudbase.net/integration/wechat-pay-native/index.md) <br>
- [Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md) <br>
- [Packaged overview reference](references/overview.md) <br>
- [Packaged troubleshooting reference](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, configuration] <br>
**Output Format:** [Markdown guidance with checklists, scenario routing, and JavaScript code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scenario-specific guidance for CloudBase WeChat payment and OAuth flows; generated code should be reviewed before changes to callbacks, fulfillment, order status, or token storage are deployed.] <br>

## Skill Version(s): <br>
1.2.15 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
