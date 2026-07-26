## Description: <br>
万豪集团旗下万怡酒店实时搜索，返回价格与预订链接，支持酒店详情和套餐优惠查询，多旅游平台数据直连，零配置即装即用。暑期商旅出行优选，万怡酒店全球查询预订 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and travel-planning agents use this skill to search Courtyard by Marriott hotels, review prices, locations, details, package offers, and follow booking links. It is intended for external hotel discovery and booking assistance, not direct reservation execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel destinations, dates, hotel names, and keywords are sent to a cloud proxy and travel API provider. <br>
Mitigation: Use only when that data sharing is acceptable, avoid entering sensitive travel details, and review proxy and token configuration before deployment. <br>
Risk: Hotel prices, availability, package details, and booking links may change after search results are returned. <br>
Mitigation: Confirm final price, availability, policies, and booking terms on the linked booking page before purchase. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/travel-skills/skills/courtyard-hotel-booking) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown text in Chinese with hotel listings, details, package offers, prices, addresses, and booking links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results depend on cloud proxy and travel API availability; prices and availability can change before booking.] <br>

## Skill Version(s): <br>
1.1.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
