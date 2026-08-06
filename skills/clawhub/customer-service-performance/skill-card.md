## Description:

客服绩效核算 reads user-provided customer-service workload data and performance rules, calculates per-agent scores with visible intermediate steps, and outputs performance details, team distribution, and manual-review items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zenobiazizi](https://clawhub.ai/user/zenobiazizi)

### License/Terms of Use:

MIT-0

## Use Case:

Customer-service managers and operations teams use this skill to calculate draft agent performance scores from Excel or CSV workload data and configurable scoring rules. The output is intended for review and audit before any payroll, evaluation, or HR decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes employee workload and performance data that may contain sensitive personal or employment information.

Mitigation: Install only when the agent may access the specific workload and rule files needed for the calculation; keep processing local and mask personal identifiers beyond required employee IDs.

Risk: Draft score outputs could be mistaken for final payroll, evaluation, or HR decisions.

Mitigation: Treat all reports as review drafts, retain the required manual-review warning, and independently verify results before using them for compensation or performance decisions.

Risk: Missing data, ambiguous rules, or mismatched columns can produce incomplete or misleading scores.

Mitigation: Flag missing or ambiguous items for manual review, avoid silently scoring missing values as zero, and confirm unclear column mappings or rule definitions before relying on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zenobiazizi/skills/customer-service-performance)
- [Default customer-service performance rules](artifact/references/rules-default.md)
- [Custom rules guide](artifact/references/rules-guide.md)
- [Sample performance report](artifact/examples/sample-report.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Excel workbook when supported; otherwise Markdown tables with a summary, score details, team distribution, and manual-review list.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should show raw values, matched scoring tiers, dimension scores, weights, weighted results, total scores, and review warnings.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
