## Description:

物业公共能耗分摊核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文，本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External finance, cashier, and property operations users use this skill during monthly closing or reconciliation to check property public utility apportionment tables for arithmetic, totals, duplicates, blanks, and negative values before follow-up review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker is not a legal or billing-system validator.

Mitigation: Use it as a table arithmetic and reconciliation aid, then review results against contracts, local rules, and the billing system before making billing decisions.

Risk: The free release does not run the withheld paid checks.

Mitigation: Treat the listed free checks as the complete executed scope for this release and use manual review or the complete product for withheld checks.

Risk: Telemetry documentation is inconsistent with the inspected code according to the security evidence.

Mitigation: Review privacy-facing wording before deployment and rely on the security evidence that found no actual network telemetry path in the packaged code.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/property-utility-apportionment-check-free)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON with findings, scope, summary, and missing-input guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input returns missing requirements and no conclusion.]

## Skill Version(s):

1.0.49 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
