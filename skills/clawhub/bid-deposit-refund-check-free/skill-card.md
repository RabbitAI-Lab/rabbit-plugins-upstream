## Description:

保证金收退台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and bid operations staff use this skill during month-end reconciliation, account checks, or inventory reviews to verify bid-deposit receipt and refund ledgers. It checks row-level arithmetic, totals, duplicate entries, and missing required fields, while citing source rows for each finding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ledger files may contain sensitive bidding or finance data.

Mitigation: Run the checker locally as documented and avoid sharing input or output outside the approved finance workflow.

Risk: The free release omits several checks, including date reversal, overdue refund timing, negative refund amounts, and out-of-range deposit ratios.

Mitigation: Treat a clean result as coverage for the listed free checks only, and use a fuller review path when omitted checks matter.

Risk: The interface and findings are primarily Chinese.

Mitigation: Have a Chinese-reading reviewer confirm findings before using them in formal finance or procurement decisions.

Risk: The checker expects text or JSON ledger input with recognizable headers, not native spreadsheet files.

Mitigation: Export or paste the ledger with table headers before running the skill, and review insufficient-input messages before drawing conclusions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chenqg618/skills/bid-deposit-refund-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON report with cited ledger findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided ledger text; results include executed checks, omitted checks, findings, and summary fields.]

## Skill Version(s):

1.0.55 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
