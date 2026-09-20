## Description:

A free deterministic checker for SaaS subscription usage and overage billing sheets that recomputes overage usage, overage fees, and bill totals, then flags oversized plans, duplicate subscription lines, and missing key fields with source line and subscription references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

Proprietary

## Use Case:

SaaS billing, finance, commercial operations, and customer finance teams use this skill during monthly billing, reconciliation, and renewal discussions to check subscription usage and overage billing tables. It helps review table-level arithmetic, duplicate subscription rows, oversized plans, and missing required fields, but contract terms and source-system usage rules still need separate review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input spreadsheets may contain sensitive customer and financial billing data.

Mitigation: Review and minimize inputs before use, and handle generated findings under the same controls as the source billing material.

Risk: The free release covers only its listed table-level checks, so billing issues outside those checks may remain undetected.

Mitigation: Review the checks not run and verify contract terms, source-system usage rules, invoices, approvals, taxes, and payment status through separate controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/saas-usage-billing-check-free)

## Skill Output:

**Output Type(s):** [text, json, guidance, shell commands]

**Output Format:** [Human-readable CLI output or structured JSON containing execution status, scope, findings, summary, checks run, checks withheld, and guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers and subscription identifiers; insufficient inputs return missing-field guidance instead of a billing conclusion.]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
