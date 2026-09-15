## Description:

Access SignUpGenius sign-ups, groups, and RSVPs from a shell with curl by logging in with email/password session cookies and calling the v3 API or legacy dispatcher directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve or update SignUpGenius account, group, sign-up, and RSVP data from shell scripts without installing an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles SignUpGenius account credentials, JWTs, and session cookies in shell workflows.

Mitigation: Keep credentials and tokens out of shell history and logs, use private temporary files with restrictive permissions, and delete cookie jars and response files after use.

Risk: The skill can expose participant names, comments, internal IDs, and other SignUpGenius data.

Mitigation: Use only with accounts and sign-ups the user is authorized to access, and avoid participant-name enumeration unless there is a clear user-approved need.

Risk: Some documented endpoints perform write actions, including adding group members and submitting RSVPs.

Mitigation: Confirm user intent before running write requests and review request bodies before submission.

## Reference(s):

- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes curl and jq examples for authenticated SignUpGenius session workflows.]

## Skill Version(s):

1.8.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
