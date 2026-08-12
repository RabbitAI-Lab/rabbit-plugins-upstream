## Description:

Guides an agent to query Canvas LMS from a shell with curl and bearer-token authentication for courses, grades, assignments, submissions, calendar items, planner data, announcements, conversations, discussions, and files for the current user or a linked observee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, shell users, and Canvas observers use this skill to retrieve Canvas LMS data with curl and bearer tokens when they need scriptable access without running the Canvas MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth QR-login setup can execute output from an unpinned helper through eval.

Mitigation: Use a pinned, trusted helper version or manually parse and export only the expected Canvas environment variables.

Risk: Canvas client secrets and long-lived refresh tokens may be exposed through shell history, logs, or shared terminal sessions.

Mitigation: Keep Canvas credentials out of logs and shell history, use short-lived shell sessions, and rotate credentials if exposure is suspected.

Risk: Downloaded Canvas files and API responses can contain student or course data.

Mitigation: Store downloaded Canvas data only in appropriate private directories and avoid shared paths unless access controls are confirmed.

## Reference(s):

- [Canvas API endpoints for curl](artifact/references/canvas-endpoints.md)
- [ClawHub skill release page](https://clawhub.ai/chrischall/skills/canvas-parent-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, curl API call patterns, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Canvas endpoint patterns, pagination guidance, token refresh notes, and safe handling reminders for Canvas credentials and downloaded files.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
