## Description:

A free local checker for platform settlement aging tables that recalculates row arithmetic, total cross-checks, duplicate rows, blanks, placeholders, and negative values, with each finding tied to source rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, treasury, and bookkeeping users run this skill during month-end settlement review to check platform settlement aging tables for arithmetic, totals, duplicate batch rows, blanks, placeholders, and negative values. The free release supports local deterministic checks and reports when input is insufficient instead of inventing a conclusion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release steers users toward external installation and purchase steps for a paid version that are outside the free local checking purpose.

Mitigation: Do not paste the purchase prompt into an AI assistant or run the suggested npx command unless the package, merchant, product, and payment flow have been independently verified and each payment or wallet authorization is approved manually.

Risk: The free checker omits several aging, balance, frozen-ratio, and repeated-settlement checks that users may expect from a complete reconciliation review.

Mitigation: Treat the output as a scoped free check only; review the listed checks_not_run and perform omitted accounting or platform-rule checks separately before relying on the reconciliation.

Risk: The skill checks table arithmetic and internal consistency but does not validate platform rules, fee composition, frozen-fund treatment, source system truth, tax, foreign exchange, bad debt, or cash-flow assumptions.

Mitigation: Confirm platform settlement rules and accounting treatment with authoritative platform exports, contracts, bank records, or accounting reviewers before making financial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/platform-settlement-aging-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON findings with row-level evidence and scope notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided platform settlement aging tables; reports withheld checks and out-of-scope accounting judgments when applicable.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
