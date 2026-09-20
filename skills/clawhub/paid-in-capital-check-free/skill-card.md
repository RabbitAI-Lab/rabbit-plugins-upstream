## Description:

Checks Chinese shareholder contribution tables by recalculating rows, totals, unpaid amounts, paid-in capital, capital reserves, duplicate shareholders, blanks, and ratio consistency, citing source evidence for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

Proprietary

## Use Case:

Company finance, corporate secretary, audit, and securities affairs teams use this skill before annual audits, filings, capital increases, restructuring, or equity transfers to check whether shareholder contribution tables reconcile. It surfaces formula, total, duplicate-row, blank-field, and ratio issues without replacing legal, audit, tax, or authenticity review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The help text mentions anonymous usage statistics and a --no-stats option, while security evidence says no telemetry code or --no-stats parser was found in this artifact.

Mitigation: Review the installed artifact behavior and clean up or verify the telemetry wording before deployment.

Risk: The checker does not provide legal, audit, tax, valuation, bank-record authenticity, or corporate-registry judgments.

Mitigation: Use results as table reconciliation support and keep legal, audit, tax, and authenticity determinations with qualified reviewers and source documents.

Risk: The free release intentionally omits several checks that are listed as not run.

Mitigation: Review the checks not run in the output and decide whether the omitted checks are needed before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/paid-in-capital-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable CLI text or structured JSON findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [JSON output includes findings, severity, category, message, evidence, summary, executed checks, and checks not run.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
