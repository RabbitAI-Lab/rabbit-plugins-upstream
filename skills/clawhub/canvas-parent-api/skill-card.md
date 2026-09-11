## Description:

Query Canvas LMS from a shell with curl and a bearer access token for courses, grades, assignments, submissions, calendar, planner, announcements, conversations, discussions, and files for yourself or a linked observee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support staff, and Canvas users use this skill to ask an agent for direct Canvas REST API curl commands and setup guidance when an MCP server is unavailable or unnecessary. It is aimed at retrieving Canvas account, course, grade, assignment, communication, and file data using a user-provided bearer token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The OAuth setup example can execute an unpinned npx helper through eval.

Mitigation: Use the personal access token path when available, or pin and review the OAuth helper before running it.

Risk: Canvas access tokens, refresh tokens, and client secrets can leak through shell history, logs, or broad environment variables.

Mitigation: Keep secrets in a narrowly scoped shell or secrets manager, avoid logging command output that contains credentials, and unset sensitive variables after use.

Risk: Bearer tokens could be sent to the wrong host if Canvas base URLs or file URLs are manipulated.

Mitigation: Use only verified HTTPS Canvas institution URLs and validate file download URLs before sending Authorization headers.

Risk: The skill can retrieve sensitive Canvas education records and private messages.

Mitigation: Use the least-privileged token available and review retrieved data before saving, sharing, or forwarding it.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include jq projections, Canvas API paths, environment variable setup, pagination loops, and token refresh guidance.]

## Skill Version(s):

1.5.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
