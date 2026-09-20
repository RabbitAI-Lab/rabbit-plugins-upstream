## Description:

This skill helps an agent answer questions about Canvas LMS courses, grades, assignments, announcements, planner items, conversations, and course files for a user's own account or an observed student.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students, parents, observers, and their agents use this skill to inspect Canvas LMS account data, including courses, grades, assignments, missing work, announcements, inbox conversations, planner items, and files. It is most useful when an agent needs to summarize Canvas status or retrieve course materials through the configured Canvas MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local MCP process can access sensitive Canvas account data through tokens, credentials, OAuth refresh tokens, or browser session cookies.

Mitigation: Use the narrowest supported authentication method, avoid storing passwords in configuration, and install only in environments where this account access is acceptable.

Risk: The recommended fetchproxy mode relies on cookies from a signed-in browser tab.

Mitigation: Keep the browser session limited to the intended Canvas instance and disable the fetchproxy fallback when another credential method is preferred.

Risk: The skill can download Canvas course files to local paths.

Mitigation: Use explicit destination paths that the user controls and review downloaded files before opening or sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent)
- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command snippets; MCP tool responses may include compact or full Canvas payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return Canvas LMS records and file download handles; compact mode strips avatar media fields while preserving link fields.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
