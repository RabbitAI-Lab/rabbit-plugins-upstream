## Description:

Checks safety production fee extraction and use tables by recomputing row amounts, rolling balances, totals, duplicates, blanks, placeholders, and negative values, with source-line evidence for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and safety management teams use this skill during monthly close, safety fee accrual, and dedicated-account reimbursement review to check arithmetic and table consistency before further review. It is focused on table checks and does not provide legal, accounting, or regulatory compliance advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is focused on Chinese-domain safety production fee tables and does not provide legal or accounting compliance advice.

Mitigation: Use the output as arithmetic and consistency support, then confirm regulatory treatment with current rules and qualified finance, safety, or legal reviewers.

Risk: The free release omits several checks such as lower-bound extraction-rate checks, overuse of available balance, negative ending balance, zero current-period extraction, and cumulative usage-ratio checks.

Mitigation: Review the listed checks that were not run and do not treat a clean free-tier result as a complete compliance assessment.

Risk: Telemetry wording is inconsistent with the inspected code according to the authoritative security guidance.

Mitigation: Validate runtime behavior in the target environment before processing sensitive material and keep confidential source tables under local data-handling controls.

Risk: Incomplete or unrecognized table headers cause the skill to withhold conclusions rather than infer missing values.

Mitigation: Provide a complete table with the expected period, subject, rate, extraction, use, and balance fields, and review any insufficient-input report before relying on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/safety-production-fee-check-free)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable console output or JSON findings from a local Node.js checker.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source lines when checks execute; insufficient input reports missing requirements instead of a conclusion.]

## Skill Version(s):

1.0.49 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
