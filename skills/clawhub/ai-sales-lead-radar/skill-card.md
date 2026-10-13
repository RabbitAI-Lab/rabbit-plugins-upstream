## Description:

为政企销售和渠道人员检索拟建项目、采购意向及临期续约机会，并按价值和紧急度整理销售线索。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

政企销售、商务拓展与渠道人员根据行业、产品和地区查找潜在客户及尚未发标的机会，生成带优先级和跟进建议的商机清单。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Search queries are sent to the vendor, and trial account registration collects a hashed device identifier.

Mitigation: Share only appropriate query details; use a preconfigured API key to avoid trial registration, or obtain informed consent before registering.

Risk: Stored API credentials and report links with login-bypass parameters may grant access if shared.

Mitigation: Protect local credential and report files; avoid forwarding reports or login-bypass links broadly.

Risk: Lead scanning consumes account credits.

Mitigation: Review estimated credit use before scanning and require approval before exceeding the call budget.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dragonzu/skills/ai-sales-lead-radar)
- [Skill installation documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Sales lead scanning workflow](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Account setup and consent](artifact/references/auto-register.md)
- [Report format](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML report]

**Output Format:** [Ranked Markdown opportunity list and optional shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include source links, priority rationale, follow-up actions and data coverage; a full scan uses account credits.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
