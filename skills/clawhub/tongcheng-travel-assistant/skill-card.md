## Description:

同程旅行全品类搜索，酒店/机票/火车票/汽车票/景点门票/综合交通/度假线路7大品类全覆盖，含预订链接和实时价格，零配置即装即用。暑期同程旅行特惠，景点酒店一站预订

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel assistants use this skill to search Tongcheng travel products across hotels, flights, trains, buses, scenic tickets, multimodal transport, and vacation packages. It returns current options, prices, ratings, schedules, and booking links while leaving booking and payment to Tongcheng.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel search text, including destinations, dates, route preferences, and similar details, is sent through a cloud proxy to Tongcheng.

Mitigation: Avoid unnecessary personal or confidential details in queries, and complete booking or payment only on the destination Tongcheng page or app.

Risk: Prices, availability, and schedules can change after results are returned.

Mitigation: Confirm final pricing, route details, and availability on Tongcheng before booking.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/tongcheng-travel-assistant)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown travel search results with prices, schedules, ratings, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on Tongcheng availability and may change before booking.]

## Skill Version(s):

1.2.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
