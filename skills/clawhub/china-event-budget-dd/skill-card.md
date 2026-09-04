## Description:

逐行审核并谈判中国境内大型线下活动、展会、展台、发布会及临时活动空间的预算或供应商报价，识别异常后给出可执行的第一口、成交红线、补件和谈判话术。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tinadu-ai](https://clawhub.ai/user/tinadu-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External event, procurement, finance, and operations teams use this skill to review China-based offline event budgets, vendor quotes, BOQs, and settlement sheets. It identifies line-level anomalies, missing evidence, potential add-ons, and negotiation positions while preserving row-level traceability.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: User budgets, vendor quotes, and supporting event files can contain confidential business terms or personal data.

Mitigation: Use only documents intended for review, remove sensitive identifiers before public benchmarking, and keep red lines or internal budgets out of supplier-facing outputs.

Risk: Public or non-comparable market prices can lead to misleading claims about whether a line item is overpriced.

Mitigation: Require comparable city, venue, date, specification, quantity, service scope, tax status, and procurement conditions before treating benchmarks as evidence.

Risk: Negotiation guidance could be misused to cut safety, compliance, or objectively necessary on-site work.

Mitigation: Preserve evidence-based anomaly statuses and require qualified confirmation for fire, structural, electrical, tax, labor, insurance, and venue compliance issues.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tinadu-ai/skills/china-event-budget-dd)
- [逐项异常规则](references/anomaly-rules.md)
- [地区、场馆与价格基准](references/regional-benchmarking.md)
- [报告字段与呈现规则](references/report-schema.md)
- [一线砍价方法](references/negotiation-playbook.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown tables and summaries in Chinese]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Line-level findings preserve source row references; negotiation mode adds first offer, internal red line, evidence requests, and supplier-facing wording.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
