## Description:

CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, debug, or extend CloudBase WeChat Pay and Official Account OAuth flows. It helps agents route Mini Program Pay, JSAPI Pay, Native QR-code Pay, OAuth, callback, openid, and generated-function troubleshooting tasks to the right implementation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment or OAuth guidance may target the wrong generated CloudBase function name or route.

Mitigation: Verify the actual generated function names and route paths in CloudBase before applying code or configuration changes.

Risk: Merchant keys, certificates, APIv3 keys, or AppSecret values could be exposed if copied into source code or chat.

Mitigation: Keep sensitive values in CloudBase console configuration and avoid including secrets in generated examples, prompts, commits, or client code.

Risk: Client-side payment success can be mistaken for authoritative order completion.

Mitigation: Use server-side payment callbacks or order queries before fulfillment or business-state updates.

Risk: Payment changes can affect live commerce workflows.

Mitigation: Test generated payment and callback behavior carefully with sandbox or low-value transactions before production use.

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
- [CloudBase WeChat Pay JSAPI H5](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md)
- [CloudBase WeChat Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline code examples, checklists, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable components are packaged; outputs should keep merchant and official-account secrets out of code and chat.]

## Skill Version(s):

1.2.41 (source: server release metadata; artifact frontmatter declares 2.32.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
