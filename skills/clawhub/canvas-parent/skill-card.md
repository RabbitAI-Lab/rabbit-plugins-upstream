## Description:

Helps users check courses, grades, assignments, messages, and files in their own or an observed student's Canvas account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students and parents or other observers use this skill to review Canvas coursework, grades, deadlines, announcements, conversations, and course files for accounts they can access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas tokens, passwords, or browser session cookies may expose private account records.

Mitigation: Use the least-privilege authentication available, protect credentials like passwords, and disable the browser-cookie fallback if live session cookies should not be used.

Risk: Downloaded course files and Canvas responses may contain confidential student information.

Mitigation: Limit access to authorized accounts and handle downloaded files and responses as confidential student data.

## Reference(s):

- [Canvas Parent on ClawHub](https://clawhub.ai/chrischall/skills/canvas-parent)
- [Canvas Parent MCP package](https://www.npmjs.com/package/canvas-parent-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include confidential Canvas student records and links to course files.]

## Skill Version(s):

2.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
