## Description:

Query Canvas LMS (Instructure) from a shell with curl and a bearer access token instead of running the canvas-parent-mcp server: courses, grades, assignments, submissions, calendar, planner, announcements, conversations, discussions, and files for yourself or a linked observee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and Canvas users use this skill to query Canvas LMS data with curl and bearer-token authentication when the MCP server is unavailable or unnecessary. It helps retrieve profiles, courses, grades, assignments, submissions, calendar items, announcements, conversations, discussions, and files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The OAuth setup handles Canvas credentials and includes a command that executes generated shell exports from an external helper.

Mitigation: Prefer a personal access token where allowed, manually inspect helper output before exporting variables, avoid storing Canvas secrets in persistent shell profiles or logs, and revoke exposed tokens.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes curl commands, environment-variable setup, jq projections, pagination guidance, and token-refresh guidance.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
