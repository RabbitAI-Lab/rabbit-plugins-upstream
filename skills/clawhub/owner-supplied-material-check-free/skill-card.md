## Description:

This Chinese-language skill checks owner-supplied material ledgers by recalculating issued quantity, issued amount, settlement deductions, totals, duplicate material rows, blanks, and negative values, with findings tied to source ledger line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External construction project cost staff and subcontract settlement staff use this skill during monthly measurement reporting and final settlement to check owner-supplied material ledgers and identify arithmetic, total, duplicate-row, missing-field, and negative-value issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the free checker as covering withheld checks such as over-issuance judgment, return-offset detection, contract-price comparison, or missed deduction detection.

Mitigation: Use it only for the seven listed ledger checks and route withheld checks to a separate review or tool.

Risk: Insufficient or unrecognized ledger input can produce a missing-input response rather than a substantive finding.

Mitigation: Provide ledger text with the required headers and review missing-field guidance before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/owner-supplied-material-check-free)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON checker output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source ledger line numbers; insufficient input returns missing-field guidance instead of a conclusion.]

## Skill Version(s):

1.0.47 (source: server evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
