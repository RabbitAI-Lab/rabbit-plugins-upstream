## Description:

Guides Huifu merchant onboarding and user enrollment, including KYC, business activation, API integration, signing, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huifu](https://clawhub.ai/user/huifu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and integration engineers use this skill to plan and implement Huifu merchant onboarding and user enrollment, check request fields and SDK usage, and troubleshoot application status and notifications. Payment transactions and refunds are outside its scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PHP SDK 2.0.31 may not verify TLS certificates correctly while transmitting sensitive merchant identity and banking data.

Mitigation: Do not use this version with production or real KYC and banking data unless certificate-chain and hostname verification are verified or patched; otherwise use a reviewed fixed SDK or security-approved adapter.

Risk: Onboarding examples and debugging can expose signing credentials or sensitive personal and banking information.

Mitigation: Keep credentials in secure configuration and redact identity, banking, phone, and image data from examples, logs, and repositories.

## Reference(s):

- [Huifu merchant onboarding skill release](https://clawhub.ai/huifu/skills/huifu-merchant-onboarding)
- [Huifu enterprise merchant onboarding API](https://paas.huifu.com/partners/api/doc/shgl/shjj/api_shjj_qyshjbxxrz_kyc.md)
- [Huifu API signing and verification guide](https://paas.huifu.com/open/doc/guide/#/api_v2jqyq)
- [Merchant onboarding field contracts](references/merchant-onboarding-field-contracts.md)
- [SDK compatibility matrix](references/shared-server-sdk-matrix.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies unresolved API or SDK details for official confirmation.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill documentation)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
