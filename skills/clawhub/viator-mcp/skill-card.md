## Description:

Search Viator tours, activities, attractions, availability, pricing, product details, destinations, and currency data through a read-only MCP connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, travel planners, and developers use this skill to search Viator tours, activities, attractions, product details, pricing, and availability from an agent workflow. It supports discovery and comparison, while booking details should be verified on Viator before purchase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Viator Partner API key in MCP configuration.

Mitigation: Install only after trusting the @chrischall/viator-mcp package, and keep VIATOR_API_KEY in local configuration or environment storage appropriate for secrets.

Risk: Travel product prices, availability, and booking terms can change after search results are returned.

Mitigation: Verify product details, pricing, availability, cancellation terms, and booking conditions on Viator before making any purchase.

Risk: Users may confuse search results and booking URLs with completed booking actions.

Mitigation: Treat this as a read-only Viator search helper; complete any booking directly through Viator using the returned product URL.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/viator-mcp)
- [npm package: @chrischall/viator-mcp](https://www.npmjs.com/package/@chrischall/viator-mcp)
- [Viator Partner Resources](https://partnerresources.viator.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and Viator search result data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only search and reference output; compact responses are described as the default artifact behavior.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
