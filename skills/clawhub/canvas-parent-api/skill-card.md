## Description:

Query Canvas LMS for courses, grades, assignments, submissions, calendars, messages, and files using authenticated curl commands instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students, parents with linked observer access, and developers use this skill to retrieve authorized Canvas course information and files from a shell or script without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth setup runs a live package helper and evaluates its output while handling long-lived credentials.

Mitigation: Prefer a pinned, trusted helper; inspect its output and avoid evaluating live package output when possible.

Risk: Canvas tokens and retrieved student data could be exposed through shared shells, logs, or unauthorized queries.

Mitigation: Keep tokens out of shared shells and logs, unset them after use, and access or download only data you are authorized to view.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require an institution-specific Canvas URL and authorized bearer token.]

## Skill Version(s):

2.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
