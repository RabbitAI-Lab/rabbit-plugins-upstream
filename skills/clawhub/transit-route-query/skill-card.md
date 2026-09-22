## Description:

Queries urban bus and metro routes, prioritizes metro options, and returns transfer plans for fastest, fewer-transfer, or less-walking strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to ask for same-city public transit directions between an origin and destination, with route plans organized around metro, bus, walking, estimated duration, and transfer details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-entered origin, destination, and city information is sent to the skill publisher's cloud proxy for route lookup.

Mitigation: Avoid entering sensitive private locations and use the skill only when sharing route query details with the publisher's proxy is acceptable.

Risk: Transit times, fares, and route options are estimates and do not provide real-time official arrival guarantees.

Mitigation: Verify time-sensitive trips, last trains, fares, and service disruptions against local transit operators or a live map application before traveling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/transit-route-query)
- [Disclosed cloud proxy endpoint](https://1439498936-bl10af74fl.ap-guangzhou.tencentscf.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown-formatted route summary with transit segments, walking steps, estimated duration, fare estimates, and caveats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns one route-planning response per query; inputs include origin, destination, city, and optional route strategy.]

## Skill Version(s):

1.0.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
