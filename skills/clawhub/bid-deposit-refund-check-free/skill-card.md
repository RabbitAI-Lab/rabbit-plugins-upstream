## Description:

This skill locally checks bid-deposit refund ledgers for row-level arithmetic, totals reconciliation, duplicate entries, blanks, and source-cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and procurement operations staff use this skill during month-end reconciliation, account checking, or inventory reviews to verify bid-deposit refund ledgers before downstream accounting work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review flags an unpinned remote payment and install workflow for the paid version.

Mitigation: Do not let an agent run the paid-version install or payment command until the package version, source, permissions, and payment flow have been separately reviewed.

Risk: The free checker intentionally omits several controls, including date-order, overdue-refund, negative-refund, and rate-range checks.

Mitigation: Treat the output as a free-scope ledger consistency check and review the reported checks_not_run before relying on the result.

Risk: Insufficient or unrecognized ledger input produces no conclusion rather than a clean result.

Mitigation: Provide ledger text or JSON with the required headers and review any missing-input messages before taking action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bid-deposit-refund-check-free)
- [Paid version purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console text or JSON result object with cited ledger findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with ledger text or JSON input; the free version reports checks not run and does not make findings when input is insufficient.]

## Skill Version(s):

1.0.7 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
