## Description:

医疗大健康采招雷达-医疗招标采购网，当搜索词包含医院、医疗、卫生、体检时触发，重点提取采购方（医院）和中标方（医药公司/代理商），分析特定医院的Top供应商体系。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement analysts use this skill to query medical and healthcare bidding/procurement data, identify purchasing hospitals and winning suppliers, analyze supplier networks, and find project opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create an account using device-derived identifiers and persist an API key under ~/.zlbx/config.json.

Mitigation: Prefer setting ZLBX_API_KEY manually; allow auto-registration only after explicit consent and review the stored credential.

Risk: The skill can surface project contact phone numbers and steer users to recharge or related agent links.

Mitigation: Use narrow procurement-specific queries, avoid bulk contact export, and verify account or recharge links before following them.

## Reference(s):

- [Skill listing](https://clawhub.ai/thuanlynham-stack/skills/medical-health-bid-radar-yiliaozhaobiaocaigouwang)
- [Bid Search API Details](references/api-search.md)
- [Company Analysis API Details](references/api-company.md)
- [Market Analysis API Details](references/api-market.md)
- [Account API Details](references/api-account.md)
- [Auto-Registration Flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown responses with tables, links, concise analysis, and JSON request examples when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a consent-gated auto-registration flow; account status may affect contact visibility and quota behavior.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
