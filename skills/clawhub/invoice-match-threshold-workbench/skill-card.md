## Description:

Build an invoice reconciliation summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external business users use this skill for routine invoice reconciliation when they need a concise summary based on a supplied invoice match threshold.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may include invoice data that was not intended for the current reconciliation request.

Mitigation: Provide only the invoice information needed for the current request; the skill does not require credentials, private file access, or accounting-system access.

Risk: A generated reconciliation summary may be used without checking whether the selected match threshold is appropriate.

Mitigation: Review the returned threshold, matched count, and matched invoice IDs before using the summary in business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/invoice-match-threshold-workbench)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text]

**Output Format:** [JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a reconciliation_summary object with summary_id, threshold, matched_count, and matched_invoice_ids.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
