## Description:

Current geo-tagged world news for agents, split into viewpoints with a count of the media, social and on-the-ground posts behind each. Use when a user asks what people are saying about a country, conflict or public story, wants the distinct positions on a story, or wants an early signal ahead of the wider press. Pay per call with an API key (free 7-day trial) or with x402 in USDC on Base, Polygon or Arbitrum.

This skill is ready for commercial/non-commercial use.

## Publisher:

[quorumz](https://clawhub.ai/user/quorumz)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to retrieve current news for a country, conflict, or public story and see the distinct viewpoints with supporting source counts. It is intended for timely, geo-tagged news signals rather than general web searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the external Quorumz API may involve sharing an API credential and can incur per-call charges after the free allowance or through x402.

Mitigation: Review the service terms and route pricing, start with the free sample, and provide an API key or payment wallet only when authorized.

## Reference(s):

- [Quorumz agent API documentation](https://sense.quorumz.com/agents/docs)
- [Quorumz OpenAPI specification](https://api.quorumz.com/openapi.json)
- [x402 service discovery](https://api.quorumz.com/.well-known/x402)

## Skill Output:

**Output Type(s):** [Text, JSON, Analysis]

**Output Format:** [Structured news and viewpoint data in JSON, suitable for concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Country and stream filters; cursor-based pagination; route costs vary.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
