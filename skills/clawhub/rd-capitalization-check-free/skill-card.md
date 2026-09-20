## Description:

研发支出明细表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文，并仅执行免费版声明的检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External finance, accounting, and audit-preparation users can use this skill to check R&D expenditure detail tables before monthly close, annual tax settlement, or audit review. It checks arithmetic consistency, totals, duplicate rows, negative values, and blanks, but does not replace professional accounting, audit, or tax judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: R&D accounting tables may contain sensitive business or financial data.

Mitigation: Run the checker only in an approved local environment and provide only the rows needed for review under the organization's data-handling rules.

Risk: The output checks arithmetic and table consistency but is not audit, tax, or professional accounting advice.

Mitigation: Have qualified accounting, audit, or tax reviewers validate capitalization judgments and any downstream decisions.

Risk: The free tier explicitly omits several accounting checks, so relevant issues may remain unreported.

Mitigation: Review the listed checks not run and perform separate review for omitted items before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/rd-capitalization-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or structured JSON with findings, scope, and summary fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Node.js checker; free tier lists checks performed and checks not run.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
