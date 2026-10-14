## Description:

Searches healthcare procurement notices and identifies purchasing hospitals, winning suppliers, and leading suppliers for a selected hospital.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement researchers and healthcare business teams use this skill to find hospital tenders, identify awardees, and examine supplier activity using Zhiliaobiaoxun data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries use an external procurement-data service and require an API key.

Mitigation: Use a key you are comfortable supplying to Zhiliaobiaoxun, protect stored credentials, and review account usage.

Risk: Optional trial registration uses device features, including a hashed MAC address, and stores the returned key locally.

Mitigation: Require informed consent before registration; decline and configure a key manually if device-based registration is unwanted.

Risk: Supplier rankings and company relationships can be misleading when records are incomplete.

Mitigation: Describe only returned records, distinguish award history from confirmed relationships, and avoid guessing from missing data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thuanlynham-stack/skills/medical-health-bid-radar-yiliaozhaobiaocaigouwang)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Procurement search API reference](references/api-search.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results reflect retrieved procurement records and available account credits.]

## Skill Version(s):

1.0.9 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
