## Description:

This skill helps agents answer Canvas LMS questions for a user's own student account or observed students, including courses, assignments, grades, inbox conversations, announcements, planner items, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect Canvas LMS educational records for a signed-in account or linked observees. It supports course, grade, assignment, calendar, conversation, announcement, discussion, planner, and file workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Canvas educational records and authentication material.

Mitigation: Use scoped token or OAuth-style access where available, avoid username/password authentication, and install only in environments where Canvas record access is acceptable.

Risk: The fetchproxy mode can reuse browser cookies from a signed-in Canvas session.

Mitigation: Disable fetchproxy with CANVAS_DISABLE_FETCHPROXY=1 when browser-cookie reuse is not desired.

Risk: The file download tool can write Canvas files to disk.

Mitigation: Download files only to an explicit, trusted destination directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent)
- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [canvas-parent-mcp source link from artifact](https://github.com/chrischall/canvas-parent-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown or plain text with JSON configuration and inline shell commands when setup is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize Canvas API data returned by MCP tools; compact view strips avatar URLs by default while preserving named link fields.]

## Skill Version(s):

1.5.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
