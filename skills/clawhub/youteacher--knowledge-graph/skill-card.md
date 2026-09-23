## Description:

Helps agents create, query, source, and summarize a user-owned knowledge graph through the AI Skills platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when they need to store sourced entities and relations, query a limited-depth subgraph from a seed entity, attach HTTPS sources, or produce source-aware graph summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected graph entities, relations, and HTTPS source links are sent to the disclosed AI Skills knowledge-graph service.

Mitigation: Use the skill only when that data sharing is acceptable, and keep sensitive information out of graph fields and source URLs.

Risk: The configured API key could be exposed through prompts, graph data, URLs, logs, or command arguments.

Mitigation: Store the key only in KNOWLEDGE_GRAPH_API_KEY, protect it as a secret, and rotate any key that may have been exposed.

Risk: User-supplied sources and graph content are traceability signals, not independently verified facts.

Mitigation: Preserve verification status and source IDs in outputs, and do not present user-supplied source associations as platform-verified claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/knowledge-graph)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key and environment](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/API-KEY.md)
- [HTTP requests, idempotency, and polling](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/HTTP-REQUESTS.md)
- [Operations, fields, and results](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/OPERATIONS.md)
- [Safety, sources, and errors](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires KNOWLEDGE_GRAPH_API_KEY; API responses include task status, task IDs, structured graph results, artifacts metadata, errors, and billing headers.]

## Skill Version(s):

1.5.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
