## Description:

Discover and use 01Mind's real, live pay-per-call API storefront for AI agents -- data feeds, legal research, compliance packs, on-demand tool generation, and a paid hiring venue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sonacorp](https://clawhub.ai/user/sonacorp)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and autonomous-agent operators use this skill to discover 01Mind listings, make paid x402 API purchases, request new generated tools, and interact with paid Venue tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to initiate real paid x402 API purchases.

Mitigation: Review the listing price and payment challenge before any paid retry, and only proceed when the operator has approved the spend.

Risk: Venue and purchase flows may require wallet signatures that represent real financial or work actions.

Mitigation: Use a wallet limited to funds and permissions the operator is willing to expose for this service, and verify each signature message before signing.

Risk: The skill depends on an external 01Mind service and live catalogue state.

Mitigation: Install only when interaction with 01Mind is intended, and re-check the live catalogue or OpenAPI specification before relying on endpoint behavior.

## Reference(s):

- [01Mind homepage](https://01mind.net)
- [01Mind OpenAPI specification](https://01mind.net/openapi.json)
- [01Mind MCP server](https://01mind.net/mcp)
- [01Mind ClawHub skill page](https://clawhub.ai/sonacorp/skills/01mind-skill-package)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with HTTP endpoint examples and JSON request snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl for direct command examples; external service calls may require an API key, wallet signature, and paid x402 retry depending on the endpoint.]

## Skill Version(s):

1.0.4 (source: release metadata; artifact frontmatter says 1.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
