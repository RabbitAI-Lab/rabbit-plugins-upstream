## Description:

Helps owner-operators attribute revenue increases or drops to changes in customer count, per-customer volume, pricing, and slow recurring erosion using ledger or order-book data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External business owners use this skill to explain where monthly revenue changes came from before choosing an action. It compares periods, decomposes the movement into customer count, per-customer volume, and price, checks group and multi-month trends, and calls out what data is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Revenue, order, and customer-level business details may be sensitive.

Mitigation: Provide summaries or redact customer names when exact identities are not needed for the attribution task.

Risk: Retained memory can preserve prior corrections and recurring anomaly notes beyond a single session.

Mitigation: Periodically review the configured zmm-revenue memory folder and remove details that should no longer be retained.

## Reference(s):

- [理论底座 · 营收归因](references/理论底座.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-revenue)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown revenue-attribution report with concise prose and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a conclusion, data-confidence note, decomposition table, grouped review, trend check, specific causes, and immediate next actions.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
