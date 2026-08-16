## Description:

全域电商经营专家团 v1.5.8。当用户需要品牌电商店铺诊断、周报/月报/年报、经营复盘、单平台增长、投流 ROI 与利润优化、内容直播诊断或行动方案时使用。以真实数据为唯一经营事实来源，按主理人、数据、平台、内容、投流、交付六个角色协作输出，严禁编造数据或客户信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gzbarry1980-bot](https://clawhub.ai/user/gzbarry1980-bot)

### License/Terms of Use:

MIT-0

## Use Case:

Brand owners, e-commerce operators, and growth teams use this skill to diagnose storefront performance, produce weekly/monthly/annual operating reports, review campaigns, and create evidence-based action plans across Chinese commerce and content platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect sensitive business performance exports and customer-specific reports provided by the user.

Mitigation: Use a clearly defined client scope, provide only files needed for the current engagement, and avoid unrelated customer files or private historical reports.

Risk: Incomplete or inconsistent commerce data can lead to unsupported profit, budget, or growth conclusions.

Mitigation: Apply the PASS/WARN/BLOCKED data quality gate, disclose limitations on affected conclusions, and withhold profit or budget claims when required inputs are missing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gzbarry1980-bot/skills/omni-ecom-skill)
- [Team Lead Role Reference](references/team-lead.md)
- [Data Analyst Role Reference](references/data-analyst.md)
- [Platform Operations Role Reference](references/platform-ops.md)
- [Content and Live Growth Role Reference](references/content-live-growth.md)
- [Ad Profit Optimizer Role Reference](references/ad-profit-optimizer.md)
- [Data Quality Gate and Evidence Rules](references/data-quality-gate.md)
- [Report Delivery and PDF Rules](references/report-delivery.md)
- [Delivery Review Role Reference](references/delivery-review.md)
- [Privacy, Client Isolation, and Versioning](references/privacy-and-versioning.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown and structured report artifacts when the host supports file generation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce report JSON, editable Markdown, PDF delivery specifications, action tables, evidence summaries, and review receipts depending on host capabilities.]

## Skill Version(s):

1.5.8 (source: manifest.yaml, CHANGELOG.md, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
