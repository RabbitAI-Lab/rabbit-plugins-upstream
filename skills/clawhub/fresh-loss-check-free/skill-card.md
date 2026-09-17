## Description:

面向财务、出纳和门店盘点人员的本地核对技能，用于对生鲜损耗与盘点表执行逐行复算、合计勾稽、重复行、空白占位符和负数量检查，并为结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External business users such as finance staff, cashiers, store managers, and fresh produce operators use this skill during month-end closing, reconciliation, and inventory checks to verify arithmetic consistency in fresh produce loss and stocktake tables. It reports missing input instead of drawing a conclusion when the provided table lacks required fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill text includes a paid-upgrade flow that asks an agent to install an unpinned external payment/onboarding package and initiate a purchase.

Mitigation: Use only the bundled free local checker unless a human has separately reviewed the payment instructions and explicitly confirms any install or payment step.

Risk: The free checker intentionally omits several checks that are reserved for the paid edition, so users may mistake a limited result for complete coverage.

Mitigation: Treat results as limited to the listed free checks and review the withheld and out-of-scope checks before relying on the output for business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/fresh-loss-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands, plus local checker output as human-readable text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; findings cite source rows; insufficient input returns missing fields instead of a conclusion.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
