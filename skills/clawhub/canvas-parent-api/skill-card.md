## Description:

Helps agents query Canvas LMS data with curl and a bearer token for courses, grades, assignments, submissions, calendar items, messages, discussions, and files without running the canvas-parent-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, students, and Canvas observer accounts use this skill to construct shell commands for reading Canvas LMS data directly from their institution's Canvas API. It is useful when an agent needs Canvas course, grade, assignment, submission, calendar, conversation, discussion, or file guidance without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas access tokens, OAuth secrets, refresh tokens, or QR-login URLs can expose private Canvas data if shared or logged.

Mitigation: Use a private shell, avoid placing secrets in shared logs, screenshots, or CI, and revoke Canvas tokens if they may have been exposed.

Risk: Generated commands can retrieve private student, observer, course, conversation, or file data from the Canvas institution configured by the user.

Mitigation: Confirm the Canvas base URL, course IDs, observee IDs, request path, and download destination before executing commands.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Canvas base URL and bearer token or OAuth refresh credentials; Canvas responses may require XSSI prefix stripping and Link-header pagination.]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
