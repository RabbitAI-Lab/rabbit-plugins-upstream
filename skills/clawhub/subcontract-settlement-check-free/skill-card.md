## Description:

A local Node.js skill that checks subcontract settlement and production-value tables by recalculating payable amounts and totals, detecting duplicate or incomplete rows, and citing source rows for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and construction operations users run this skill during monthly settlement, reconciliation, or inventory close to check subcontract settlement tables for arithmetic mismatches, total-row issues, duplicate rows, blanks, and negative amounts. It reports when source material is insufficient instead of producing unsupported conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes settlement table data locally, so users may run it on commercially sensitive finance or subcontractor records.

Mitigation: Install and run it only in an environment approved for those records; the security evidence reports no data exfiltration, hidden persistence, credential access, or destructive behavior.

Risk: The help text contains stale wording about anonymous usage statistics that the security evidence says are not actually implemented.

Mitigation: Treat network-use claims as a review point during release validation and rely on the security evidence when assessing current risk.

Risk: The checker covers only the free-tier checks and does not decide contractual measurement, warranty, tax, ERP import, or other out-of-scope questions.

Mitigation: Use findings as row-cited reconciliation support and verify business conclusions against the underlying contract, table source, and any required accounting review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/subcontract-settlement-check-free)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable terminal text or JSON containing executed checks, withheld checks, status, and row-cited findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally over user-provided subcontract settlement table text or JSON; exits with distinct status codes for missing input, insufficient material, parse failures, and unexpected errors.]

## Skill Version(s):

1.0.52 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
