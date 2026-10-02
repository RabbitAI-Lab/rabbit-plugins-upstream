## Description:

Guides authorized users to access AlphaPortal student transportation, bus location, and notification data with shell commands instead of running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized AlphaPortal account holders use this skill to retrieve student bus routes, live vehicle locations, and notifications through direct API calls without installing the MCP server. It also documents account-changing requests that require extra care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extracting a reusable browser refresh token exposes sensitive account access and student transportation data if the token or command output is disclosed.

Mitigation: Use only an account you are authorized to access; keep tokens and outputs out of shared machines and logs, and store them securely.

Risk: Direct write requests can change real transportation records without a preview or confirmation step.

Mitigation: Avoid write endpoints unless necessary, and independently review the exact student ID and request body before sending.

## Reference(s):

- [AlphaPortal endpoint reference](references/endpoints.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/alphaportal-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Example commands can return sensitive student transportation records and live bus locations.]

## Skill Version(s):

1.1.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
