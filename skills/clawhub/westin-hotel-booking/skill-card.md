## Description:

搜索万豪集团旗下威斯汀酒店并返回实时价格与预订链接，支持酒店详情查询和套餐优惠搜索。当用户需要预订威斯汀酒店、查找Westin酒店价格时使用

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travel-planning users use this skill to find Westin hotels, compare prices, open booking links, review hotel details, and search package offers. Agents should present only the hotel data returned by the skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel searches can send cities, dates, hotel names, and review keywords to an external proxy that is not clearly disclosed in the user-facing instructions.

Mitigation: Review the proxy disclosure and avoid using sensitive travel plans unless the data-sharing behavior is acceptable.

Risk: Hotel prices, availability, package offers, and booking links can change after the skill returns results.

Mitigation: Confirm current terms on the booking page before making a reservation.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with hotel details, prices, hotel IDs, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are constrained to script-returned hotel data and may include live prices, addresses, room details, package offers, and booking URLs.]

## Skill Version(s):

1.1.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
