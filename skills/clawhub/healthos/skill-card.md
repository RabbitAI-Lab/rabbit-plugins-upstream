## Description:

Read-only access to a HealthOS user's synced Apple Health data - daily summary, metrics, sleep, workouts, and the full raw archive via a personal read-scoped API token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarekjunied](https://clawhub.ai/user/tarekjunied)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to answer questions about the user's own synced HealthOS and Apple Health records, including daily summaries, sleep, workouts, metrics, and raw sample or event history. It is intended for reporting measurements and simple trends, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent read access to sensitive HealthOS and Apple Health records, including raw sample and event history.

Mitigation: Install only with user consent, use a least-privilege read token in HEALTHOS_API_TOKEN, and request narrow date ranges and specific data types when possible.

Risk: Health measurements may be misread as medical conclusions.

Mitigation: Report measurements and simple trends only, state date range and coverage, and direct medical interpretation questions to a clinician.

Risk: The API token could expose health records if copied into prompts, arguments, files, or logs.

Mitigation: Keep the token only in the HEALTHOS_API_TOKEN environment variable and do not echo, log, or include it in examples.

## Reference(s):

- [HealthOS API reference](references/api.md)
- [HealthOS developer program](https://healthosx.com/developers)
- [HealthOS API docs](https://api.healthosx.com/docs)
- [HealthOS LLM reference](https://api.healthosx.com/llms.txt)
- [ClawHub skill page](https://clawhub.ai/tarekjunied/skills/healthos)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with JSON API results summarized for the user]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should state the date range and source coverage, avoid diagnosis, and keep tokens out of prompts, arguments, logs, and examples.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
