## Description:

This skill should be used when the user asks about Canvas LMS data - their own student account or any observed student.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Canvas LMS users and parent or observer accounts use this skill to let an agent retrieve courses, grades, assignments, announcements, planner items, conversations, and course files from Canvas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser session cookies may be reused when fetchproxy authentication is enabled.

Mitigation: Install only on a trusted machine, prefer token or OAuth authentication when available, and disable fetchproxy if browser cookie reuse is not acceptable.

Risk: Canvas access may include records for the signed-in user and linked observee or student accounts.

Mitigation: Confirm the Canvas account scope and linked observees before use, especially when handling grades, inbox messages, submissions, or student records.

Risk: Course file downloads may write files to local storage.

Mitigation: Restrict downloads to a directory the user controls and review downloaded files before opening or sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent)
- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to query Canvas LMS tools and download course files when configured.]

## Skill Version(s):

1.3.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
