## Description:

Provides agent guidance for Huifu merchant and user onboarding integrations, including KYC field contracts, SDK boundaries, signing, credential handling, status queries, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huifu](https://clawhub.ai/user/huifu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and integration engineers use this skill to plan and implement Huifu payment merchant onboarding, KYC, user onboarding, business enablement, status query, image upload, SDK, signing, and troubleshooting workflows. It helps keep merchant and user DTOs, request fields, response handling, callback boundaries, and sensitive credential handling separate and reviewable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts or generated examples may expose real payment credentials, RSA keys, identity documents, bank details, phone numbers, image identifiers, or signatures.

Mitigation: Use placeholders in examples, keep credentials server-side, disable SDK debug logging before requests, and avoid storing sensitive onboarding data in prompts, logs, repositories, or frontend code.

Risk: Merchant onboarding, user onboarding, and payment transaction flows can be confused, leading to incorrect DTOs, wrong status interpretation, or unsafe reuse of IDs.

Mitigation: Confirm whether the target is a payment merchant or settlement user, route to the matching references, keep `/v2/merchant/*` and `/v2/user/*` models separate, and hand payment transactions to the payment integration skill.

Risk: Callback handling, image upload transport, signing, TLS, or SDK-debug behavior may be implemented incorrectly in generated code.

Mitigation: Use official SDK paths where supported, preserve TLS verification, verify signed callbacks before processing, apply the documented image-upload exception only where allowed, and review generated code before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huifu/skills/huifu-merchant-onboarding)
- [Huifu merchant onboarding overview](references/shared-overview.md)
- [Huifu user onboarding overview](references/user-onboarding-shared-overview.md)
- [Merchant onboarding field contracts](references/merchant-onboarding-field-contracts.md)
- [User onboarding field contracts](references/user-onboarding-field-contracts.md)
- [Credential and sensitive data boundary](references/shared-credential-boundary.md)
- [Signing and verification boundary](references/shared-signing-v2.md)
- [Huifu official merchant application status API](https://paas.huifu.com/partners/api/doc/shgl/shjj/api_shjj_sqdztcx.md)
- [Huifu merchant basic data status query endpoint](https://api.huifu.com/v2/merchant/basicdata/status/query)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with field tables, code snippets, command examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; generated implementation guidance should be reviewed before production use.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
