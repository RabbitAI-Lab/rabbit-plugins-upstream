## Description:

This skill helps agents answer Canvas LMS questions by using a Canvas parent or observer MCP server to read courses, grades, assignments, announcements, planner items, conversations, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to configure and operate a Canvas LMS MCP helper for student, parent, or observer workflows, including grades, assignments, announcements, inbox messages, planner items, and course files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Canvas education records, inbox content, observee data, course files, and Canvas session or credential material.

Mitigation: Install and use it only when the external npm package is trusted, and prefer the narrowest available authentication method.

Risk: Using browser-session cookie reuse or raw username and password authentication may expose credentials or active Canvas sessions.

Mitigation: Avoid raw username and password authentication when possible, and disable fetchproxy when browser cookie reuse is not acceptable.

Risk: Course file downloads can write Canvas files to user-selected local paths.

Mitigation: Choose download destinations deliberately and review downloaded files before sharing or executing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent)
- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [canvas-parent-mcp source](https://github.com/chrischall/canvas-parent-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown with JSON configuration snippets, shell commands, and Canvas LMS tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce compact or full Canvas payloads and may download course files when requested.]

## Skill Version(s):

2.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
