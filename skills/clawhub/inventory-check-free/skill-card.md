## Description:

库存盘点表逐项核对（逐行算术、合计勾稽、重复与空缺检测），每条结论引用原文行号。本免费版执行引擎声明的免费检查项。触发词包括 库存盘点表核对、库存盘点表对不上。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and warehouse staff use this skill during month-end reconciliation, payroll, account matching, and inventory counts to check copied inventory tables for arithmetic mismatches, totals errors, duplicate item rows, and missing cells. The free release reports line-cited findings and withholds conclusions when required table evidence is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation includes an optional upgrade prompt involving an unpinned remote installer and a purchase flow.

Mitigation: Use the free local checker for inventory reconciliation only unless the SkillPay instructions, package publisher, resolved package version, and payment details have been independently verified in a constrained environment.

Risk: The free release does not perform some inventory checks, including difference-rate threshold alerts, negative-inventory detection, inbound amount reconciliation, and long-inactive item prompts.

Mitigation: Review the listed checks executed and checks withheld before relying on results, and do not treat a clean free-check result as an audit, tax, physical-count, or accounting-policy conclusion.

Risk: Materials without a recognizable inventory table header or sufficient item rows cannot support a conclusion.

Mitigation: Provide copied inventory table text with headers and item rows; when the skill reports insufficient input, collect the missing fields and rerun instead of treating the result as no findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/inventory-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Optional SkillPay shelf mentioned by artifact](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON findings with source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on inventory table text copied from Excel or supplied as JSON; insufficient input returns missing requirements instead of a pass/fail conclusion.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
