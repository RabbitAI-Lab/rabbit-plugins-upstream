## Description:

Helps agents query AllTrails trails, reviews, photos, weather, and signed-in account activity using one-shot fpx commands through a browser tab without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other AllTrails users use this skill to retrieve trail information and, with a signed-in browser session, their saved lists, completed trails, and activity feed from a shell without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-mediated requests may expose personal AllTrails activity and captured request headers in shared logs or scripts.

Mitigation: Review account-scoped commands and avoid sharing logs or scripts containing captured headers or personal AllTrails data.

## Reference(s):

- [AllTrails endpoint examples](references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/alltrails-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only requests; account-specific results require a signed-in AllTrails browser tab.]

## Skill Version(s):

3.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
