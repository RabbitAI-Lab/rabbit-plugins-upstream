## Description:

Query Canvas LMS (Instructure) from a shell with curl and a bearer access token instead of running the canvas-parent-mcp server — courses, grades, assignments, submissions, calendar, planner, announcements, conversations, discussions, and files for yourself or a linked observee. Use when you want Canvas data without the MCP, in a script, or on a machine where the MCP isn't installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students, parents, and guardians use this skill to query their own Canvas data or a linked observee's courses, grades, assignments, messages, and files from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The QR-login example runs an external helper and evaluates its output, which could expose credentials or execute unexpected shell code.

Mitigation: Verify and pin the helper; capture and validate its expected fields, then export them without eval.

Risk: Sending a bearer token to an incorrect host could disclose Canvas account access.

Mitigation: Use the verified HTTPS origin for the institution and validate the destination host before sending credentials.

Risk: Downloads and queries may expose or overwrite private student records, and conversation queries may mark messages as read.

Mitigation: Save records only in a private location with overwrite protection and cleanup, and disable automatic message read-marking for queries.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/canvas-parent-api)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use placeholders for institution-specific URLs, IDs, and credentials.]

## Skill Version(s):

2.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
