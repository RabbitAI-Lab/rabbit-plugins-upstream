## Description:

Helps owner-operators attribute revenue changes by separating customer count, purchase volume per customer, and price effects, then checking grouped and multi-month patterns before recommending next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External owner-operators use this skill to understand why revenue rose or fell from ledgers, order books, or platform exports before deciding whether to retain customers, ask customers, adjust pricing, or avoid reactive fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may store sensitive revenue, order, pricing, and customer-level business context in memory without clear user notice or controls.

Mitigation: Set clear boundaries on what may be stored in memory before use, and periodically review or delete the zmm-revenue memory when it contains sensitive commercial information.

## Reference(s):

- [理论底座 · 营收归因](references/理论底座.md)
- [ClawHub Skill Page](https://clawhub.ai/iamzifei/skills/zmm-revenue)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown revenue attribution report with tables and action guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use local memory to retain corrected revenue-analysis assumptions and prior attribution outcomes.]

## Skill Version(s):

0.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
