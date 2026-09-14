## Description:

基于飞常准数据，提供航班实时动态、延误分析、舒适度评分、机场天气查询，覆盖全球航班，零配置即用。暑期航班实时动态

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers, travel support agents, and operations users use this skill to check live flight status, route delay conditions, comfort comparisons, and airport weather from flight numbers, routes, dates, airports, or city names.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flight numbers, routes, dates, and airport queries are sent through the publisher's fixed proxy service.

Mitigation: Install only when that data flow is acceptable, and avoid submitting sensitive travel details unless the proxy operator is trusted.

Risk: The source includes a shared proxy token.

Mitigation: The publisher should remove and rotate the embedded token and require secure runtime configuration.

Risk: Broad activation patterns can cause the skill to handle general flight or airport-weather requests.

Mitigation: Review activation behavior before routine deployment and tighten routing patterns where needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/variflight-tracker)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown summaries with tables, plus JSON-formatted error messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs flight status, route status, comfort scores, and airport weather assessments for user-provided travel queries.]

## Skill Version(s):

1.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
