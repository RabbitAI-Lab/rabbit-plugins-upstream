## Description:

Checks monthly manufacturing accounting materials for production input/output and scrap rate, material usage and standard loss, and inventory movements with weighted-average cost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Manufacturing finance, cashier, and operations staff use this skill during monthly close, reconciliation, or inventory count workflows to check tabular manufacturing records for arithmetic, totals, missing values, duplicates, and weighted-average cost consistency. It supports review and reconciliation but does not replace accounting, audit, or attestation decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incomplete review can appear complete if the user only reads the human summary.

Mitigation: Run with --json and verify result.per_check statuses, result.scope.sections_done, and the checks_not_run list before relying on the result.

Risk: A NO_ISSUE_FOUND summary can be mistaken for proof that every promised check ran.

Mitigation: Treat NO_ISSUE_FOUND as valid only after confirming every expected section is present and marked ok.

Risk: Month-end accounting decisions may rely on this tool beyond its stated arithmetic and reconciliation scope.

Mitigation: Use the output as review support and keep accounting, audit, attestation, and filing decisions under qualified human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/manufacturing-monthly-selfcheck-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text summary or structured JSON report when run with --json]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed checks, findings, missing-input status, withheld checks, local execution, and network-use flags.]

## Skill Version(s):

1.0.46 (source: server release metadata; artifact frontmatter lists 1.0.45)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
