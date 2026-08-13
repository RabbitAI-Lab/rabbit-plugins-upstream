## Description:

Voc Conversation analyzes batches of customer service conversations and produces a decision-oriented VOC report with topic distribution, sentiment, high-frequency issues, redacted customer quotes, risk signals, and improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zenobiazizi](https://clawhub.ai/user/zenobiazizi)

### License/Terms of Use:

MIT-0

## Use Case:

Operations, product, and customer service teams use this skill to summarize Chinese customer service conversation exports into a single VOC insight report for customer feedback analysis, complaint attribution, and product or service improvement planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customer conversation exports may contain personal, order, address, or other sensitive information.

Mitigation: Use the skill only when authorized to process the data, minimize or redact sensitive fields before analysis, and verify that report quotes are de-identified before sharing.

Risk: A single-batch VOC report may overstate patterns or support decisions beyond the supplied conversation sample.

Mitigation: Treat the output as decision support, retain the report disclaimer, and validate important decisions with additional data.

Risk: Very large or malformed exports can lead to incomplete or biased analysis if processed without review.

Mitigation: Follow the skill workflow by identifying unparsed files, preserving count totals, and asking the user to confirm full-analysis, sampling, or batching choices for large datasets.

## Reference(s):

- [通用问题标签树 v1.0](references/topics-default.md)
- [VOC 会话分析报告示例](examples/sample-report.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown report or Excel workbook]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a one-page conclusion, topic distribution, sentiment distribution, high-frequency issue table, redacted representative quotes, risk signals, prioritized recommendations, and a decision-reference disclaimer.]

## Skill Version(s):

1.0.0 (source: server release metadata and README version section)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
