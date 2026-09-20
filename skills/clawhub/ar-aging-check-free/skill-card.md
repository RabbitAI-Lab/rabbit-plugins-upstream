## Description:

应收对账表逐项核对（逐行算术、合计勾稽、重复与空缺检测），每条结论引用原文行号。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, warehouse, and operations staff use this skill during month-end close, payroll, reconciliation, or inventory workflows to check AR aging tables for arithmetic mismatches, total-row errors, duplicate customers, and blank or placeholder values. The skill reports line-cited findings and withholds conclusions when the supplied table is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the free subset as a complete AR review even though the skill explicitly omits credit-balance prompts, over-collection checks, long-aged exposure ratio checks, and sign-consistency checks.

Mitigation: Review the listed withheld checks before relying on the result, and use a broader accounting review for decisions involving collections, provisions, or unusual balances.

Risk: Incomplete or malformed table input can prevent the skill from checking the AR aging data or can leave accounting issues outside the executed checks.

Mitigation: Provide the full table with recognizable headers and review the line-cited evidence, missing-input messages, and executed-check list before using the findings.

Risk: The output is an arithmetic and table-consistency check, not audit, tax, legal, credit, or accounting-policy advice.

Mitigation: Have qualified finance or accounting reviewers evaluate policy judgments and downstream business decisions separately from this skill's findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ar-aging-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Console text or JSON with line-cited findings, summaries, executed checks, and withheld checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node standard library; accepts an AR aging table as JSON text or pasted table text; returns insufficient-input status instead of conclusions when required table structure is missing]

## Skill Version(s):

1.0.57 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
