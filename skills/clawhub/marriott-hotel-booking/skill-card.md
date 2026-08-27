## Description:

搜索万豪集团旗下酒店并返回实时价格与预订链接，支持酒店详情查询和套餐优惠搜索。当用户需要预订万豪酒店、找喜来登、威斯汀、丽思卡尔顿、JW万豪、万丽、万枫、瑞吉等万豪旗下品牌酒店时使用

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Travel-booking agents and users use this skill to search Marriott-family hotels, inspect hotel details, and find package offers with prices and booking links from the reported Feizhu Marriott source.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel-search details may be sent through the publisher's Tencent SCF proxy.

Mitigation: Review before installing and only use the skill where routing these queries through that publisher-operated proxy is acceptable.

Risk: The distributed script includes an embedded proxy credential.

Mitigation: Treat the credential as exposed release material and verify the publisher's proxy controls before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/marriott-hotel-booking)
- [ClawHub publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown text with booking links and command-line tool invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search, detail, and package results depend on the script parameters and returned data.]

## Skill Version(s):

1.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
