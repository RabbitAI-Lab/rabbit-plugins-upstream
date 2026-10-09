## Description:

Guides agents to query AllTrails trail and account data through a signed-in browser tab using fpx, without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find trails, reviews, photos, and weather, or to retrieve authorized saved lists, completed trails, and activity from AllTrails without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed-in browser access exposes private account activity, saved lists, completed trails, profile IDs, and captured headers.

Mitigation: Install only if comfortable granting fpx and ContextMint Bridge access to the signed-in tab; keep account data and captured headers out of logs, screenshots, public issues, and untrusted scripts.

Risk: Requests to another person's account or profile could exceed the user's authorization.

Mitigation: Use documented endpoints only for accounts and profiles you are authorized to access.

## Reference(s):

- [AllTrails FPX release](https://clawhub.ai/chrischall/skills/alltrails-fpx)
- [AllTrails endpoint reference](artifact/references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON data]

**Output Format:** [Markdown instructions and shell commands; AllTrails responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only requests; account data requires an authorized signed-in tab; route geometry is returned raw, not as GPX.]

## Skill Version(s):

3.1.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
