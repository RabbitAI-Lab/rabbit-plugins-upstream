## Description:

餐饮菜品成本与出品率核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Restaurant finance, cashier, and operations staff use this skill during monthly closing, reconciliation, or inventory review to check dish cost and yield tables for arithmetic mismatches, missing fields, duplicate rows, and negative values. It runs a free local checker and reports findings with source row references when the supplied table is sufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes paid-upgrade instructions that ask an AI assistant to install payment tooling and begin a purchase flow.

Mitigation: Use the free local checker only unless the package, merchant, product, and payment flow have been independently verified; require the human user to confirm any wallet authorization or payment.

Risk: The checker validates table arithmetic and completeness but does not verify source documents, recipe correctness, tax treatment, inventory valuation, or operational records.

Mitigation: Treat findings as reconciliation support and review the underlying cost cards, receiving records, POS exports, inventory records, and finance policy before acting on the result.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/restaurant-food-cost-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON checker output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Checker results identify executed checks, omitted paid-tier checks, row-level findings, summary counts, and insufficient-input messages.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
