## Description:

Searches tender and company data to identify prospective buyers, suppliers, and customer-development opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business-development teams use this skill to search procurement notices, examine company relationships, and prioritize potential customers and suppliers.

### Deployment Geography for Use:

Global (focused on Chinese procurement data)

## Known Risks and Mitigations:

Risk: Automatic registration can send device features, including a hashed MAC address, to the provider.

Mitigation: Require informed consent before registration; configure ZLBX_API_KEY manually to skip device collection and account creation.

Risk: An automatically issued API key is stored locally and used for account and data requests.

Mitigation: Protect ~/.zlbx/config.json, avoid sharing the key in responses, and review account-maintenance requests before enabling the skill.

Risk: Company records can be snapshots, and paid data queries may consume account credits.

Mitigation: Check data dates and source context, and limit paid queries to the user's requested scope.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/precision-tender-sourcing-xunbiaobao)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Company analysis API reference](artifact/references/api-company.md)
- [Tender search API reference](artifact/references/api-search.md)
- [Automatic registration and credential handling](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and lists of tender opportunities, buyers, and suppliers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the provider's data coverage and may include dated company snapshots.]

## Skill Version(s):

2.0.7 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
