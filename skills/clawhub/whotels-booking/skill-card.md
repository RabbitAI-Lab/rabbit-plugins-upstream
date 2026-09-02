## Description:

搜索万豪集团旗下W酒店并返回实时价格与预订链接，支持酒店详情查询和套餐优惠搜索。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and booking assistants use this skill to search W Hotels by destination, retrieve hotel details, compare package offers, and present booking links using only the script output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User travel search details are sent to a hardcoded external proxy service.

Mitigation: Install only when this data transfer is acceptable, and disclose the outbound service and transmitted travel fields before use.

Risk: The artifact includes an embedded proxy token.

Mitigation: Remove and rotate the embedded token, then use a deployment-managed secret instead.

Risk: Activation may be broader than users expect for booking and hotel-search intents.

Mitigation: Narrow activation to clear W Hotels booking, pricing, hotel-detail, or package-search requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/travel-skills/skills/whotels-booking)
- [Skill Instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown-formatted hotel search, detail, and package results with booking links and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve hotel names, prices, ratings, details, and booking links exactly as returned by the script.]

## Skill Version(s):

1.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
