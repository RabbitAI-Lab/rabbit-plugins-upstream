## Description:

Query Canvas LMS (Instructure) from a shell with curl and a bearer access token for courses, grades, assignments, submissions, calendar, planner, announcements, conversations, discussions, and files for yourself or a linked observee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, administrators, parents, or students use this skill to compose curl requests that retrieve Canvas LMS profile, course, grade, assignment, calendar, conversation, discussion, and file data for themselves or an observed student.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The OAuth setup asks users to run an unpinned npm helper through shell eval while creating Canvas credentials.

Mitigation: Verify and pin the helper package before use, inspect generated environment exports before applying them, or prefer an institution-issued personal access token when permitted.

Risk: Canvas tokens and observee data can expose sensitive educational records.

Mitigation: Keep credentials in a private local shell environment, avoid logging tokens or API responses, and query or download only accounts and courses the user is authorized to access.

Risk: Manual file-download commands can overwrite local files if destinations are reused carelessly.

Mitigation: Check whether the destination exists and whether the parent directory is valid before using curl with an output path in scripts.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and Canvas API endpoint examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Canvas base URL and bearer token; examples return JSON through curl and jq.]

## Skill Version(s):

1.5.6 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
