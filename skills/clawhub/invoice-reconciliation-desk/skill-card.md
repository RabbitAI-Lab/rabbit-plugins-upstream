## Description:

Derive match thresholds and build invoice reconciliation summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations users can use this skill to derive an invoice matching threshold from a supplied reconciliation rule and summarize matched invoices from a prepared threshold.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoice matching summaries could be mistaken for an accounting system of record.

Mitigation: Verify thresholds and matched invoice IDs against source records before acting on the summary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/invoice-reconciliation-desk)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Text or structured object fields for match_threshold and reconciliation_summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a numeric match threshold or a reconciliation summary with summary_id, threshold, matched_count, and matched_invoice_ids.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
