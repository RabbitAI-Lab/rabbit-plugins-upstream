## Description:

Guides authorized Canvas LMS users in querying their own or linked students' courses, grades, assignments, and other school data with curl and a bearer token, without a running MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students, parents with linked observees, and developers use this guide to retrieve authorized Canvas LMS information from a shell or script when an MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas access and refresh tokens can be exposed through shell history, logs, or shared output.

Mitigation: Keep credentials out of history and logs, share only redacted output, and revoke tokens when finished.

Risk: Running an unpinned QR-login helper through shell eval can expose OAuth credentials or execute unexpected commands.

Mitigation: Pin or independently verify the helper before use, and avoid eval when handling its output.

Risk: Sending an Authorization header to an unverified file URL can disclose a Canvas token.

Mitigation: Validate the destination URL before using it with authenticated curl commands.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/canvas-parent-api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples return Canvas API data after authentication; results depend on the user's access permissions.]

## Skill Version(s):

2.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
