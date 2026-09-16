## Description:

万怡酒店查询服务已调整，原品牌酒店数据专区数据源暂停，现引导使用全球酒店搜索、酒店比价等通用酒店技能查询万怡/Courtyard等品牌酒店。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users can keep legacy Courtyard/万怡 hotel query calls working while receiving a clear notice to use general hotel search or price-comparison skills for current hotel results and booking options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expect this skill to return live Courtyard search, detail, package, or booking data even though the dedicated data source is no longer available.

Mitigation: Present the skill as a compatibility stub and follow its notice to use general hotel search or price-comparison skills for current results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/courtyard-hotel-booking)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text notice]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the same Chinese service-adjustment notice for search, detail, and packages calls.]

## Skill Version(s):

1.1.7 (source: release evidence; artifact _meta.json shows 1.1.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
