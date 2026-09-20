## Description:

This skill checks teaching-hour consumption and teacher hourly-pay sheets by recomputing pay, validating lesson-type accounting rules, reconciling student and system hour consumption, checking totals, and flagging below-floor rates, duplicate records, and missing key fields with source-line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Academic affairs, finance, and campus managers at training organizations use this skill during monthly teacher-pay reconciliation to compare exported student hour consumption with teacher hourly-pay rows. It helps identify arithmetic mismatches, lesson-type accounting issues, total-row errors, below-floor hourly rates, duplicate rows, and missing required fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation claims local operation, while runner text mentions anonymous usage statistics and security evidence notes this mismatch.

Mitigation: Review the release documentation before installation and, where available, disable statistics collection or run in an offline environment when handling sensitive payroll material.

Risk: The skill checks arithmetic and stated table consistency but does not validate legal, contractual, attendance, tax, or payroll-policy correctness.

Mitigation: Use findings as reconciliation support only and route pay, contract, attendance, and compliance decisions through the organization's approved payroll and legal review process.

Risk: The free version explicitly withholds cross-teacher or cross-campus rollups, ranked handling lists, pay-difference attribution, rate-consistency checks, and daily-hour cap checks.

Mitigation: Confirm that the free check scope is sufficient before relying on the result, and perform separate review for withheld checks when those controls are required.

Risk: Missing or unrecognized required columns cause insufficient_input output, so incomplete tables do not receive a positive or negative reconciliation result.

Mitigation: Provide copied or exported table text with the required headers and treat insufficient_input as no conclusion rather than as a clean result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/teacher-hour-pay-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console text or structured JSON findings with source-line evidence and remediation advice]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns success or insufficient_input status; findings include severity, category, line, amount, message, evidence, and advice.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
