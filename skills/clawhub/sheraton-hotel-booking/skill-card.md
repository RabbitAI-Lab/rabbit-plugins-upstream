## Description:

喜来登酒店查询服务已调整，原品牌酒店数据专区数据源暂停，现引导使用全球酒店搜索、酒店比价等通用酒店技能查询喜来登/Sheraton等品牌酒店。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel assistants use this skill as a compatibility entry point for Sheraton hotel queries after the dedicated Sheraton data source was retired. It directs users toward general hotel search, hotel price comparison, and travel-platform skills for current Sheraton/Sheraton-branded hotel information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake this retired Sheraton-specific skill for a source of live hotel prices, availability, or booking links.

Mitigation: Treat the output as redirect guidance only and review the recommended hotel-search skills before relying on their prices, booking links, or travel decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/sheraton-hotel-booking)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Plain text guidance from compatibility tool entry points, with Markdown documentation and a bash example]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The search, detail, and packages entry points all return the same service-adjustment notice and redirect users to general hotel-search skills.]

## Skill Version(s):

1.1.9 (source: server release metadata; artifact _meta.json reports 1.1.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
