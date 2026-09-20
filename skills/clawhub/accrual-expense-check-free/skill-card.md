## Description:

预提费用台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during monthly close, reconciliation, or inventory checks to review accrual expense ledgers for arithmetic consistency, totals, duplicate projects, and blank or placeholder fields. It reports insufficient input rather than drawing conclusions when required ledger columns or rows are missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free version omits several accrual and invoice write-off checks.

Mitigation: Use the output's disclosed checks-not-run list and verify withheld checks separately before relying on results for financial controls.

Risk: The skill only checks internal ledger consistency and does not judge whether accrual amounts are reasonable.

Mitigation: Review accrual reasonableness against contracts, budgets, accounting policy, and supporting invoice records outside this skill.

Risk: Missing or malformed ledger columns can prevent valid review.

Mitigation: Provide ledger text with project, opening balance, current accrual, current invoice write-off, and closing balance columns; treat insufficient-input output as no conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/accrual-expense-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON findings with source-line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on provided ledger text; free-version output lists checks performed and checks not run.]

## Skill Version(s):

1.0.61 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
