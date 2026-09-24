## Description:

帮助开发者集成汇付支付/斗拱支付商户进件、用户开户、KYC、业务开通、字段合同、SDK 调用、签名验签和通知排障。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huifu](https://clawhub.ai/user/huifu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and integration engineers use this skill to implement and troubleshoot Huifu merchant onboarding, user onboarding, KYC, business-opening, electronic-contract, and SDK integration workflows while keeping request, response, notification, signing, and credential boundaries explicit.

### Deployment Geography for Use:

Global; production use remains subject to Huifu account, regional, and regulatory eligibility.

## Known Risks and Mitigations:

Risk: PHP live integrations may send sensitive KYC, bank, identity, credential, or merchant-management data through an SDK transport path with disabled TLS peer verification.

Mitigation: Review before use; do not send real sensitive data through the PHP path until a corrected transport with certificate and hostname validation is verified.

Risk: Generated onboarding or merchant-management requests can affect live accounts when real credentials, identifiers, materials, or operator authority are used.

Mitigation: Require explicit operator confirmation for live account changes, keep examples masked, preserve signing and verification boundaries, and isolate unknown protocol details as TODOs or configuration.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huifu/skills/huifu-merchant-onboarding)
- [Merchant Onboarding Overview](artifact/references/shared-overview.md)
- [User Onboarding Overview](artifact/references/user-onboarding-shared-overview.md)
- [Onboarding Extension Overview](artifact/references/onboarding-extension-shared-overview.md)
- [Server SDK Matrix](artifact/references/shared-server-sdk-matrix.md)
- [Skill Version Policy](artifact/references/skill-version-policy.md)
- [Official Service Source Index](artifact/references/official-service-source-index.md)
- [Huifu Open Platform](https://paas.huifu.com/open/home/index.html)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, configuration, shell commands]

**Output Format:** [Markdown with optional code snippets, request/response structures, SDK guidance, TODO markers, and human-confirmation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include interface-specific references, field paths, signing and credential boundaries, and masked placeholders for sensitive values.]

## Skill Version(s):

1.0.3 (source: server release evidence and artifact version policy)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
