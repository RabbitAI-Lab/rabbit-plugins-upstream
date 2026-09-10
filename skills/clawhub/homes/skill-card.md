## Description:

Look up Homes.com real-estate listings, property details, price and tax history, market reports, saved homes, and photo galleries through the homes-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Homes.com property information through an MCP server, including searches, individual property records, history, photos, market reports, saved items, and local mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup asks users to run unpinned external code and install a separate browser extension.

Mitigation: Review homes-mcp and fetchproxy before installation, prefer pinned package versions or audited commits, and check extension permissions.

Risk: Saved homes and saved searches require a signed-in Homes.com browser session and may expose account-specific data to the agent session.

Mitigation: Use authenticated saved-item tools only when the user is comfortable sharing that account-specific data in the active agent session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [fetchproxy extension setup](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown with structured property data, links, and inline JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact responses strip media URLs by default for supported tools; full responses can include photos and floorplan URLs where the underlying MCP tool supports them.]

## Skill Version(s):

1.4.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
