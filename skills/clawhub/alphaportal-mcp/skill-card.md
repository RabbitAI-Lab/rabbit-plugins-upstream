## Description:

Provides shell commands to access AlphaPortal school transportation data and manage notification settings through its API without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized parents, guardians, and developers can retrieve student bus stops, live vehicle locations, and arrival notifications using shell commands when the MCP server is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extracting a reusable browser refresh token can expose sensitive student transportation data if the token is disclosed.

Mitigation: Use only with authorized accounts; prefer the official MCP or a sanctioned API flow, and keep tokens out of shared shells, logs, scripts, screenshots, and agent memory.

Risk: Direct API writes change transportation records without a built-in preview or confirmation.

Mitigation: Avoid writes unless necessary; manually verify the exact student, endpoint, and values immediately before sending each request.

## Reference(s):

- [AlphaPortal endpoint reference](references/endpoints.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [AlphaPortal MCP release](https://clawhub.ai/chrischall/skills/alphaportal-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return live account data or change notification and transportation settings when executed.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
