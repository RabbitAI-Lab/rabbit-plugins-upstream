## Description:

Query Canvas LMS (Instructure) from a shell with curl and a bearer access token instead of running the canvas-parent-mcp server - courses, grades, assignments, submissions, calendar, planner, announcements, conversations, discussions, and files for yourself or a linked observee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable Canvas users use this skill to have an agent produce curl-based Canvas API calls for retrieving course, grade, assignment, calendar, communication, discussion, and file data when the MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas bearer tokens and OAuth refresh tokens can expose private education data if they appear in shell history, logs, shared terminals, or broad environment dumps.

Mitigation: Use a private shell session, prefer safer credential-loading methods, scope and rotate tokens where possible, and keep Canvas credentials out of history, logs, and shared output.

Risk: The documented eval-based credential-loading example may execute unexpected shell content if the helper output is altered or untrusted.

Mitigation: Avoid eval in shared or logged shells; inspect the generated NAME=value output first or export the required variables explicitly.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses caller-supplied Canvas base URL and bearer or OAuth credentials; responses are expected to be JSON after removing Canvas's XSSI prefix.]

## Skill Version(s):

1.5.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
