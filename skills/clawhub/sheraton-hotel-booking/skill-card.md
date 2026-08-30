## Description:

搜索万豪集团旗下喜来登酒店并返回实时价格与预订链接，支持酒店详情查询和套餐优惠搜索。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-assistant agents use this skill to search Sheraton hotels, inspect hotel details, and find package offers with live prices and booking links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search destinations, dates, hotel names, and related filters are sent to an external proxy service to retrieve live hotel results.

Mitigation: Use the skill only for intended Sheraton hotel searches and avoid sending unnecessary sensitive traveler details.

Risk: Live hotel prices, availability, details, and package data depend on the external service response and may be incomplete or unavailable.

Mitigation: Show only returned data, preserve booking links when present, and do not add prices, ratings, amenities, or hotel details that the tool did not return.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/sheraton-hotel-booking)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with hotel search results, details, package offers, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results should reflect returned hotel data without adding unsupported prices, ratings, amenities, or booking details.]

## Skill Version(s):

1.1.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
