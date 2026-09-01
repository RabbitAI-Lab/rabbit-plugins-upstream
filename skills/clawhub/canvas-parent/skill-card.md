## Description:

This skill helps an agent answer questions about Canvas LMS courses, assignments, grades, conversations, announcements, planner items, and files for the user or observed students.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, observers, students, and education-support agents use this skill to inspect Canvas LMS account data, including courses, grades, missing work, announcements, inbox conversations, planner items, and downloadable course files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Canvas LMS accounts, linked student records, grades, messages, and other education data.

Mitigation: Install it only for agents that should access that Canvas account, and review the account scope before use.

Risk: Authentication may rely on Canvas credentials or browser session cookies.

Mitigation: Prefer the least-privileged authentication method available, avoid storing raw passwords, and disable fetchproxy when browser cookie access is not intended.

Risk: The skill can download Canvas files to the local filesystem.

Mitigation: Use a controlled download directory and review downloaded files before opening or sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent)
- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [canvas-parent-mcp source repository](https://github.com/chrischall/canvas-parent-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May also guide agents toward Canvas MCP tool calls and local file downloads when configured by the user.]

## Skill Version(s):

1.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
