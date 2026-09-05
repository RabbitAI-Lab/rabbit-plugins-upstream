## Description:

Use when the user wants a periodic authority and backlink report - referring-domain movement, pillar state, prospect pipeline - as a document, from link exports or TrustGrowth authority data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and SEO operators use this skill to turn link exports or TrustGrowth authority data into a periodic authority and backlink report with source-labeled measurements, movement, verdict, next actions, evidence, and unmeasured gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may contain misleading SEO conclusions if facts are not traceable to validated evidence or if missing values are silently filled.

Mitigation: Use only validated evidence records for conclusions, keep nulls unknown, and label every reported value as Measured, User-provided, or Estimated.

Risk: Authority movement can be misread when counts from different backlink providers are compared directly.

Mitigation: Compare movement only between dated snapshots from the same source and leave cross-provider comparisons uncalculated with a note in the not-measured section.

Risk: Paid or already-configured SEO and analytics connectors may expose sensitive site data or incur provider costs.

Mitigation: Use only user-supplied exports or already-configured connectors, never print keys, and review paid provider batches before approving them.

## Reference(s):

- [Connectors and categories](references/connectors.md)
- [Reporting contract](references/reporting.md)

## Skill Output:

**Output Type(s):** [markdown, guidance]

**Output Format:** [Markdown report with tables, verdict, next actions, evidence, and not-measured sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SHIP, FIX, BLOCK, or UNDECIDED verdicts and labels facts as Measured, User-provided, or Estimated.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
