## Description:

同程旅行助手帮助代理搜索酒店、机票、火车票、汽车票、景点门票、综合交通和度假线路，并返回价格、评分、时刻、余票和预订链接等结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel planners use this skill to search Tongcheng travel products from natural-language city, route, date, and preference inputs. It supports comparison and discovery across lodging, transportation, attractions, and vacation packages, with booking completed outside the skill through returned links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel destinations, dates, and preferences are sent through the skill's cloud proxy to the Tongcheng API.

Mitigation: Avoid entering highly sensitive itinerary details, and review the publisher's data-flow and retention disclosures before normal approval.

Risk: The security evidence reports that the artifact ships a reusable proxy token.

Mitigation: Rotate the exposed token, remove it from source, and use scoped per-install credentials or a secret manager.

Risk: Travel prices and availability can change after the skill returns results.

Mitigation: Verify prices, availability, and terms on the returned Tongcheng booking page before purchase.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/tongcheng-travel-assistant)
- [ClawHub publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, markdown]

**Output Format:** [Markdown travel search results with prices, availability, ratings, schedules, and booking links when returned by the upstream service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are query-dependent and may change as live prices and availability change.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
