## Description:

Search Viator tours, activities and experiences via MCP for destination discovery, product details, pricing, availability, attractions, and supplier-currency conversion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and operate a read-only Viator MCP connector for travel activity search, product lookup, availability checks, attraction browsing, and exchange-rate retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Viator API key could be exposed if MCP configuration with a real credential is committed or shared.

Mitigation: Store VIATOR_API_KEY as a secret or local environment value, and avoid committing MCP config files that contain a real key.

Risk: Broad travel requests may produce Viator-focused results and booking URLs rather than neutral coverage of all available providers.

Mitigation: Treat results as Viator catalog output, review product details before recommending an option, and preserve Viator booking URLs when affiliate attribution is required.

Risk: Authentication, endpoint rate limits, or empty catalog responses can make results appear incomplete.

Mitigation: Use the healthcheck tool when calls fail or return unexpectedly empty data, and respect documented retry and cache behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/viator-mcp)
- [npm package](https://www.npmjs.com/package/@chrischall/viator-mcp)
- [Viator Partner Resources](https://partnerresources.viator.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command examples; MCP tool responses return travel-search data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only connector output; compact view is the default for read tools that support view selection.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
