## Description:

詹明明·这个月钱去哪了 helps owner-operators attribute revenue changes by separating customer count, per-customer volume, and price effects from ledger or order-book data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External owner-operators use this skill to understand why revenue rose or fell, separate customer-count, purchase-volume, and price effects, and identify concrete next actions from available ledger or order-book data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process ledger, order, customer-level revenue, and other sensitive business data.

Mitigation: Limit memory reads to the skill namespace where possible, redact customer names and exact values when feasible, and review outputs before sharing them.

Risk: The skill reads shared general memory and may save business conclusions for later use.

Mitigation: Ask before saving sensitive details and provide a way to inspect and delete stored records.

Risk: Incomplete or mismatched revenue data can produce misleading attribution conclusions.

Mitigation: State the accounting basis, data coverage, and missing fields before relying on the attribution.

## Reference(s):

- [理论底座 · 营收归因](references/理论底座.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-revenue)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with tables and action bullets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes attribution confidence, data limitations, trend checks, and concrete next actions.]

## Skill Version(s):

0.2.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
