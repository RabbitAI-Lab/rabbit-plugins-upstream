## Description:

This skill locally checks advertising agency rebate reconciliation tables for row arithmetic, totals, duplicate rows, blanks, and negative amounts, citing source rows for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations teams use this skill during monthly or quarterly reconciliation to check Chinese advertising agency rebate tables before settlement. It helps recompute rebate and net payable values, compare totals, and flag duplicate, blank, or negative entries; it is not a contract, tax, or full financial audit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the output as a complete contract, tax, or financial audit.

Mitigation: Use the results as arithmetic and table-consistency checks only, and review the checks not run before relying on the free version.

Risk: Insufficient or malformed table input can lead to missing checks.

Mitigation: Provide the required advertising rebate reconciliation table format with headers; the skill reports missing material instead of issuing a conclusion when input is insufficient.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/chenqg618/skills/ad-agency-rebate-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console text or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input produces missing-material guidance instead of a pass/fail conclusion.]

## Skill Version(s):

1.0.44 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
