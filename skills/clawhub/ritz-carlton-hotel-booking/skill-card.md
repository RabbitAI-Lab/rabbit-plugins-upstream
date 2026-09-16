## Description:

丽思卡尔顿酒店查询服务已调整，原品牌酒店数据专区数据源暂停，现引导用户使用全球酒店搜索、酒店比价等通用酒店技能查询丽思卡尔顿/Ritz-Carlton等品牌酒店。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travel users use this skill as a compatibility entry point for Ritz-Carlton hotel queries after the dedicated Marriott-brand data source was paused. It returns guidance directing users to general hotel search, hotel price comparison, or travel-platform skills for current Ritz-Carlton availability, pricing, and booking links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake the preserved Ritz-Carlton entry points for live dedicated hotel search or booking functionality.

Mitigation: The skill should clearly state that dedicated Marriott-brand search is offline and direct users to separate hotel-search or price-comparison skills for live availability, pricing, and booking links.

Risk: Any live pricing or booking action depends on other hotel-search skills with separate permissions and trust considerations.

Mitigation: Review and trust the downstream hotel-search skills before relying on their prices, availability, or booking links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/ritz-carlton-hotel-booking)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, guidance, shell commands]

**Output Format:** [Plain text guidance returned by preserved search, detail, and packages tool entry points; Markdown may describe example command usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not directly search, price, or book hotels; live hotel results depend on separate hotel-search skills.]

## Skill Version(s):

1.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
