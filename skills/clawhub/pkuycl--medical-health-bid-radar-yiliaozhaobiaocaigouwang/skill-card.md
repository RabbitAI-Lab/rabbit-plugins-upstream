## Description:

检索医疗健康领域的招采公告，识别医院采购方和中标供应商，并分析医院的主要供应商。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

采购、市场和医疗行业分析人员可检索医疗招标与中标信息，识别医院的主要供应商并跟踪采购项目。该技能还提供企业信息与市场分析查询。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement searches send query details to the external ZLBX service.

Mitigation: Avoid submitting sensitive search terms and share only information appropriate for the service.

Risk: Without a configured API key, account registration can transmit device-derived features and save an API key locally.

Mitigation: Configure your own ZLBX_API_KEY to avoid auto-registration; otherwise obtain consent first and review local key storage.

Risk: Company contacts, business intelligence, and recharge or login links extend beyond medical bid monitoring.

Mitigation: Limit queries to the intended task, handle contact details carefully, and verify links before account or payment actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pkuycl/skills/medical-health-bid-radar-yiliaozhaobiaocaigouwang)
- [Bid search API reference](artifact/references/api-search.md)
- [Company intelligence API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Business registry API reference](artifact/references/api-registry.md)
- [Auto-registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language summaries and structured lists of procurement results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include source links, purchaser and supplier names, and project details.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
