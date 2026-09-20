## Description:

Checks Chinese receivables collection and payment tables for row-level arithmetic, total reconciliation, duplicate customer-period rows, blanks, placeholders, and negative amounts, with findings tied to source rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounts receivable staff use this skill during monthly close, reconciliation, or review cycles to check receivables collection plan tables before relying on them for follow-up work. It is intended as a deterministic reconciliation aid, not financial, legal, or credit-risk advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may over-rely on reconciliation output for financial, legal, or credit-risk decisions.

Mitigation: Treat findings as a table-checking aid and verify decisions against company policy, contracts, source accounting records, and qualified professional review.

Risk: The free release does not run several checks that are listed as outside this package's free scope.

Mitigation: Review the reported checks run and checks not run before acting on the result; do not treat a clean result as a complete receivables audit.

Risk: Receivables tables may contain sensitive customer or financial data.

Mitigation: Run the checker only in an approved local environment and provide only the table data needed for reconciliation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/receivable-collection-plan-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON results from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, source line, summary totals, checks run, checks not run, and insufficient-input guidance when required table fields are missing.]

## Skill Version(s):

1.0.43 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
