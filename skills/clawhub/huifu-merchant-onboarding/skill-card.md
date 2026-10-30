## Description:

为汇付商户进件与用户开户提供接口选择、字段核对和 SDK 接入指导，并辅助签名、通知与审核排障。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huifu](https://clawhub.ai/user/huifu)

### License/Terms of Use:

MIT-0

## Use Case:

面向汇付支付接入开发者，按商户或用户实体选择开户与进件接口，核对字段和 SDK 调用，并处理签名、通知及审核问题。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PHP examples may allow insecure TLS connections when used for live requests.

Mitigation: Require certificate-chain and hostname verification before live use.

Risk: Upload examples may omit checks for file source, content, format, and size.

Mitigation: Validate the file source, content, permitted format, and size before upload.

Risk: SDK debugging or insufficient authorization can expose sensitive data or allow unintended merchant and account changes.

Mitigation: Keep SDK debugging disabled and authorize each specific merchant or account change.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huifu/skills/huifu-merchant-onboarding)
- [Merchant onboarding overview](references/shared-overview.md)
- [Merchant onboarding field contracts](references/merchant-onboarding-field-contracts.md)
- [Official service source index](references/official-service-source-index.md)
- [Credential and sensitive-data boundary](references/shared-credential-boundary.md)
- [Image upload requirements](references/merchant-onboarding-image-upload.md)
- [Huifu enterprise merchant onboarding API](https://paas.huifu.com/partners/api/doc/shgl/shjj/api_shjj_qyshjbxxrz_kyc.md)
- [Huifu merchant business opening API](https://paas.huifu.com/partners/api/doc/shgl/shywkt/api_shjj_shywkt_kyc.md)
- [Huifu user onboarding API source index](references/user-onboarding-official-service-source-index.md)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Code, Configuration, Markdown]

**Output Format:** [Markdown guidance with field tables, API examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tailored to the selected merchant or user onboarding flow and SDK.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
