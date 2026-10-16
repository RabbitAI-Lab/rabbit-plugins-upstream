## Description:

Guides agents in querying AllTrails trail information and signed-in account data through a browser-connected shell CLI without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other AllTrails users use this skill to search trails, inspect details and reviews, and retrieve saved lists or activity from an account they are authorized to access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser extension and shell access to a signed-in AllTrails session can expose account data.

Mitigation: Install only if comfortable granting this access, and query only your own account or clearly authorized profiles.

Risk: Captured headers and saved-list, completed-trail, or activity responses may contain sensitive account information.

Mitigation: Do not store or share captured headers or returned account data; treat account activity as personal data.

## Reference(s):

- [AllTrails FPX release](https://clawhub.ai/chrischall/skills/alltrails-fpx)
- [AllTrails endpoint examples](references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown instructions and shell examples; queried data is JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only queries; signed-in account responses can include personal data.]

## Skill Version(s):

3.1.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
