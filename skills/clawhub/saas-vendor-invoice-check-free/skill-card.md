## Description:

A deterministic local checker for SaaS vendor invoices and usage-detail tables that recomputes billed amounts, compares billed quantity with usage or seats, checks totals, duplicate charges, contract-price overruns, and missing fields, with source line references for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, finance, and IT asset teams use this skill during monthly vendor billing, quarterly usage reviews, and renewal negotiations to check whether a SaaS invoice matches the supplied usage or seat table. It returns line-referenced findings and withholds conclusions when required input columns are missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package text inconsistently mentions anonymous usage statistics and a --no-stats option that is not implemented.

Mitigation: Users with strict no-network requirements should review the runner before installation and execution.

Risk: The checker only verifies table-internal arithmetic and selected column comparisons, so a clean result does not prove the contract terms, usage source, seat ledger, tax treatment, invoice status, or payment status are correct.

Mitigation: Review findings against the contract, vendor billing system, internal usage reports, seat ledger, invoices, and payment records before making payment or renewal decisions.

Risk: Missing or placeholder input fields prevent reliable conclusions.

Mitigation: Provide a table with the required headers and use 0 only when the value is known to be zero; otherwise treat blanks as unknown and rerun after filling the missing data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/saas-vendor-invoice-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Command-line text or JSON containing scope, findings, summary, executed checks, withheld checks, and out-of-scope checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity level, category, source line, affected amount, message, and advice; insufficient input returns missing fields and does not produce a positive or negative conclusion.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
