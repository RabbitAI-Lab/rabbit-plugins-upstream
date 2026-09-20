## Description:

A deterministic checker for land appreciation tax prepayment and settlement worksheets that recomputes deductions, appreciation amount and rate, tax payable, prepayment due, total rows, duplicates, blanks, and line-referenced findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External project accountants and tax review teams use this skill to check land appreciation tax prepayment and settlement worksheet arithmetic before filing or reconciliation. It is intended for worksheet consistency review, not tax advice.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Users may treat arithmetic consistency findings as tax advice.

Mitigation: Use the output as a worksheet check and have qualified tax staff confirm filing positions, local policy, and final treatment.

Risk: The workflow is Chinese-language and expects land appreciation tax worksheet text with specific headers.

Mitigation: Run it only on the intended worksheet type and provide complete table headers and rows; treat insufficient-input responses as no conclusion.

Risk: Security evidence notes inconsistent telemetry and free-tier wording.

Mitigation: Review runtime notices before deployment and run in an environment appropriate for local Node-based checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/land-appreciation-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON report with line-referenced worksheet findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports insufficient input without making a finding; worksheet materials must include recognizable headers.]

## Skill Version(s):

1.0.19 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
