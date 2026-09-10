## Description:

医疗大健康采招雷达-医疗招标采购网，当搜索词包含医院、医疗、卫生、体检时触发，重点提取采购方（医院）和中标方（医药公司/代理商），分析特定医院的Top供应商体系。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement analysts use this skill to query Chinese medical and healthcare bidding data, inspect buyer and supplier relationships, and generate market or account-status guidance from the ZhiLiao BiaoXun APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends procurement queries, company or contact lookups, and account usage requests to a third-party procurement data service.

Mitigation: Use it only for data the user is authorized to process, and configure a user-controlled ZLBX_API_KEY where possible.

Risk: The evidence reports account onboarding, device fingerprinting, local credential persistence, and tracked referral behavior.

Mitigation: Review or avoid the auto-registration and auto-login flows when device tracking or plaintext local API-key storage is unacceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/medical-health-bid-radar-yiliaozhaobiaocaigouwang)
- [Publisher profile](https://clawhub.ai/user/pkuycl)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown with API request examples, tabular summaries, and concise analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY or a consented account registration flow before paid data calls.]

## Skill Version(s):

1.0.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
