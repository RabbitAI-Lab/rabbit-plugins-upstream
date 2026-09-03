## Description:

查询长江三峡游轮和城市游船船票信息，并返回价格、航线方向、退改政策、去码头交通、景点门票和住宿推荐。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel-planning agents use this skill to compare domestic China river and city cruise tickets, plan transportation to piers, and find nearby attractions or hotels. The skill provides discovery and booking links, but does not purchase tickets or manage existing bookings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cruise searches, origin and destination locations, city names, attraction keywords, and hotel preferences are sent through publisher cloud proxies and external travel/map providers.

Mitigation: Use the skill only when that data sharing is acceptable, and avoid entering sensitive personal details in hotel or route queries.

Risk: Ticket prices, availability, refund terms, routes, and travel-time estimates can change after the skill returns results.

Mitigation: Confirm final price, availability, refund policy, and route details on the linked provider page before purchase or travel.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/cruise-ticket-query)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-style Chinese text with lists, prices, route details, caveats, and booking links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include real-time travel data from cloud proxy services and external travel/map providers; prices, availability, and route estimates can change.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
