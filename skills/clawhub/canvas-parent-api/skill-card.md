## Description:

Query Canvas LMS from a shell with curl and a bearer access token for courses, grades, assignments, submissions, calendar, planner, announcements, conversations, discussions, and files for yourself or a linked observee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, administrators, parents, and students use this skill to have an agent produce direct Canvas LMS curl commands and setup guidance when they need Canvas data without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to handle long-lived Canvas credentials in shell environments.

Mitigation: Use the minimum needed Canvas token access, keep refresh tokens out of long-lived shell environments, and revoke Canvas tokens when no longer needed.

Risk: The setup flow shows eval of output from an external npx helper.

Mitigation: Inspect helper output before exporting values and avoid eval on helper output unless the helper source and output are trusted.

Risk: The skill can query educational records such as grades, submissions, conversations, and files through Canvas API calls.

Mitigation: Run commands only against the intended Canvas tenant and account, avoid oversharing command output, and store downloaded files only in approved locations.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Canvas tenant base URL and bearer-token environment variables; Canvas API responses are JSON.]

## Skill Version(s):

1.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
