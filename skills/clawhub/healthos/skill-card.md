## Description:

Read-only access to a HealthOS user's synced Apple Health data, including daily summaries, metrics, sleep, workouts, and raw archive samples and events through a personal read-scoped API token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarekjunied](https://clawhub.ai/user/tarekjunied)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to answer questions about the user's own synced Apple Health data, including activity, vitals, sleep, workouts, and date-range trends. It reports measurements and simple trends without diagnosis or medical interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read broad and sensitive HealthOS and Apple Health records, including raw samples and events.

Mitigation: Use the narrowest read-scoped token available and ask for explicit confirmation before broad raw archive lookups.

Risk: A bearer token for health data could expose private records if mishandled.

Mitigation: Store HEALTHOS_API_TOKEN in a protected secret mechanism or locked-down configuration, never place it in prompts or command arguments, and rotate or revoke it if exposed.

Risk: Health measurements may be mistaken for medical conclusions.

Mitigation: Report measurements and simple trends only, cite date range and source coverage, and direct medical interpretation questions to a clinician.

## Reference(s):

- [HealthOS API reference](references/api.md)
- [HealthOS developer program](https://healthosx.com/developers)
- [HealthOS OpenAPI documentation](https://api.healthosx.com/docs)
- [HealthOS llms.txt](https://api.healthosx.com/llms.txt)
- [ClawHub skill page](https://clawhub.ai/tarekjunied/skills/healthos)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results summarized for the user]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers should state date range and source coverage, avoid medical diagnosis, and keep the API token out of prompts, arguments, logs, and examples.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata; SKILL.md frontmatter says 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
