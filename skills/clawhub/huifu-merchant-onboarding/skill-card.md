## Description:

帮助开发者集成汇付支付/斗拱支付的商户进件、用户开户、KYC、资料上传、业务开通、状态查询和商户管理流程。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huifu](https://clawhub.ai/user/huifu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and integration teams use this skill to select the correct Huifu merchant or user onboarding route, draft API requests, verify field contracts, and understand SDK, signing, credential, status, and notification boundaries for sensitive financial onboarding workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated onboarding guidance can affect sensitive financial, KYC, merchant, or user account workflows.

Mitigation: Confirm the target entity, subject type, API route, environment, credentials boundary, and materials source before using generated API calls.

Risk: RSA keys, identity documents, bank card data, phone numbers, and uploaded KYC materials may be exposed if copied into logs, front-end code, repositories, or prompts.

Mitigation: Keep private keys and KYC materials server-side, avoid sensitive values in examples, and review logging/debug settings before test or production use.

Risk: Merchant and user onboarding share similar field names but have different DTOs, identifiers, status models, and notification behavior.

Mitigation: Use the exact merchant or user reference set for the selected workflow and preserve unresolved protocol or field conflicts as human confirmation items.

Risk: SDK support differs by language and endpoint, especially for image upload and fee-rate workflows.

Mitigation: Use official SDK paths for normal interfaces and follow the documented controlled exception only where the artifact permits it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huifu/skills/huifu-merchant-onboarding)
- [商户进件资料总览](references/shared-overview.md)
- [汇付用户开户与入驻总览](references/user-onboarding-shared-overview.md)
- [商户进件官方来源索引](references/official-service-source-index.md)
- [用户开户官方来源索引](references/user-onboarding-official-service-source-index.md)
- [商户字段合同](references/merchant-onboarding-field-contracts.md)
- [用户字段合同](references/user-onboarding-field-contracts.md)
- [商户外部资源](references/merchant-onboarding-external-resources.md)
- [用户平台合同](references/user-onboarding-platform-contracts.md)
- [签名、验签和凭据边界](references/shared-signing-v2.md)
- [凭据安全边界](references/shared-credential-boundary.md)
- [SDK 能力矩阵](references/shared-server-sdk-matrix.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API request examples, field tables, code snippets, shell commands, and configuration notes when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes answers through task-specific references and marks unresolved protocol or field boundaries for human confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
