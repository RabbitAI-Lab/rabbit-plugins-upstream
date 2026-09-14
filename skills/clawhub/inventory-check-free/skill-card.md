## Description:

库存盘点表逐项核对（逐行算术、合计勾稽、重复与空缺检测），每条结论引用原文行号。本免费版执行引擎声明的免费检查项。触发词包括 库存盘点表核对、库存盘点表对不上。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Warehouse, finance, and operations teams use this skill after monthly or quarterly inventory counts to check arithmetic consistency in copied inventory tables. It helps identify line-level reconciliation errors, total-row mismatches, duplicate item rows, blanks, and unparseable numeric fields while preserving source line references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat arithmetic findings as accounting, audit, tax, or physical-stock verification.

Mitigation: Present results as arithmetic assistance only and require qualified review before using findings for financial, audit, tax, or inventory-control decisions.

Risk: Unrelated sensitive material could be pasted because some help text examples refer to non-inventory documents.

Mitigation: Use only inventory count tables needed for reconciliation and remove unrelated payroll, contract, or other sensitive content before running the skill.

Risk: The free version omits some checks, including difference-rate thresholds, negative inventory detection, inbound amount reconciliation, and stagnant inventory prompts.

Mitigation: Review the reported checks not run and apply separate controls when those checks are required.

Risk: The tool does not read .xlsx files directly and may return insufficient input when headers or table structure are missing.

Mitigation: Copy the inventory table from Excel as text with headers, preferably tab-separated, and treat insufficient-input responses as no conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/inventory-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or structured JSON findings with source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; accepts JSON or copied plain-text inventory tables with headers.]

## Skill Version(s):

1.0.0 (source: evidence.json release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
