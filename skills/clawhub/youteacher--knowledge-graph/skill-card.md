## Description:

Helps agents store sourced entities and relationships, query related graph data, and produce traceable summaries through the AI Skills platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can build a sourced knowledge graph, explore relationships around an entity, and obtain summaries with links back to user-provided sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Entities, relationships, and source URLs are stored on the hosted AI Skills service.

Mitigation: Use only with user-authorized data; do not store secrets or sensitive personal data in graph fields.

Risk: A shared platform API key can grant access across enabled products.

Mitigation: Prefer the product-specific KNOWLEDGE_GRAPH_API_KEY for tighter separation and keep all keys out of graph fields and responses.

Risk: Attached sources may be mistaken for independently verified evidence.

Mitigation: Identify sources as user-provided and do not describe their contents as verified by the platform.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/youteacher/skills/knowledge-graph)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key and setup guide](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/API-KEY.md)
- [HTTP requests and retries](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/HTTP-REQUESTS.md)
- [Graph operations and results](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/OPERATIONS.md)
- [Safety and source interpretation](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Structured graph data, Text summaries, Guidance]

**Output Format:** [JSON results and human-readable summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operation status and source identifiers where available; user-provided sources are not independently verified.]

## Skill Version(s):

1.7.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
