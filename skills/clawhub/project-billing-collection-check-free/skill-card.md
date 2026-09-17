## Description:

Checks project billing and collection ledgers for row-level arithmetic, totals consistency, duplicate rows, blanks, placeholders, and negative amounts, with source-cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, treasury, and project operations teams use this skill during monthly closing, reconciliation, or inventory checks to validate a project billing and collection ledger. It helps identify arithmetic mismatches, total-line issues, duplicate project-period rows, missing values, placeholders, and negative amounts without making conclusions when required ledger material is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is flagged suspicious because the free checker also directs users toward payment tooling and purchase of a separate paid skill.

Mitigation: Use the free checker only when the user is comfortable ignoring upgrade or purchase instructions; do not run payment-tooling commands or authorize purchases without separately verifying the package, merchant, version, and paid skill.

Risk: The free checker intentionally omits several billing and collection checks that are described as available only in the paid version.

Mitigation: Treat the output as limited to the executed free checks and review the listed checks_not_run before relying on the result for operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/project-billing-collection-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance and local checker output, with optional JSON results from the bundled Node.js runner.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows and scopes; insufficient input produces missing-material guidance instead of a no-issue conclusion.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
