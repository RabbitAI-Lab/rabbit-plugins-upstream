## Description:

CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, debug, or extend WeChat payment and Official Account OAuth flows in CloudBase applications. It helps route Mini Program Pay, JSAPI Pay, Native QR-code Pay, openid handling, callbacks, and generated CloudBase Integration Center functions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment and OAuth work may expose merchant keys, private keys, APIv3 keys, certificates, or AppSecrets if credentials are copied into chat or source code.

Mitigation: Keep credentials in the CloudBase Integration Center console configuration and do not ask users to paste secrets into chat, generated examples, README files, commits, or application source code.

Risk: Frontend payment success callbacks can be mistaken for final business truth, causing incorrect order fulfillment.

Mitigation: Use server-side payment callbacks or order-query results as the authoritative state, and add amount validation, order persistence, idempotency, and fulfillment checks around generated functions.

Risk: Assuming generated function names, route paths, or Integration Center management APIs can produce broken payment or OAuth flows.

Mitigation: Confirm the actual CloudBase environment ID, generated function name, route path, and official documentation before changing code or issuing calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase-wechat-integration)
- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce/index.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage/index.md)
- [Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)
- [Native QR-code Pay](https://docs.cloudbase.net/integration/wechat-pay-native/index.md)
- [Official Account JSAPI Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md)
- [Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md)
- [CloudBase WeChat Integration Overview](references/overview.md)
- [Mini Program WeChat Pay reference](references/mini-program-pay.md)
- [Official Account JSAPI Pay reference](references/official-account-jsapi-pay.md)
- [Native QR-code Pay reference](references/native-qr-pay.md)
- [Official Account OAuth reference](references/official-account-oauth.md)
- [WeChat Integration Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, checklists, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focuses on user-directed setup, troubleshooting, and business-logic extensions while keeping secrets out of chat and source code.]

## Skill Version(s):

1.2.26 (source: server release metadata; artifact frontmatter reports 2.25.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
