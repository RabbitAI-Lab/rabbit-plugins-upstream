## Description:

Query Canvas LMS from a shell with curl and a bearer access token for courses, grades, assignments, submissions, calendar, planner, announcements, conversations, discussions, and files for yourself or a linked observee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable Canvas users use this skill to query Canvas LMS data directly from a shell when they need courses, grades, assignments, submissions, messages, discussions, or files without running the Canvas MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The QR-login setup command evaluates unpinned remote package output while handling Canvas OAuth credentials.

Mitigation: Avoid running the eval npx command as written; pin and verify the helper and parse structured output before exporting environment variables.

Risk: Canvas access tokens, refresh tokens, grades, messages, submissions, and files are private data.

Mitigation: Validate the Canvas base URL before sending tokens, keep credentials out of logs and shell history, and limit command output to the data needed for the task.

## Reference(s):

- [Canvas API endpoint reference](artifact/references/canvas-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use Canvas bearer tokens and institution-specific Canvas base URLs.]

## Skill Version(s):

1.5.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
