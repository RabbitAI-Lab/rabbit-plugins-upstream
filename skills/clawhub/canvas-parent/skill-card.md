## Description:

Provides Canvas LMS access for an agent to check a user's or observed student's courses, grades, assignments, announcements, conversations, planner items, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Canvas users use this skill to connect an agent to Canvas LMS so it can answer questions about coursework, grades, messages, announcements, planner items, and downloadable course files for the signed-in user or linked observees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recommended setup can give the MCP access to a Canvas account session and linked student or observer records.

Mitigation: Install only when that account and data access is intended; prefer scoped token or OAuth configuration when available.

Risk: Fetchproxy-based authentication can read Canvas session cookies from a signed-in browser tab.

Mitigation: Disable fetchproxy with CANVAS_DISABLE_FETCHPROXY=1 when cookie-based access is not acceptable.

Risk: The file download tool can write course files to a requested destination path.

Mitigation: Use destination paths inside a directory you control and review file download requests before execution.

## Reference(s):

- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide MCP setup and tool use; configured tools may retrieve Canvas LMS records and download course files.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
