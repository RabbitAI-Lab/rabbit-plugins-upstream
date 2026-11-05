## Description:

Query Canvas LMS (Instructure) from a shell with curl and a bearer access token instead of running the canvas-parent-mcp server — courses, grades, assignments, submissions, calendar, planner, announcements, conversations, discussions, and files for yourself or a linked observee. Use when you want Canvas data without the MCP, in a script, or on a machine where the MCP isn't installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Canvas users and developers can use these shell examples to retrieve their own or a linked observee's courses, grades, assignments, messages, and other LMS data without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The QR-login example evaluates output from an external npm helper as shell code.

Mitigation: Review and correct the example before use. Prefer the personal-token route when available; otherwise verify and pin the helper, and import its values without eval.

Risk: Bearer-token requests can expose credentials and private student data if sent to an unintended host or saved in an unsafe location.

Mitigation: Restrict credential-bearing requests to the institution's HTTPS origin, set auto_mark_as_read=false, and use private output locations with explicit overwrite and cleanup rules.

## Reference(s):

- [Canvas API endpoint examples](references/canvas-endpoints.md)
- [canvas-parent-api on ClawHub](https://clawhub.ai/chrischall/skills/canvas-parent-api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use curl and jq with a per-institution Canvas base URL and bearer token.]

## Skill Version(s):

2.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
