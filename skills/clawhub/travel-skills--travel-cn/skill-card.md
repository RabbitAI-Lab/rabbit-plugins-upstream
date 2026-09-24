## Description:

旅行信息查询 - 去哪儿/携程/飞猪数据查询（Expedia 中国版）

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Travel planners, business travelers, and developers use this skill to compare China travel options, query flights, hotels, trains, and attractions, and plan or monitor trip costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel queries may send city, route, date, and booking-related details to third-party travel providers.

Mitigation: Use official provider APIs where available, share only the data needed for the query, and avoid embedding credentials directly in commands or scripts.

Risk: Scraping travel sites may violate provider terms or trigger blocking.

Mitigation: Review provider terms before scraping, prefer approved APIs, and review any local scripts before running them.

Risk: Travel prices and availability can change quickly.

Mitigation: Verify prices, availability, and booking terms directly with the provider before making travel decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/travel-cn)
- [Ctrip flight search API example](https://api.ctrip.com/flight/search?from=SHA&to=PEK&date=2026-02-20)
- [Qunar flight search page](https://flight.qunar.com/)
- [Ctrip hotel search API example](https://api.ctrip.com/hotel/search?city=上海&checkin=2026-02-20)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash and Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes travel-provider API examples, scraping examples, and quick script command examples.]

## Skill Version(s):

1.0.0 (source: package.json, release evidence, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
