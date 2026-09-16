## Description:

喜来登酒店查询服务已调整，原品牌酒店数据专区数据源暂停，现引导用户使用全球酒店搜索、酒店比价等通用酒店技能查询喜来登/Sheraton等品牌酒店。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill as a legacy Sheraton hotel entry point that explains the retired brand-specific service and redirects them to general hotel search, hotel price comparison, or travel-platform skills for current availability and booking options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expect the skill to directly search or book Sheraton hotels even though the Sheraton-specific service has been retired.

Mitigation: The skill should clearly present the service-adjustment notice and direct users to general hotel-search, price-comparison, or travel-platform skills before they make travel decisions.

Risk: The skill output is Chinese-language guidance, which may not fit users or deployments that require another language.

Mitigation: Use the skill where Chinese-language hotel guidance is acceptable, or provide an appropriate translation layer for the target audience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/sheraton-hotel-booking)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text guidance in Chinese]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No direct hotel search, detail, package, or booking results are produced.]

## Skill Version(s):

1.1.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
