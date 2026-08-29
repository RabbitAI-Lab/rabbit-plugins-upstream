## Description:

零配置即装即用，支持火车票查询含12306实时余票、去火车站交通方式查询和住宿推荐，多旅游平台数据直连。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to look up China train ticket schedules, fares, and 12306 seat availability, then compare station transport options and hotel recommendations. It helps plan travel but does not directly purchase tickets or manage existing bookings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel searches, station routes, approximate or precise origin addresses, and hotel preferences are sent to third-party travel and map services through publisher proxy endpoints.

Mitigation: Install only if this data sharing is acceptable, and avoid entering unusually sensitive addresses or private itinerary details unless needed for the lookup.

Risk: Ticket availability, fares, transport times, taxi costs, and hotel recommendations can change or be estimates.

Mitigation: Confirm important details on the official booking or map page before purchase or travel.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/train-ticket-query)
- [Publisher profile](https://clawhub.ai/user/travel-skills)
- [12306 station data endpoint](https://kyfw.12306.cn/otn/resources/js/framework/station_name.js)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-formatted Chinese text with itinerary details, estimates, and links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include time-sensitive ticket availability, fare estimates, route estimates, hotel recommendations, and booking links.]

## Skill Version(s):

1.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
