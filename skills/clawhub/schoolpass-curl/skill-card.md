## Description:

Read a SchoolPass parent account directly with curl against the regional SchoolPass REST API for one-off terminal checks of students, calendars, pickup changes, drivers, dismissal locations, and school information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill for one-off shell access to their own SchoolPass parent account, including reading student records, dismissal calendars, pickup changes, authorized drivers, dismissal locations, and school information. It is best suited for terminal checks and scripts when a conversational MCP server is not running.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reference recipes include live write and delete examples for student arrival or dismissal changes.

Mitigation: Review commands before execution, use write and delete examples only intentionally, and re-read the calendar to confirm any change or cancellation.

Risk: SchoolPass credentials, bearer tokens, and account data may be exposed in shared transcripts or unattended terminal sessions.

Mitigation: Protect SCHOOLPASS_EMAIL, SCHOOLPASS_PASSWORD, and bearer tokens; avoid echoing secrets or responses into shared logs.

Risk: Using the wrong SchoolPass host or school code can send requests to the wrong regional shard or fail authorization.

Mitigation: Verify the school host and AppCode from the signed-in SchoolPass portal before running API requests.

## Reference(s):

- [Ready-to-run requests](artifact/references/requests.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, curl, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request bodies and response-filtering recipes; does not itself store bearer tokens.]

## Skill Version(s):

0.3.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
