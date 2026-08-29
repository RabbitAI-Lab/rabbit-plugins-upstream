## Description:

This skill helps agents answer requests about Canvas LMS courses, grades, assignments, announcements, conversations, planner items, and course files for a user's own or observed-student account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students, parents, observers, and education-support agents use this skill to retrieve Canvas LMS account, coursework, grade, communication, planner, and course-file information through a Canvas MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Canvas LMS records, including grades, coursework, conversations, and observed-student information.

Mitigation: Install only for trusted Canvas accounts and use scoped token or OAuth credentials when available.

Risk: Browser-session reuse through fetchproxy can expose active Canvas authentication if enabled unintentionally.

Mitigation: Disable fetchproxy with CANVAS_DISABLE_FETCHPROXY=1 when browser-session reuse is not desired, and treat cookies and refresh tokens like passwords.

Risk: Course file downloads may save student or course material to unintended local paths.

Mitigation: Choose download destinations deliberately and review destination paths before downloading files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent)
- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [canvas-parent-mcp source](https://github.com/chrischall/canvas-parent-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Canvas MCP setup guidance and Canvas account data summaries when an authorized server is available.]

## Skill Version(s):

1.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
