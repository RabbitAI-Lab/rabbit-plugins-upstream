## Description:

Provides curl and jq recipes for accessing SchoolPass parent-account information and submitting or canceling student dismissal changes through the regional API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and authorized assistants use these shell recipes to check student calendars, pickup changes, drivers, and school details. The included write commands can also submit or cancel dismissal changes when deliberately authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ready-to-run write and delete commands can change or cancel real student dismissal records.

Mitigation: Run change or cancellation commands only with deliberate authorization, then re-read the calendar to confirm the result.

Risk: Parent credentials, bearer tokens, and student information may be exposed in shell history, logs, shared terminals, or transcripts.

Mitigation: Protect credentials, tokens, and API output; do not copy sensitive values into shared histories, logs, or transcripts.

## Reference(s):

- [SchoolPass Curl release on ClawHub](https://clawhub.ai/chrischall/skills/schoolpass-curl)
- [Ready-to-run requests](references/requests.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a SchoolPass parent account, school code, and regional API host.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
