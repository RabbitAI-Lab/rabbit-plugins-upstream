## Description: <br>
搜索万豪集团旗下丽思卡尔顿酒店，返回实时价格与预订链接，支持酒店详情查询和套餐优惠搜索。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to search Ritz-Carlton hotels, inspect hotel details, compare package offers, and follow booking links returned by travel-platform results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel-search details are sent to an unspecified proxy and downstream travel APIs. <br>
Mitigation: Use the skill only when the publisher and proxy configuration are trusted, and avoid entering sensitive itinerary details. <br>
Risk: Prices, availability, package terms, and booking links come from third-party travel results. <br>
Mitigation: Verify all prices, availability, and booking terms on the destination booking page before relying on them. <br>
Risk: The security verdict is suspicious because the skill uses an embedded proxy token and may overstate data-source transparency. <br>
Mitigation: Review the proxy configuration and token handling before deployment, and document the actual data sources exposed to users. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/ritz-carlton-hotel-booking) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown-formatted text with hotel details, prices, package summaries, and booking links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results depend on proxy and downstream travel API responses; booking links and availability should be verified on the destination booking page.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release evidence; artifact frontmatter lists 1.1.2 and _meta.json lists 1.1.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
