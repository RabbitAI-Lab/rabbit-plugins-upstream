## Description:

A free deterministic checker for construction-in-progress ledgers that recomputes cost pooling, cumulative cost roll-forward, carrying balance, capitalized interest, transfer amounts, duplicate rows, missing fields, and category conformance with source-line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, accounting, and audit users apply this skill to review construction-in-progress ledger text copied from spreadsheets, checking arithmetic consistency, interest capitalization calculations, transfer reconciliation, duplicate entries, missing fields, and allowed cost categories before month-end close or audit review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes optional paid-upgrade installation and payment instructions that extend beyond local free ledger checking.

Mitigation: Use the free checker for local ledger analysis only unless the user deliberately requests the upgrade, verifies package and source details, and personally confirms any wallet or payment step.

Risk: The free checker intentionally omits several accounting judgment checks, including transfer timing, post-transfer cost accumulation, interrupted-period capitalization, contract-rate mismatch, and provisional-transfer adjustments.

Mitigation: Present omitted checks clearly and avoid treating a clean free-check result as accounting or audit assurance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/cip-capitalization-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summary or JSON result with findings, severity levels, source line numbers, missing-input messages, executed checks, and checks not run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard-library code and expects ledger text or JSON input; material shortage returns missing fields rather than conclusions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
