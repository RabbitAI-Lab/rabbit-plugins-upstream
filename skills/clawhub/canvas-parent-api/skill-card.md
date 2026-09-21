## Description:

Query Canvas LMS from a shell with curl and a bearer access token instead of running the canvas-parent-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, students, parents, and automation agents use this skill to retrieve Canvas LMS profile, course, assignment, grade, calendar, announcement, conversation, discussion, and file data from institution-specific Canvas APIs with curl.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to handle Canvas access tokens, refresh tokens, client secrets, and institution-specific API hosts in shell environments.

Mitigation: Keep secrets out of shared shells, logs, and broad environment variables where possible; rotate or revoke Canvas tokens if exposure is suspected.

Risk: The OAuth QR-login path uses an unpinned npm helper to exchange credentials.

Mitigation: Prefer pinned and verified tooling for QR-login flows, and review helper provenance before running it with Canvas credentials.

## Reference(s):

- [Canvas endpoint reference](artifact/references/canvas-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent-api)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with curl and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Canvas base URL and bearer token supplied by the user.]

## Skill Version(s):

2.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
