## Description:

CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, debug, or extend WeChat payment and Official Account OAuth flows in CloudBase applications. It focuses on CloudBase Integration Center generated functions, callback handling, openid handling, credential boundaries, and scenario-specific payment guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment and OAuth work can expose merchant keys, AppSecret values, certificates, or APIv3 keys if handled in chat or source code.

Mitigation: Use the skill only in relevant CloudBase projects and keep credentials in CloudBase console configuration rather than prompts, commits, or application source.

Risk: Frontend payment success can be mistaken for authoritative business payment state.

Mitigation: Confirm paid state through server-side query results or verified payment callbacks before fulfillment or order-status updates.

Risk: Generated CloudBase Integration Center function names and routes may differ from examples.

Mitigation: Inspect the actual generated function name and route before writing calls, and preserve generated credential handling and callback verification logic when extending functions.

## Reference(s):

- [CloudBase WeChat Integration skill page](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
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
- [CloudBase Official Account JSAPI Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md)
- [CloudBase Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific guidance for CloudBase WeChat Pay and Official Account OAuth flows]

## Skill Version(s):

1.2.28 (source: server release metadata; artifact frontmatter lists 2.26.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
