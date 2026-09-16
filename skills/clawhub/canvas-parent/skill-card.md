## Description:

This skill helps agents use Canvas LMS data for a user's own student account or an observed student, including courses, grades, assignments, announcements, planner items, conversations, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to connect an agent to Canvas LMS through an MCP server so it can read course, grade, assignment, planner, announcement, conversation, observee, and file information within the user's authorized Canvas scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead users to run unpinned third-party package code.

Mitigation: Pin and audit the npm package version or source commit before installation and review the package before enabling it in an agent environment.

Risk: Canvas credentials, browser-session cookies, or OAuth material may grant broad access to student and course data.

Mitigation: Prefer scoped OAuth when available, keep secrets out of shared project `.mcp.json` files, and disable fetchproxy unless browser-session reuse is intentional.

Risk: The file download tool can write Canvas files to disk.

Mitigation: Allow downloads only to a user-controlled directory and review file paths before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent)
- [npm package: canvas-parent-mcp](https://www.npmjs.com/package/canvas-parent-mcp)
- [Source repository: canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP configuration and Canvas tool usage; Canvas tool responses can include user, course, grade, assignment, conversation, planner, and file metadata.]

## Skill Version(s):

1.5.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
