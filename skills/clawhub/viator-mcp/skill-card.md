## Description:

Searches Viator tours, activities, attractions, availability, pricing, and supplier-currency exchange rates through a read-only MCP connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure and use a Viator MCP server for read-only travel discovery, including tour search, product details, availability, pricing, attractions, destinations, and exchange rates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill registers and uses a third-party Viator MCP connector that sends travel search queries to Viator.

Mitigation: Install only when that connector is intended for the agent, and verify the external @chrischall/viator-mcp package or source before relying on it.

Risk: The connector requires a VIATOR_API_KEY for Viator Partner API access.

Mitigation: Keep VIATOR_API_KEY out of committed project files and provide it through the MCP server environment.

Risk: Search results, prices, availability, and booking links come from an external travel API and may change.

Mitigation: Treat returned travel information as current external API data and use Viator product URLs for booking and affiliate attribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/viator-mcp)
- [npm package @chrischall/viator-mcp](https://www.npmjs.com/package/@chrischall/viator-mcp)
- [Viator Partner Resources](https://partnerresources.viator.com/)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on read-only MCP tool use and handling external Viator API responses.]

## Skill Version(s):

2.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
