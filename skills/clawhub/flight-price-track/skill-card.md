## Description:

Helps agents compare real-time flight prices across travel platforms, assess fare levels, scan flexible dates, and prepare price-watch requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travel users and agents use this skill to search flight options, compare fares across platforms, identify lower-price travel dates, and set up target-price monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared proxy token is embedded in the artifact.

Mitigation: Remove and rotate the token before release, and load credentials from the declared PROXY_TOKEN environment variable or a managed secret store.

Risk: Monitoring output can include a shell command string.

Mitigation: Treat check_command as untrusted data; pass structured monitoring arguments to the host scheduler and avoid shell execution.

Risk: The skill sends flight query parameters to external proxy endpoints.

Mitigation: Review the endpoints before installation, document the data flow for users, and limit outbound network access to approved services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/flight-price-track)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [JSON from the helper script with concise Markdown guidance from the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search, comparison, calendar, and monitoring outputs may include route/date inputs, fare analysis, booking URLs, and monitor task details.]

## Skill Version(s):

2.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
