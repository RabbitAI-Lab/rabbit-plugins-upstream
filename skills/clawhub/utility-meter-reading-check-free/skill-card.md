## Description:

水电抄表与账单核对（免费版）逐项复算水电抄表与账单核对表，检查逐行算术、合计勾稽、重复行、缺失字段和负数金额，并让每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, property, park, and facility operations staff use this skill during monthly meter reading, closing, and reconciliation to check water and electricity billing tables before downstream settlement. It is intended for arithmetic reconciliation of provided table text, not for verifying local tariff policy, site meter photos, late fees, refunds, or allocation losses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs limited arithmetic reconciliation and should not be treated as a complete billing audit.

Mitigation: Review the reported findings against the original meter readings, utility bills, contracts, and any checks listed as not run before relying on the result.

Risk: The artifact and security guidance indicate a Chinese-language local Node.js utility with locale-specific table expectations.

Mitigation: Run the bundled sample first and confirm that production inputs use compatible headers, units, and tabular structure.

Risk: Security guidance notes stale telemetry wording and recommends clarification, even though the inspected artifacts do not show hidden data sending.

Mitigation: Confirm the publisher's current privacy and usage-statistics behavior before deployment in environments with sensitive billing data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/utility-meter-reading-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Console text or JSON result objects with cited reconciliation findings, missing-input guidance, executed check lists, and withheld check lists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs against user-provided table text or JSON input; sample input is bundled in templates/sample.json.]

## Skill Version(s):

1.0.45 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
