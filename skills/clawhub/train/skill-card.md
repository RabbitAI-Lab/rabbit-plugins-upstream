## Description:

Supports train station-to-station, train-line, and ticket-availability queries using the JisuAPI train inquiry service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jisuapi](https://clawhub.ai/user/jisuapi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to look up China train routes, train stops, fares, schedules, and remaining ticket availability from natural-language rail travel requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Train routes, dates, train numbers, and the configured JisuAPI AppKey are sent to JisuAPI.

Mitigation: Use a scoped key if available, avoid logging full request URLs, monitor quota or billing, and rotate the key if it may appear in logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jisuapi/skills/train)
- [JisuAPI train API documentation](https://www.jisuapi.com/api/train/)
- [JisuAPI homepage](https://www.jisuapi.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and the JISU_API_KEY environment variable.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
