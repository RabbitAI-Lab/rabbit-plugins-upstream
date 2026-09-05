## Description:

A Chinese-first dependency checkup skill that helps owner-operators identify who can unilaterally change their business, assess switching cost and time, and prepare practical Plan B actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External owner-operators and business leaders use this skill to map production-side dependencies across channels, premises and licenses, key people, suppliers, and payment rails. It produces a dependency report that highlights switching costs, switching time, backup options, expiration dates, unassessed items, and concrete next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive supplier, landlord, platform, payment, or key-person details may be retained in the configured memory location.

Mitigation: Use anonymized labels and avoid sharing names or business details that should not be stored.

Risk: A dependency can look controlled when switching cost or switching time has not been quantified.

Mitigation: Mark any item without concrete cost or time estimates as unassessed and revisit it with ranges before treating the risk as manageable.

Risk: Lease, license, permit, and contract dependencies may require professional review before action.

Mitigation: Use the skill to identify and prioritize risks, then have relevant legal or compliance details reviewed by qualified professionals.

## Reference(s):

- [理论底座 · 依赖](references/理论底座.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-dependency)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown dependency assessment report with tables and numbered next-step options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include calibrated memory notes when configured; reports should use anonymized counterparty labels when desensitization is enabled.]

## Skill Version(s):

0.2.4 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
