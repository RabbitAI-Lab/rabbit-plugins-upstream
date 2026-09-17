## Description:

Read Remind (remind.com) classes, chats, messages, and notification settings from a shell by capturing a signed-in session once through the fpx browser bridge, then querying Remind's GraphQL API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to inspect Remind account, class, chat, message, and notification data from shell workflows without running a separate MCP server. It is read-oriented, with write-capable mutation examples documented only for deliberate account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to capture full Remind session cookies and a CSRF token, which function like account credentials.

Mitigation: Use a dedicated Remind session when possible, store the captured session file with restrictive permissions, treat it like a password, and remove it after use.

Risk: The bundled examples include write-capable GraphQL mutations that can change account settings or send real messages.

Mitigation: Avoid mutation examples unless an account owner explicitly intends to make the live change, and check account permissions before attempting writes.

Risk: Remind may return HTTP 200 responses that still contain authorization or validation errors.

Mitigation: Inspect the response body for GraphQL errors and refresh the captured session when unauthorized responses appear.

## Reference(s):

- [Remind GraphQL ready-to-run documents](artifact/references/graphql-queries.md)
- [Remind GraphQL endpoint](https://www.remind.com/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/remind-mcp)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, GraphQL, JSON, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes session-capture steps and ready-to-run query patterns; mutation examples require explicit user intent before use.]

## Skill Version(s):

0.4.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
