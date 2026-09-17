## Description:

电商退货退款与货款结算核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations staff use this skill during monthly ecommerce settlement reconciliation to check refund, commission, payable, net settlement, total-row, duplicate-order, blank-field, and negative-value issues in a provided settlement table.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes paid-upgrade instructions that direct an agent toward an external install and payment workflow.

Mitigation: Use the local free checker only unless a human separately verifies the package, publisher, version, permissions, and purchase terms before any external install or payment step.

Risk: The free edition intentionally omits several settlement checks and may leave issues outside its declared scope undetected.

Mitigation: Review the reported checks_not_run and checks_out_of_scope before relying on results for settlement, accounting, or audit decisions.

Risk: The checker depends on user-supplied table text and does not independently validate platform contracts, tax treatment, bank receipts, or source-system exports.

Mitigation: Provide complete table data with headers and reconcile any findings against platform statements, contracts, accounting policy, and source records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ecommerce-refund-settlement-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Console text or structured JSON findings with source-line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on supplied table text; reports insufficient input instead of making unsupported conclusions.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
