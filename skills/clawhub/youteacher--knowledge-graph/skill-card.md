## Description:

Helps agents store sourced entities and relationships, query bounded subgraphs from a seed entity, attach HTTPS source links, and generate sourced structured summaries through the AI Skills platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create and update knowledge graph entities and relations, query limited-depth subgraphs, attach user-supplied HTTPS sources, and return traceable summaries for downstream reasoning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Graph data and source URLs are sent to the hosted AI Skills platform using the configured API key.

Mitigation: Do not submit secrets as entity names, properties, source URLs, or graph content; block and rotate exposed credentials when detected.

Risk: User-supplied sources are stored for traceability but are not independently verified by the platform.

Mitigation: Present source-backed graph items as user_supplied rather than verified facts, and preserve source IDs without inventing citations.

Risk: Write retries can create uncertainty after timeouts or idempotency conflicts.

Mitigation: Reuse the original idempotency key with identical JSON for the same logical write, and stop for reconciliation when outcome is uncertain.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/knowledge-graph)
- [API key and environment variables](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/knowledge-graph/references/API-KEY.md)
- [HTTP requests, idempotency, and polling](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/knowledge-graph/references/HTTP-REQUESTS.md)
- [Operations, fields, and results](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/knowledge-graph/references/OPERATIONS.md)
- [Security, provenance, and errors](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/knowledge-graph/references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands, HTTP requests, and structured JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses KNOWLEDGE_GRAPH_API_KEY, bounded polling, idempotency keys, and explicit verification labels for user-supplied sources.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
