## Description:

通过中国招投标与企业数据查找采购机会、潜在客户及企业合作伙伴，并整理可供跟进的目标列表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business-development teams use this skill to search tender notices, identify prospective purchasers, examine company customers and suppliers, and prioritize outreach leads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service receives an API key and package identity when queried, and the skill checks account and update status.

Mitigation: Use a personally configured ZLBX_API_KEY and review the provider's credential and usage terms before enabling requests.

Risk: Optional trial registration sends hashed device characteristics to the provider.

Mitigation: Configure an API key to skip registration, or require informed user consent before collecting device characteristics.

Risk: Requested business contact results can contain full phone numbers for paid accounts.

Mitigation: Limit access and sharing to the stated outreach purpose; preserve masked numbers and avoid bulk contact exports.

Risk: Data queries can consume account credits and incomplete company records can lead to overconfident conclusions.

Mitigation: Query only requested records and pages, check applicable charges, and distinguish returned facts from unknown or unqueried data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/precision-tender-sourcing-xunbiaobao)
- [Search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Company registry interpretation](references/api-registry.md)
- [Optional trial registration and privacy](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries, linked result tables, and follow-up suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the provider's returned records and account access; contact numbers may be masked.]

## Skill Version(s):

2.0.6 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
