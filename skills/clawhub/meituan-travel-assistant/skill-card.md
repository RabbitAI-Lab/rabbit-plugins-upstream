## Description:

美团旅行助手支持用自然语言查询酒店、机票、火车票、景点门票和行程规划，覆盖300+城市。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to ask natural-language travel questions and receive hotel, flight, train ticket, scenic ticket, booking-link, and itinerary information for supported Chinese cities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel queries, city names, and itinerary details are sent to a configured proxy service.

Mitigation: Install only when this data flow is acceptable and avoid submitting sensitive personal details.

Risk: The release security summary flags an exposed default proxy token and configurable proxy destination.

Mitigation: The publisher should remove and rotate the embedded token, align documented and implemented environment variables, and restrict proxy URLs to trusted hosts before broad use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/meituan-travel-assistant)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [JSON from the tool, typically summarized by the agent as Markdown or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include travel search results, prices, schedules, itinerary suggestions, and booking links; results depend on the configured proxy service.]

## Skill Version(s):

2.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
