## Description:

CloudBase WeChat Integration guides agents in adding, debugging, and extending Mini Program WeChat Pay, Official Account JSAPI Pay, Native QR-code Pay, Official Account OAuth, openid handling, payment callbacks, and CloudBase Integration Center generated functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement or troubleshoot CloudBase-backed WeChat payment and Official Account OAuth flows, including generated function calls, callback handling, idempotency, fulfillment, and openid routing. It is intended for application-side integration work that must keep credentials in CloudBase console configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated changes to payment flows could mishandle order amounts, callback idempotency, fulfillment, or payment status.

Mitigation: Review generated changes carefully, validate amounts and order ownership server-side, and treat payment callbacks or order queries as the authoritative business state.

Risk: Merchant keys, APIv3 keys, private keys, AppSecret values, certificates, or OAuth credentials could be exposed in chat or source code.

Mitigation: Configure secrets only in the CloudBase console Integration Center form and keep generated credential handling out of prompts, commits, and client code.

Risk: OAuth and generated callback behavior could be broken by replacing platform-managed verification, decryption, token handling, or environment variables.

Mitigation: Preserve generated verification and decryption logic, keep required environment variables intact, and add business logic around the generated handlers.

## Reference(s):

- [Mini Program WeChat Pay](references/mini-program-pay.md)
- [Native QR-Code Pay](references/native-qr-pay.md)
- [Official Account JSAPI Pay](references/official-account-jsapi-pay.md)
- [Official Account OAuth](references/official-account-oauth.md)
- [CloudBase WeChat Integration Overview](references/overview.md)
- [WeChat Integration Troubleshooting](references/troubleshooting.md)
- [CloudBase Integration Center Overview](https://docs.cloudbase.net/integration/introduce/index.md)
- [CloudBase Integration Center Usage](https://docs.cloudbase.net/integration/usage/index.md)
- [CloudBase Mini Program WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)
- [CloudBase Native WeChat Pay](https://docs.cloudbase.net/integration/wechat-pay-native/index.md)
- [CloudBase WeChat Pay JSAPI H5](https://docs.cloudbase.net/integration/wechat-pay-jsapi-h5/index.md)
- [CloudBase WeChat Official Account OAuth](https://docs.cloudbase.net/integration/wechat-official-oauth/index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline code examples, checklists, and scenario-specific troubleshooting steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be adapted to the user's actual CloudBase environment ID, generated function names, routes, and WeChat payment or OAuth scenario.]

## Skill Version(s):

1.2.38 (source: server release metadata; artifact frontmatter reports 2.32.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
