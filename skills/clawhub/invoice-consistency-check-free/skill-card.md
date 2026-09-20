## Description:

A free local invoice and expense-claim consistency checker that reports recomputable arithmetic, amount, date, duplicate-invoice, placeholder, and entity-name findings with original-text evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, operations, and reimbursement reviewers use this skill to check invoice or expense text before submission or review. It helps identify mechanical inconsistencies such as mismatched totals, tax arithmetic errors, date conflicts, duplicate invoice signals, placeholder residue, and entity-name mismatches without making tax, audit, or authenticity determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake a clean consistency result for tax validation, invoice authenticity verification, or audit approval.

Mitigation: Treat results as mechanical consistency findings only and keep human finance, tax, or audit review for authenticity, compliance, and business-judgment decisions.

Risk: The checker relies on text with recognizable labels or table structure and does not process images or PDFs directly.

Mitigation: Convert invoices to text first and review insufficient-input responses; do not treat missing or unrecognized fields as proof that no issue exists.

Risk: Entity-name normalization is intentionally narrow and may flag abbreviations, aliases, or legal-name variants for human review.

Mitigation: Review the cited source lines and confirm whether names refer to the same legal entity before changing or rejecting a claim.

Risk: Security evidence says this version appears local-only, but documentation mentions anonymous usage statistics that were not implemented in inspected files.

Mitigation: Re-check security evidence and runtime behavior before relying on future versions for network-free handling of sensitive invoice text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/invoice-consistency-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable console text or structured JSON containing findings, evidence, summaries, and withheld checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, line number, advice, and recomputable evidence; insufficient input returns no conclusion rather than a clean verdict.]

## Skill Version(s):

1.0.46 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
