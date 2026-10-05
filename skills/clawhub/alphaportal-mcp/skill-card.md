## Description:

Guides authorized users in accessing AlphaPortal student transportation, stops, live bus locations, and notifications through shell commands without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized AlphaPortal users and developers use this skill to retrieve school-bus transportation information or prepare direct API requests from a shell when the MCP server is unavailable or unwanted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A captured refresh token could expose sensitive student and bus-location data if shared or logged.

Mitigation: Use only with authorized accounts; protect the refresh token like a password and avoid putting it in logs or shared shell history.

Risk: Direct write commands can permanently change transportation settings without confirmation.

Mitigation: Prefer the MCP flow for writes, or manually review each request and its student identifier before execution.

## Reference(s):

- [AlphaPortal MCP release](https://clawhub.ai/chrischall/skills/alphaportal-mcp)
- [AlphaPortal endpoint reference](references/endpoints.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read sensitive student and location data or make account changes.]

## Skill Version(s):

1.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
