## Description:

Knowledge Graph stores sourced entities and relationships, queries bounded subgraphs from a seed entity, attaches HTTPS source links, and generates traceable structured summaries through the AI Skills platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to persist user-directed knowledge graph data, query limited graph neighborhoods, attach source URLs, and return structured summaries with provenance indicators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Graph entities, relationships, and source URLs are stored with the AI Skills platform.

Mitigation: Install only when that storage model is acceptable for the data being handled.

Risk: Secrets could be exposed if they are placed in graph fields, source URLs, logs, artifacts, or command arguments.

Mitigation: Use the KNOWLEDGE_GRAPH_API_KEY environment variable, avoid submitting secrets in graph content, and rotate any secret that was exposed.

Risk: User-supplied source URLs and graph claims are provenance signals, not verified facts.

Mitigation: Present verification values accurately and do not describe user-supplied sources as independently validated.

Risk: Write operations can have uncertain results after timeouts or idempotency conflicts.

Mitigation: Reuse the original idempotency key with the same JSON for the same logical request and stop for manual reconciliation when required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/knowledge-graph)
- [API key and site root](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/API-KEY.md)
- [HTTP requests, idempotency, and polling](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/HTTP-REQUESTS.md)
- [Operations, fields, and results](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/OPERATIONS.md)
- [Security, provenance, and errors](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires KNOWLEDGE_GRAPH_API_KEY; graph data and source URLs are stored on the AI Skills platform.]

## Skill Version(s):

1.4.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
