## Description:

Checks Chinese advance-receipt and revenue-recognition ledgers for row arithmetic, total tie-outs, duplicates, blanks, and placeholder values, with each finding tied to the source line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, bookkeeping, and operations users run this skill before monthly close or reconciliation to check an advance-receipt ledger against expected balances and totals. It helps identify deterministic table issues while leaving accounting judgment and omitted free-tier checks for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker does not replace accounting judgment and does not determine revenue-recognition timing or performance progress.

Mitigation: Have a qualified finance or accounting reviewer assess the ledger, contracts, tax treatment, and recognition timing before relying on results.

Risk: The free version explicitly omits several checks, including available-prepayment, contract-total, and zero-prepayment revenue checks.

Mitigation: Review the listed checks not run and perform those omitted checks separately when they matter to the close or audit workflow.

Risk: Results depend on user-provided Chinese ledger text being complete and parseable.

Mitigation: Provide the table with required headers and source rows, and treat insufficient-input responses as no conclusion rather than a clean result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/advance-receipt-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable console text or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes executed checks, checks not run, line-cited findings, summary counts, and insufficient-input guidance.]

## Skill Version(s):

1.0.61 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
