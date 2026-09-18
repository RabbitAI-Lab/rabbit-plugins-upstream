## Description:

W酒店查询服务已调整，原品牌酒店数据源暂停后，该技能保留 W Hotels 查询入口并引导用户使用通用酒店搜索、酒店比价或旅行平台技能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travel users use this legacy W Hotels entry point to receive guidance for finding W Hotels through available general hotel-search, price-comparison, or travel-platform skills. It is useful for compatibility with historical search, detail, and package tool calls after the former W Hotels-specific data source was suspended.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expect live W Hotels search, hotel details, package lookup, or booking support from this legacy entry point.

Mitigation: Present it as a compatibility stub and direct users to general hotel-search, hotel price-comparison, or travel-platform skills for current availability and pricing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/whotels-booking)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a fixed service-adjustment notice from the retained search, detail, and packages tool entries.]

## Skill Version(s):

1.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
