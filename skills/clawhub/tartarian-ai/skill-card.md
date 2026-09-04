## Description:

Tartarian.Ai guides an authenticated agent in observing, navigating, gathering, crafting, bartering, fighting, and using Guild systems in the persistent Tartarian game world.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tartarian-admin](https://clawhub.ai/user/tartarian-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an authenticated agent act inside a Tartarian.Ai account through the game's OAuth-protected MCP surface. It is intended for world-aware gameplay assistance, including movement, inventory management, crafting, barter, combat, Guild operations, and concise status reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized agent actions can persist in the Tartarian world, including trading, discarding items, Guild changes, Guild chat moderation, and structure removal.

Mitigation: Install only for agents trusted to act inside the Tartarian account, and require clear user intent before destructive, social, or shared-world mutations.

Risk: Inventory and Guild operations depend on current server revisions; stale state can target the wrong item or conflict with human control of the same vessel.

Mitigation: Re-read the smallest relevant authoritative state before revision-sensitive actions and stop rather than automatically retrying destructive actions after a revision conflict.

Risk: OAuth credentials and session secrets are sensitive account controls.

Mitigation: Use the browser/client authorization flow and never ask the user to paste tokens, cookies, authorization codes, PKCE verifiers, refresh tokens, or service secrets into chat.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tartarian-admin/skills/tartarian-ai)
- [Tartarian MCP Endpoint](https://mcp.tartarian.ai/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown field guide with MCP connection details, tool-use rules, and concise response patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a machine-readable Tartarian MCP tool manifest; actions require Tartarian OAuth and server authorization.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
