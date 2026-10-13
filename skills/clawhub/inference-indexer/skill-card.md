## Description:

Helps agents compare model pricing, quality, and provider options before recommending an inference model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[desmartin01](https://clawhub.ai/user/desmartin01)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users compare model costs and capabilities, find suitable inference providers, and check price history or privacy-related availability before choosing a model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pricing queries and model selection may contact InferenceIndexer or external inference providers with task details.

Mitigation: Avoid sensitive task details unless the selected provider meets applicable privacy requirements.

Risk: Provider-stated zero-retention and EU availability claims may not be independently verified.

Mitigation: Check provider policies and the recommendation's freshness and caveats before relying on those claims.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/desmartin01/skills/inference-indexer)
- [InferenceIndexer MCP configuration](https://www.inferenceindexer.ai/.well-known/mcp-config.json)

## Skill Output:

**Output Type(s):** [Text, Configuration guidance]

**Output Format:** [Markdown with model recommendations, prices, and provider configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations should include pricing, rationale, freshness, and caveats.]

## Skill Version(s):

1.0.1 (source: ClawHub release; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
