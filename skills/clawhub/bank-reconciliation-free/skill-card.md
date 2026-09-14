## Description:

把银行流水和企业账面记录逐笔配对，列出未达账项与重复记录，每条结论都带原文日期与金额，不需要付款，也不需要注册。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

Proprietary

## Use Case:

External users, finance staff, cashiers, and accountants use this skill to mechanically reconcile pasted bank statement lines against book entries, find unmatched items on either side, detect single-side duplicate records, and compare counts and totals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The matching logic can incorrectly mark transactions with missing, malformed, or impossible dates as matched.

Mitigation: Verify source dates and amounts manually before using reconciliation results for accounting decisions.

Risk: The skill performs mechanical matching only and does not decide accounting treatment, verify bank-statement authenticity, or connect to banking or finance systems.

Mitigation: Use the output as a reconciliation aid and have qualified finance staff review unmatched items, duplicates, and any required adjustments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bank-reconciliation-free)
- [Free web checker](https://www.tokendidi.cn/check)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON reconciliation findings with evidence-backed dates, amounts, summaries, and execution status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can run locally from sample data or an input JSON/text file; returns insufficient_input instead of a reconciliation conclusion when required materials are missing.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
