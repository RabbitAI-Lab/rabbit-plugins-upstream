## Description:

费用分摊表逐项核对（逐行算术、合计勾稽、重复与空缺检测），每条结论引用原文行号。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, property-management, and operations staff use this skill during monthly closing, reconciliation, and inventory checks to review utility allocation tables. It checks row arithmetic, total-row consistency, duplicate tenants, and blank or placeholder cells, with each finding tied to source line evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional full-version upgrade path asks the agent to run an unpinned remote installer and start a payment-related installation flow.

Mitigation: Verify the SkillPay guide and package publisher before use, avoid blanket pre-authorization, and prefer a pinned reviewed installer version or a sandboxed environment.

Risk: The free checker omits several allocation checks, including allocation-to-area-share agreement, abnormal share values, negative payable totals, and tenant area-share consistency.

Mitigation: Review the listed withheld checks before relying on results, and perform the omitted checks separately when allocation fairness or billing completeness matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/utility-allocation-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON results with findings, summaries, executed checks, withheld checks, and insufficient-input guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source lines; successful runs may report no findings only for executed free-tier checks; insufficient input returns missing information instead of a conclusion.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
