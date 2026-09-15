## Description:

This skill should be used when the user asks about Canvas LMS data for their own student account or an observed student, including courses, assignments, grades, conversations, announcements, planner items, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students, parents, observers, and developers use this skill to connect an agent to Canvas LMS through the canvas-parent MCP server and retrieve coursework, grades, inbox messages, announcements, planner items, and course files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Canvas account data and student educational records through browser cookies, access tokens, OAuth credentials, or username and password.

Mitigation: Install only after trusting the package, publisher, and fetchproxy extension; prefer a pinned reviewed version and narrowly scoped token or OAuth flow.

Risk: The npx setup runs the npm package without a pinned version.

Mitigation: Pin and review a specific package version, or install from a reviewed local source checkout before use.

Risk: The file download tool can write course files to local paths.

Mitigation: Restrict downloads to a dedicated folder and review destination paths before invoking file downloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/canvas-parent)
- [npm package: canvas-parent-mcp](https://www.npmjs.com/package/canvas-parent-mcp)
- [Source repository: canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides MCP configuration and use of Canvas tools that return Canvas LMS profile, course, grade, assignment, communication, planner, and file data.]

## Skill Version(s):

1.5.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
