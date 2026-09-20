## Description:

Guides an agent to read a user's SimplePractice Client Portal from a shell with curl against the portal JSON:API, including passwordless sign-in and optional fpx cookie capture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when they want scripted, read-only access to their own SimplePractice portal data without running a SimplePractice MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose protected health information, billing data, documents, and live portal session cookies while helping read a SimplePractice client portal.

Mitigation: Use it only for the user's own portal data, keep cookie jars chmod 600 and out of git, avoid shared machines and logs, and treat API responses as sensitive health records.

Risk: The optional fpx path captures an authenticated browser session cookie.

Mitigation: Use fpx only when the user understands and approves browser-session access; prefer passwordless sign-in when a fresh session is acceptable.

## Reference(s):

- [SimplePractice Client Portal request reference](artifact/references/requests.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal workflow guidance; handling live cookies, tokens, billing data, documents, and other health-record data requires user-controlled credential storage.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
