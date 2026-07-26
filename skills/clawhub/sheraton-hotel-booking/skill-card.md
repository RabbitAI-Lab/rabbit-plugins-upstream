## Description: <br>
搜索万豪集团旗下喜来登酒店，返回实时价格与预订链接，支持酒店详情查询和套餐优惠搜索，基于飞猪官方数据直连。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to search Sheraton hotels, compare nightly prices, inspect hotel details, and obtain booking links for completion on Fliggy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel destinations, dates, and query terms are sent through a cloud proxy whose endpoint is not clearly declared. <br>
Mitigation: Install only when the proxy data flow is acceptable for the intended users, and avoid submitting sensitive personal travel details. <br>
Risk: The artifact includes a shared embedded proxy token according to the security evidence. <br>
Mitigation: Review token handling before deployment and prefer per-installation or managed credentials where available. <br>
Risk: Hotel prices, package details, and availability may change after the skill returns results. <br>
Mitigation: Confirm current price, availability, and booking terms on the linked Fliggy page before purchase. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/sheraton-hotel-booking) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-style text with hotel listings, detail summaries, prices, IDs, and booking links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results depend on the configured proxy and the upstream travel platform; prices and availability should be confirmed on the booking page.] <br>

## Skill Version(s): <br>
1.1.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
