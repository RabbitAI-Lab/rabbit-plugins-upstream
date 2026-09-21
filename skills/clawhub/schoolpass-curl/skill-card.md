## Description:

Read a SchoolPass parent account directly with curl against the regional SchoolPass REST API for one-off shell access to students, arrival and dismissal calendars, pickup changes, drivers, dismissal locations, and school information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and authorized SchoolPass parent-account users use this skill to generate curl and jq commands for inspecting their own SchoolPass account data from a shell. It is best suited for one-off checks and scripted reads, not repeated conversational workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reference guide includes POST and DELETE examples that can create or cancel live student arrival or dismissal changes.

Mitigation: Run write or delete examples only after confirming the student, school, date, change type, identifier, and intended outcome; prefer read-only commands for routine checks.

Risk: Shell commands require SchoolPass parent-account credentials and bearer tokens.

Mitigation: Keep credentials in local environment variables, avoid echoing passwords or bearer tokens into shared transcripts, and retry rejected logins only after correcting credentials.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass-curl)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided SchoolPass credentials, school code, and regional API host.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
