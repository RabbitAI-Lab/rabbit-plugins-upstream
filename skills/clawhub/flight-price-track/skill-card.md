## Description:

Flight price monitoring and comparison assistant that searches multi-platform real-time fares, compares specific flights, scans low-price calendars, and helps prepare price-watch requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents use this skill to compare flight prices across listed travel platforms, evaluate buying timing, find lower-price departure dates, and prepare price-watch requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel route, date, and flight-search details are sent to publisher-operated proxy services.

Mitigation: Use the skill only for searches that can be shared with the publisher's proxy services, and avoid submitting unnecessary personal or sensitive travel details.

Risk: The security review notes an embedded shared token and unclear disclosure of external endpoints.

Mitigation: Prefer a release that requires a user-provided token and clearly names external endpoints before commercial deployment.

Risk: Returned booking links and same-price ordering may be affiliate-influenced.

Mitigation: Compare displayed platform prices independently before booking and treat booking links as convenience links rather than neutral recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/flight-price-track)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON results and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include booking links, route/date price summaries, price status analysis, and structured price-watch request details.]

## Skill Version(s):

2.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
