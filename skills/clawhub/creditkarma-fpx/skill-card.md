## Description:

Guides agents to retrieve Credit Karma transactions with fpx-captured browser session cookies and direct curl requests instead of running the Credit Karma MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other authorized Credit Karma users can use this skill to obtain transaction pages in scripts without installing the Credit Karma MCP server. It explains browser-session capture, token refresh, pagination, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Captured session cookies and access or refresh tokens can grant access to sensitive Credit Karma data.

Mitigation: Use only a trusted, dedicated session and machine; restrict extension site access and never paste tokens into chats or logs.

Risk: Shell commands and temporary response files can expose financial transaction data or credentials on shared systems.

Mitigation: Avoid shared systems, restrict file permissions, and remove temporary files after use.

## Reference(s):

- [Creditkarma FPX ClawHub release](https://clawhub.ai/chrischall/skills/creditkarma-fpx)
- [Credit Karma request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes transaction retrieval and pagination; live requests return financial transaction data.]

## Skill Version(s):

3.3.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
