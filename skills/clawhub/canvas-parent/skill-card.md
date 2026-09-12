## Description:

This skill helps agents answer questions about Canvas LMS courses, grades, assignments, conversations, announcements, planner items, and files for a signed-in student or linked observer account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students, parents, observers, and developers use this skill to connect an agent to Canvas LMS through the canvas-parent-mcp server and retrieve school records such as courses, grades, assignments, announcements, inbox conversations, planner items, and course files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended npx setup installs and runs an external MCP package without a pinned reviewed version.

Mitigation: Pin and review the canvas-parent-mcp package version before deployment, and update only through an intentional review process.

Risk: The fetchproxy authentication path gives the local MCP process access to Canvas browser session cookies for sensitive school records.

Mitigation: Use the least-privileged Canvas authentication method available, restrict local MCP access to trusted users, and treat browser session access as equivalent to signed-in Canvas account access.

Risk: Canvas tokens, OAuth secrets, refresh tokens, usernames, passwords, or session-derived credentials could be exposed if stored in shared project files.

Mitigation: Keep Canvas credentials in user-local secret storage or private environment configuration, and avoid committing them to project repositories.

## Reference(s):

- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [canvas-parent-mcp source repository](https://github.com/chrischall/canvas-parent-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include MCP setup, Canvas tool usage, and interpretation of Canvas API responses.]

## Skill Version(s):

1.5.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
