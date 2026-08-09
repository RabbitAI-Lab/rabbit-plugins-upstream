## Description:

CloudBase WeChat integration guide for Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, debug, or extend WeChat payment and Official Account OAuth flows in CloudBase applications while keeping credential setup in CloudBase Integration Center.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment or OAuth changes can expose merchant keys, AppSecrets, private keys, APIv3 keys, or certificates if credentials are copied into source code or chat.

Mitigation: Keep secrets in the CloudBase console Integration Center configuration and avoid placing them in prompts, generated examples, commits, or frontend code.

Risk: Incorrect generated function names, routes, or client context can break payment and OAuth flows.

Mitigation: Verify the actual CloudBase environment ID, generated function name, route path, and target scenario before generating or changing code.

Risk: Treating frontend payment success or QR-code generation as final business state can cause incorrect fulfillment.

Mitigation: Require server-side payment callback handling or explicit order query confirmation before updating paid order state or fulfillment.

## Reference(s):

- [CloudBase Integration Center overview](https://docs.cloudbase.net/integration/introduce/index.md)
- [CloudBase Integration Center usage](https://docs.cloudbase.net/integration/usage/index.md)
- [Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)
- [Native WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-native/index.md)
- [Official Account JSAPI Pay](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md)
- [Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md)
- [CloudBase WeChat Integration Overview](references/overview.md)
- [Mini Program WeChat Pay Reference](references/mini-program-pay.md)
- [Native QR-Code Pay Reference](references/native-qr-pay.md)
- [Official Account JSAPI Pay Reference](references/official-account-jsapi-pay.md)
- [Official Account OAuth Reference](references/official-account-oauth.md)
- [WeChat Integration Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focuses on scenario-specific CloudBase and WeChat payment or OAuth guidance; does not produce executable install behavior.]

## Skill Version(s):

1.2.27 (source: server release metadata; artifact frontmatter reports 2.25.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
