## Description:

AI KEY·这个月钱去哪了 helps owner-operators attribute revenue changes to customer count, per-customer volume, and price, while checking for slow erosion hidden in monthly noise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External owner-operators use this skill to diagnose why revenue changed across a period using ledgers, order books, or platform exports. It separates customer count, per-customer volume, and price effects before proposing immediate next steps and actions to avoid.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask for sensitive revenue, order, customer, and pricing details.

Mitigation: Use it only where sharing that business context with the agent and any configured memory is acceptable; omit or redact unnecessary customer identifiers.

Risk: Broad trigger phrases could invoke the skill during ordinary business discussion.

Mitigation: Prefer explicit invocation when the user does not want revenue analysis to start automatically.

Risk: Stored memory about validated or corrected revenue patterns could retain business context longer than intended.

Mitigation: Review configured memory paths and retention practices before use in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-revenue)
- [理论底座 · 营收归因](references/理论底座.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown revenue attribution report with tables, caveats, and next-step guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask for revenue, order, customer, and pricing details; may save scoped memory when configured.]

## Skill Version(s):

0.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
