## Description:

CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, debug, or extend WeChat payment and Official Account OAuth flows in CloudBase applications. It supports scenario routing, generated-function integration, callback/query confirmation, and safe handling of payment and OAuth credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Merchant keys, APIv3 keys, private keys, certificates, or AppSecret values could be exposed while implementing payment or OAuth flows.

Mitigation: Keep secrets in CloudBase console Integration Center configuration and do not place them in source code, prompts, commits, or browser-accessible code.

Risk: Client-side payment success could be mistaken for authoritative fulfillment state.

Mitigation: Use server-side payment callbacks or explicit order queries before updating business records or fulfilling orders.

Risk: Using assumed generated function names or routes could break payment and OAuth flows.

Mitigation: Confirm the actual generated function name and route paths in the CloudBase console or generated function docs before writing calls.

## Reference(s):

- [CloudBase WeChat Integration Overview](references/overview.md)
- [Mini Program WeChat Pay](references/mini-program-pay.md)
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md)
- [Native QR-Code Pay](references/native-qr-pay.md)
- [Official Account OAuth](references/official-account-oauth.md)
- [WeChat Integration Troubleshooting](references/troubleshooting.md)
- [CloudBase Integration Center Overview](https://docs.cloudbase.net/integration/introduce/index.md)
- [CloudBase Integration Center Usage](https://docs.cloudbase.net/integration/usage/index.md)
- [CloudBase Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)
- [CloudBase Native WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-native/index.md)
- [CloudBase JSAPI H5 WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md)
- [CloudBase Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code examples, checklists, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario-specific output for CloudBase WeChat Pay, Official Account OAuth, callback handling, and troubleshooting.]

## Skill Version(s):

1.2.40 (source: server release metadata; artifact frontmatter: 2.32.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
