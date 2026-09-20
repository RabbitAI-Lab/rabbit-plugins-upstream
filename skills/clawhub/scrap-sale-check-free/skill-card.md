## Description:

A free deterministic checker for scrap and offcut sale settlement ledgers that recalculates quantities, amounts, ledger income, balances, totals, duplicate weighbridge tickets, blanks, and negative values with source-line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cost accounting, general ledger, audit, and internal-control users can use this skill to check copied scrap-sale settlement ledgers against basic arithmetic and reconciliation rules. It is intended for local review of provided ledger text, and it reports missing material instead of drawing conclusions when inputs are insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copied scrap-sale ledgers can contain sensitive financial or operational data.

Mitigation: Run the checker locally and avoid sharing ledger inputs outside the review environment.

Risk: The current help text mentions anonymous statistics and a --no-stats flag that are not implemented, which can confuse privacy expectations.

Mitigation: Clean up the CLI help text before publication and document the actual scanner-confirmed network behavior.

Risk: The checker depends on complete table text with recognizable headers and will not produce a conclusion when required material is missing.

Mitigation: Provide the required ledger headers and review the missing-material output before relying on any finding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/scrap-sale-check-free)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Human-readable text or JSON CLI output with source-line citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs deterministic local ledger checks; requires copied table text with recognizable headers and returns no conclusion when required material is missing.]

## Skill Version(s):

1.0.40 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
