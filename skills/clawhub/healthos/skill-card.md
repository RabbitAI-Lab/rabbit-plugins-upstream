## Description:

Read-only access to a HealthOS user's synced Apple Health data (daily summary, metrics, sleep, and workouts) via a personal read-scoped API token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarekjunied](https://clawhub.ai/user/tarekjunied)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to retrieve and summarize their own synced Apple Health data, including daily activity, vitals, sleep, workouts, and simple trends over a date range. The skill is for informational measurement reporting and should not be used for diagnosis or medical safety judgments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional HEALTHOS_API_URL override can redirect the bearer token to an arbitrary endpoint.

Mitigation: Use the default HealthOS API origin unless the endpoint is controlled and trusted; prefer an allowlisted or hard-coded API origin before attaching the token.

Risk: The skill handles sensitive personal health data and a personal API token.

Mitigation: Keep HEALTHOS_API_TOKEN in the environment only, avoid logging or prompting with it, and review outputs before sharing health data.

Risk: Health measurements could be mistaken for medical interpretation.

Mitigation: Report measurements, date range, source coverage, and simple trends only; direct medical-meaning questions to a clinician.

## Reference(s):

- [HealthOS API reference](references/api.md)
- [HealthOS developer documentation](https://healthosx.com/developers)
- [ClawHub HealthOS skill page](https://clawhub.ai/tarekjunied/skills/healthos)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should state the date range and source coverage, protect the API token, and avoid medical diagnosis.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
