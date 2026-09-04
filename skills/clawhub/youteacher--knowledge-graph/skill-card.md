## Description:

Helps agents create and query sourced knowledge graph entities, relations, HTTPS source links, and source-aware summaries through the AI Skills platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a user asks to store graph entities or relationships, attach user-provided HTTPS sources, query a bounded subgraph from a seed entity, or generate a traceable structured summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Graph fields, source URLs, logs, or generated commands could expose secrets if users include credentials in submitted data.

Mitigation: Keep KNOWLEDGE_GRAPH_API_KEY in the environment only, scan user-provided fields for secrets before POST requests, and refuse to submit or echo exposed credentials.

Risk: The hosted Knowledge Graph service stores selected entities, relations, and source URLs supplied by the user.

Mitigation: Install and use the skill only when storing that selected graph data in the AI Skills hosted service is acceptable for the user and organization.

Risk: Attached sources are user supplied and are not platform-verified for reachability, truth, authority, or freshness.

Mitigation: Describe source-backed claims as user-supplied, preserve source IDs for traceability, and avoid presenting them as independently verified facts.

Risk: Retrying write requests with changed payloads or new idempotency keys after uncertainty can duplicate or conflict with graph operations.

Mitigation: Use one saved idempotency key per logical POST, reuse it only with identical JSON after timeouts, and stop for reconciliation when the result is uncertain.

## Reference(s):

- [Knowledge Graph skill page](https://clawhub.ai/youteacher/skills/knowledge-graph)
- [API key and site root](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/API-KEY.md)
- [HTTP requests, idempotency, and polling](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/HTTP-REQUESTS.md)
- [Operations, fields, and results](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/OPERATIONS.md)
- [Behavior rules, provenance, and errors](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request bodies, polling steps, task status, result fields, artifact metadata, error codes, and billing response headers.]

## Skill Version(s):

1.5.0 (source: server release metadata and skill metadata packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
