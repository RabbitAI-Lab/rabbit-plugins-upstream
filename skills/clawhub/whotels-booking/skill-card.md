## Description: <br>
搜索万豪集团旗下W酒店，返回实时价格与预订链接，支持酒店详情查询和套餐优惠搜索，多旅游平台数据直连。暑期潮流旅行打卡，全球W酒店查询预订 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and travel-planning agents use this skill to search W Hotels by destination, review hotel details and package offers, and return booking links for follow-up purchase. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel search details are sent to the skill's proxy and downstream travel services. <br>
Mitigation: Use the skill only when that data sharing is acceptable, and avoid submitting sensitive personal or itinerary details unless the publisher's terms cover that use. <br>
Risk: The release evidence reports an embedded shared proxy token and an environment-defined proxy URL. <br>
Mitigation: The publisher should replace shared credentials with managed per-deployment credentials and document the expected proxy endpoint before broad use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/whotels-booking) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown-formatted Chinese text with hotel search results, details, package offers, prices, and booking links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prices, availability, and booking completion depend on the proxy and downstream travel services; users should verify final terms on the booking page.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
