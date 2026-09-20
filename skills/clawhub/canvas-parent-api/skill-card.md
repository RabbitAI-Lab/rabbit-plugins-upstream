## Description:

Query Canvas LMS from a shell with curl and a bearer access token for courses, grades, assignments, submissions, calendar, planner, announcements, conversations, discussions, and files for yourself or a linked observee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, Canvas users, and observers use this skill to ask an agent for curl-based Canvas API setup and endpoint guidance without running the Canvas MCP server. It is suited for querying authorized Canvas account or observee data in scripts and shell workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas credentials and responses can expose sensitive account and student records.

Mitigation: Protect tokens, avoid logging or sharing raw Canvas responses, and access only account or observee data you are authorized to view.

Risk: The documented OAuth QR setup uses an unpinned npm helper through eval, which can execute unexpected shell content.

Mitigation: Verify and pin the helper package before use, or manually inspect the generated environment exports before applying them.

Risk: Bearer tokens grant direct Canvas API access until expiry or revocation.

Mitigation: Store tokens only in trusted shell environments, rotate or revoke them when no longer needed, and refresh short-lived OAuth access tokens as documented.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Canvas base URL and bearer token; Canvas API responses may require pagination handling and XSSI prefix stripping.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
