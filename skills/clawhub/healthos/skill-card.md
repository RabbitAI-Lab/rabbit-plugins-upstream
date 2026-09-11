## Description:

Read-only access to a HealthOS user's synced Apple Health data, including daily summaries, metrics, sleep, workouts, and raw archived samples and events through a personal read-scoped API token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarekjunied](https://clawhub.ai/user/tarekjunied)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and their agents use this skill to answer questions about the user's own HealthOS-synced Apple Health data, such as daily activity, sleep, workouts, vitals, and historical trends. It is intended for measurement reporting and simple trend summaries, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive HealthOS and Apple Health data that the user has synced, including raw samples and category events.

Mitigation: Install only for users who approve agent read access to this data; keep HEALTHOS_API_TOKEN narrowly scoped as an environment secret and revoke or rotate it when access is no longer needed.

Risk: Health measurements may be mistaken for medical diagnosis or safety guidance.

Mitigation: Report measurements, units, date ranges, source coverage, and simple trends only; suggest a clinician when the user asks for medical interpretation.

## Reference(s):

- [HealthOS developer program](https://healthosx.com/developers)
- [HealthOS API docs](https://api.healthosx.com/docs)
- [HealthOS API LLM reference](https://api.healthosx.com/llms.txt)
- [HealthOS API reference](references/api.md)
- [ClawHub skill page](https://clawhub.ai/tarekjunied/skills/healthos)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or plain text responses, with JSON returned by the helper script when used directly.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers should cite date range and source coverage, and should avoid diagnosis or claims that a reading is safe or dangerous.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
