## Description:

Access SignUpGenius sign-ups, groups, and RSVPs from a shell with curl by logging in with email and password to obtain session cookies and a JWT, then calling the v3 API and legacy dispatcher directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve SignUpGenius account, group, sign-up, and RSVP data from shell scripts without installing the MCP server. It also provides curl recipes for selected write actions, including adding group members and submitting RSVP responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Passwords, session cookies, JWTs, and refresh tokens could be exposed through shell history, logs, transcripts, or temporary files.

Mitigation: Use a password manager or secret store for credentials, avoid echoing tokens, restrict temp-file permissions, and delete cookie jars and captured headers when finished.

Risk: The skill can access SignUpGenius account data and public participant rosters that may include personal information.

Mitigation: Use it only with accounts and sign-ups the user is authorized to access, and avoid collecting roster details unless needed for the task.

Risk: Some endpoint recipes perform write actions, such as adding group members or submitting RSVP responses.

Mitigation: Require explicit user confirmation before running write-capable curl commands and verify target IDs, names, emails, and RSVP values before submission.

## Reference(s):

- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes curl command patterns, environment variable setup, jq examples, endpoint notes, and session-expiry handling guidance.]

## Skill Version(s):

2.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
