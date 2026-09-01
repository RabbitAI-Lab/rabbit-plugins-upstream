## Description:

逐行审核并谈判中国境内大型线下活动、展会、展台、发布会及临时活动空间的预算或供应商报价，识别异常后给出可执行的第一口、成交红线、补件和谈判话术。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tinadu-ai](https://clawhub.ai/user/tinadu-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External and employee event procurement, marketing operations, and finance reviewers use this skill to audit China on-site event budgets, supplier quotes, BOQs, and settlement sheets line by line. It identifies evidence-backed anomalies, missing materials, amount impacts, recommended handling, and negotiation positions without assigning an overall supplier score.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Users may provide confidential client, supplier, pricing, project, or personal data in budgets and attachments.

Mitigation: Limit shared materials to what is needed for the review and desensitize any files or outputs before external reuse.

Risk: Missing attachments or incomplete quote details can make price, scope, or responsibility findings uncertain.

Mitigation: Keep conclusions evidence-labeled, record row-specific material gaps, and avoid treating missing information as confirmed overpricing.

Risk: Findings may touch fire safety, structural, electrical, tax, labor, insurance, or venue compliance issues.

Mitigation: Require confirmation from qualified professionals, the venue, or appropriate advisors before relying on those conclusions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/tinadu-ai/skills/china-event-budget-dd-clawhub-v110)
- [Publisher profile](https://clawhub.ai/user/tinadu-ai)
- [逐项异常规则](references/anomaly-rules.md)
- [地区、场馆与价格基准](references/regional-benchmarking.md)
- [报告字段与呈现规则](references/report-schema.md)
- [一线砍价方法](references/negotiation-playbook.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown tables and concise explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces traceable line-level findings, amount-impact labels, row-specific evidence requests, summaries, and optional negotiation tables.]

## Skill Version(s):

1.0.0 (source: server release metadata; source skill metadata reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
