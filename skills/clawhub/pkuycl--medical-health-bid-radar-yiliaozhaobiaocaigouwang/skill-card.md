## Description:

医疗大健康采招雷达-医疗招标采购网，当搜索词包含医院、医疗、卫生、体检时触发，重点提取采购方（医院）和中标方（医药公司/代理商），分析特定医院的Top供应商体系。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Healthcare procurement and market research teams use this skill to find medical tenders and awards, identify hospital purchasers and winning suppliers, and analyze supplier patterns for a particular hospital.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic signup uses device identifiers, and the signup description may not make this sufficiently clear.

Mitigation: Clarify which device features are used and obtain explicit user consent before automatic signup; offer manual setup with the user's own API key.

Risk: Conflicting credential-recovery instructions could lead to an unintended account or credential change.

Mitigation: Reconcile the recovery instructions before installation and require explicit approval before replacing existing credentials.

Risk: Search terms are sent to the service and some successful queries consume account credits.

Mitigation: Send only the user's requested search terms and check query costs and account usage before running broader searches.

Risk: The API key and generated login links could expose account access if mishandled.

Mitigation: Keep the saved API key and generated login links private; avoid including them in shared output.

## Reference(s):

- [ClawHub release](https://clawhub.ai/pkuycl/skills/medical-health-bid-radar-yiliaozhaobiaocaigouwang)
- [Bid search guide](artifact/references/api-search.md)
- [Company analysis guide](artifact/references/api-company.md)
- [Market analysis guide](artifact/references/api-market.md)
- [Account and usage guide](artifact/references/api-account.md)
- [Business registry guide](artifact/references/api-registry.md)
- [Credential setup and recovery guide](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown summaries, tables, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results, procurement and supplier analysis, and account usage summaries; query details and fields depend on the user's request.]

## Skill Version(s):

1.0.11 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
