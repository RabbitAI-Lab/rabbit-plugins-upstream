## Description:

Discover curated SaaS and AI-agent tools via the Tulimoa directory. Search by topic, category, pricing, MCP support, or EU hosting, pull full detail on any tool, and submit or edit your own listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[florianbaraz](https://clawhub.ai/user/florianbaraz)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and product evaluators use this skill to find, compare, and inspect SaaS or AI-agent tools in the Tulimoa directory. Authenticated Tulimoa users can submit or edit their own public directory listings through OAuth-backed write tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Discovery queries are sent to Tulimoa's remote MCP service.

Mitigation: Install and use the skill only when sharing SaaS or AI-tool discovery queries with Tulimoa is acceptable.

Risk: OAuth-backed write actions can create or modify public directory listings after admin review.

Mitigation: Review listing submissions and edits before authorizing write actions.

## Reference(s):

- [Tulimoa homepage](https://tulimoa.com)
- [Tulimoa MCP endpoint](https://mcp.tulimoa.com/mcp)
- [ClawHub skill page](https://clawhub.ai/florianbaraz/skills/tulimoa)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown or structured tool results from the Tulimoa MCP server]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools return structuredContent with declared output schemas; listing submissions and edits require Tulimoa OAuth login.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
