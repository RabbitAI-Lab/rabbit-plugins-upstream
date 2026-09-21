## Description:

Provides Canvas LMS access for questions about courses, assignments, grades, inbox conversations, announcements, planner items, and course files for a user's own account or observed students.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to connect to Canvas LMS and retrieve course, grade, assignment, calendar, inbox, announcement, and file information for a user's own account or linked observees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can access Canvas data equivalent to the signed-in Canvas session, including grades, messages, files, and linked student records.

Mitigation: Install only when this access is acceptable; prefer OAuth or a Canvas token when available, disable fetchproxy with CANVAS_DISABLE_FETCHPROXY=1 if browser-cookie authentication is not desired, and review the external npm package and fetchproxy extension before enabling them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent)
- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [canvas-parent-mcp repository](https://github.com/chrischall/canvas-parent-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, configuration, shell commands, files]

**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Canvas LMS records and downloaded course files through MCP tools.]

## Skill Version(s):

2.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
