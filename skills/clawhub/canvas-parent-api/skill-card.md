## Description:

Provides Canvas LMS curl patterns for authenticated access to courses, grades, assignments, submissions, calendar, planner, announcements, conversations, discussions, and files for the current user or a linked observee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, students, and observers use this skill to query Canvas LMS data from a shell without running the canvas-parent-mcp server. It helps agents produce authenticated curl commands and endpoint guidance for Canvas coursework, grades, calendars, messages, discussions, and files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas credentials and sensitive school data may be exposed through shared shells, logs, or unsafe command handling.

Mitigation: Keep tokens out of shared terminals and logs, unset them after use, and install only where shell-based credential handling is acceptable.

Risk: The OAuth setup uses an unpinned npx helper with eval on command output while handling Canvas credentials.

Mitigation: Prefer a pinned, trusted helper or a manually reviewed OAuth flow before exporting credentials into the shell.

Risk: File download commands may retrieve private Canvas files.

Mitigation: Download only file URLs returned by the user's own Canvas instance and review destination handling before scripting downloads.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent-api)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Canvas base URL and token environment setup, curl request patterns, endpoint paths, pagination guidance, and response-shaping examples.]

## Skill Version(s):

1.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
