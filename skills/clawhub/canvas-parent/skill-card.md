## Description:

Helps an agent answer Canvas LMS questions about a user's own student account or observed students, including courses, assignments, grades, conversations, announcements, planner items, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to configure and operate a Canvas LMS MCP server so an agent can retrieve account, course, grade, assignment, communication, planner, and file information from authorized Canvas accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can access Canvas account data and high-value session material such as cookies, tokens, OAuth credentials, or username/password credentials.

Mitigation: Use the narrowest credential method available, avoid username/password authentication where possible, and treat Canvas cookies, refresh tokens, and access tokens as secrets.

Risk: The file download tool can write Canvas files to disk.

Mitigation: Confirm the download URL and destination path before invoking downloads, and keep downloaded files inside the configured output directory.

Risk: Canvas data may include sensitive student, course, grade, submission, and conversation information.

Mitigation: Use the skill only with authorized Canvas accounts or observees and limit shared outputs to information the requester is permitted to see.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent)
- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [canvas-parent-mcp source link from skill artifact](https://github.com/chrischall/canvas-parent-mcp)
- [fetchproxy authentication helper](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and structured Canvas MCP tool responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Canvas responses may use compact or full views; file downloads write to the configured Canvas output directory.]

## Skill Version(s):

2.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
