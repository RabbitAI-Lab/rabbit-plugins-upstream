## Description:

Guides an agent to retrieve AllTrails trail and account data through a browser-connected command-line tool without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AllTrails users can search trails and retrieve trail details, reviews, photos, weather, saved lists, completed trails, and activity data through shell commands. Account-specific data requires an authorized signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paired browser extension can access AllTrails data visible to the signed-in account.

Mitigation: Pair only with a trusted extension and an account whose visible data you intend to access.

Risk: Captured headers or returned profile and activity data may be exposed through logs or shared terminals.

Mitigation: Keep headers and account data out of logs, shell history, shared terminals, and public scripts; verify the external CLI and extension before installation.

## Reference(s):

- [AllTrails endpoint examples](artifact/references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/alltrails-fpx)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, JSON data, Guidance]

**Output Format:** [Markdown instructions with shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only requests; account-specific results depend on the signed-in AllTrails session.]

## Skill Version(s):

3.1.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
