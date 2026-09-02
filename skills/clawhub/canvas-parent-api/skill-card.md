## Description:

Query Canvas LMS (Instructure) from a shell with curl and a bearer access token instead of running the canvas-parent-mcp server - courses, grades, assignments, submissions, calendar, planner, announcements, conversations, discussions, and files for yourself or a linked observee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Canvas LMS users use this skill to have an agent draft shell-based Canvas API queries for courses, grades, assignments, submissions, planner items, announcements, conversations, discussions, and files without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas access tokens, OAuth refresh tokens, and client secrets can expose Canvas data if they are left in shell history, logs, or broadly inherited environments.

Mitigation: Use the least access your institution allows and store secrets in a protected secret store or tightly permissioned file.

Risk: The setup flow shows eval'ing helper output into the shell, which can execute unexpected output if the command stream is not trusted.

Mitigation: Inspect helper output before exporting variables and avoid eval in automated or untrusted environments.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, curl, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes per-institution Canvas base URL, bearer-token setup, pagination guidance, and endpoint-specific query examples.]

## Skill Version(s):

1.5.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
