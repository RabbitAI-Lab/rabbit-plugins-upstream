## Description:

Search Viator tours, activities, attractions, availability, pricing, and destination data through an MCP server using a Viator Partner API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find Viator tours, excursions, attraction information, availability, pricing, destination data, and supplier-currency exchange rates. It supports search and retrieval workflows only; booking is handled through returned Viator product URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an external MCP package in the user's agent environment.

Mitigation: Install a pinned reviewed package version or commit before use.

Risk: A Viator Partner API key is required for normal operation.

Mitigation: Avoid placing real keys in shared project configuration and keep local config files out of source control.

Risk: The MCP server only needs access for Viator search and retrieval workflows.

Mitigation: Run the server with only the access needed for Viator lookups.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/viator-mcp)
- [npm package @chrischall/viator-mcp](https://www.npmjs.com/package/@chrischall/viator-mcp)
- [GitHub repository listed in the skill artifact](https://github.com/chrischall/viator-mcp)
- [Viator Partner Resources](https://partnerresources.viator.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and MCP tool result summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Viator lookups; compact responses are the default for tool results.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
