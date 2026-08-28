## Description:

逐行审核中国境内大型线下活动、展会、展台、发布会及临时活动空间的预算或供应商报价，识别重复收费、规格缺失、数量或工期异常、软性成本不透明、地区与场馆口径错误、漏项及潜在增项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tinadu-ai](https://clawhub.ai/user/tinadu-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External commercial, procurement, finance, event operations, and agency teams use this skill to review China event budgets, supplier quotations, BOQs, and settlement sheets line by line. It highlights evidence-backed anomalies, missing support, amount impacts, and suggested handling without assigning a supplier score.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Commercial budgets, supplier quotes, and supporting attachments may contain confidential business information.

Mitigation: Provide only necessary materials, desensitize details before external searches, and avoid giving the skill unnecessary confidential attachments.

Risk: Weak benchmark comparisons can overstate pricing concerns when city, venue, date, specification, quantity, tax, and service scope are not comparable.

Mitigation: Use same-project, same-supplier, same-venue, historical settlement, or same-scope market evidence where available; otherwise mark the issue as pending verification.

Risk: Findings involving fire, structural, electrical, tax, labor, or insurance matters may be mistaken for professional compliance opinions.

Mitigation: Treat those findings as review prompts and require confirmation from qualified professionals or the venue before relying on them.

## Reference(s):

- [Anomaly rules](references/anomaly-rules.md)
- [Regional benchmarking](references/regional-benchmarking.md)
- [Report schema](references/report-schema.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with row-by-row findings and summary sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves original budget row traceability and labels amount impacts as exact, upper-bound, range, pending verification, potential add-on, or refundable deposit/cash occupancy.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
