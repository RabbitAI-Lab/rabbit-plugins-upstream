## Description:

Guides agents through CloudBase WeChat Pay and Official Account OAuth work, including Mini Program Pay, Official Account JSAPI Pay, Native QR-code Pay, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, debug, or extend WeChat payment and Official Account OAuth flows in CloudBase applications while preserving Integration Center credential handling and callback verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment and OAuth work can expose merchant keys, certificates, APIv3 keys, AppSecret values, or tokens if handled in chat or source code.

Mitigation: Keep secrets in CloudBase console or secure backend configuration, and avoid placing credentials in prompts, client code, generated examples, or commits.

Risk: Generated payment code can incorrectly update orders, issue refunds, or fulfill purchases.

Mitigation: Review generated payment code before use, validate amount and order ownership server-side, and require callback or query confirmation before fulfillment.

Risk: Frontend payment success can be mistaken for authoritative business state.

Mitigation: Use server-side query results or verified payment callbacks as the final payment state, with idempotent order updates.

Risk: Using assumed generated function names or routes can break payment and OAuth flows.

Mitigation: Confirm the actual CloudBase Integration Center function name, route paths, environment ID, and logs before changing payment or callback code.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
- [CloudBase WeChat Integration Overview](references/overview.md)
- [Mini Program WeChat Pay](references/mini-program-pay.md)
- [Native QR-Code Pay](references/native-qr-pay.md)
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md)
- [Official Account OAuth](references/official-account-oauth.md)
- [WeChat Integration Troubleshooting](references/troubleshooting.md)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce/index.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage/index.md)
- [CloudBase Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)
- [CloudBase Native WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-native/index.md)
- [CloudBase JSAPI/H5 WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md)
- [CloudBase Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown with inline code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific guidance for payment and OAuth flows; generated code should be reviewed before it updates orders, issues refunds, or fulfills purchases.]

## Skill Version(s):

1.2.39 (source: server release metadata; artifact frontmatter reports 2.32.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
