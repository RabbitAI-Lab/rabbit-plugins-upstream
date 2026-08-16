## Description:

CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, debug, or extend WeChat payment and Official Account OAuth flows in CloudBase applications. It guides scenario selection, generated function calls, callback handling, order validation, and CloudBase console configuration without collecting merchant secrets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment and OAuth guidance may affect order creation, callback handling, fulfillment, and user identity flows.

Mitigation: Confirm generated function names and route paths, validate amounts and order ownership server-side, and test with sandbox or low-value orders before production use.

Risk: Merchant credentials, private keys, APIv3 keys, AppSecret values, and certificates could be exposed if copied into source code or chat.

Mitigation: Keep credentials in CloudBase Integration Center configuration and avoid placing secrets in generated examples, prompts, commits, or frontend code.

Risk: Frontend payment success callbacks can be mistaken for authoritative payment state.

Mitigation: Use payment callbacks or explicit order queries as the source of truth, and make callback-side order updates idempotent.

## Reference(s):

- [CloudBase WeChat Integration skill page](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce/index.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage/index.md)
- [Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)
- [Native QR-code Pay](https://docs.cloudbase.net/integration/wechat-pay-native/index.md)
- [Official Account JSAPI Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md)
- [Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md)
- [Artifact: overview.md](references/overview.md)
- [Artifact: mini-program-pay.md](references/mini-program-pay.md)
- [Artifact: official-account-jsapi-pay.md](references/official-account-jsapi-pay.md)
- [Artifact: native-qr-pay.md](references/native-qr-pay.md)
- [Artifact: official-account-oauth.md](references/official-account-oauth.md)
- [Artifact: troubleshooting.md](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions, Analysis]

**Output Format:** [Markdown with inline code examples and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CloudBase console steps, generated function call examples, callback and order-validation guidance, and troubleshooting checks.]

## Skill Version(s):

1.2.29 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
