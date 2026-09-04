## Description:

Search Viator tours, activities and experiences via MCP for destinations, products, pricing, availability, attractions, and supplier-currency conversion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure and operate a read-only Viator MCP connector for travel-search workflows, including tour discovery, product lookup, availability checks, attraction browsing, and exchange-rate lookup. It requires a Viator Partner API key and does not support booking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel-search queries and API requests are sent through a third-party npm MCP server to Viator.

Mitigation: Confirm the data-sharing posture is acceptable before installation and use the connector only for appropriate travel-search queries.

Risk: The skill requires a Viator API key.

Mitigation: Store the key only in MCP environment configuration and avoid placing credentials in prompts, source files, or shared logs.

Risk: Unpinned npx installs can change over time.

Mitigation: Pin the npm package version when reproducible installs are required.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/viator-mcp)
- [npm package @chrischall/viator-mcp](https://www.npmjs.com/package/@chrischall/viator-mcp)
- [Viator Partner Resources](https://partnerresources.viator.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP setup snippets, tool-selection guidance, and concise summaries of Viator search results returned by the configured MCP server.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
