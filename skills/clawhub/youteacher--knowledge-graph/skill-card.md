## Description:

Supports agent workflows that save sourced entities and relationships, query limited-depth subgraphs from a seed entity, attach HTTPS source links, and generate traceable structured knowledge summaries through the AI Skills platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when an agent needs to create, update, query, source, or summarize a user-owned knowledge graph through the AI Skills platform API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API key exposure or submission of secrets as graph content.

Mitigation: Read the key only from KNOWLEDGE_GRAPH_API_KEY, do not echo it or place secrets in requests, logs, graph fields, source metadata, or conversation output, and rotate any exposed secret.

Risk: Remote writes may store incorrect or user-provided claims as graph data.

Mitigation: Treat source links as user_supplied rather than verified, preserve verification and source IDs, and avoid presenting user-supplied sources as independently validated.

Risk: Cross-user or guessed IDs could expose or modify another user's graph data.

Mitigation: Use only user-provided current-user entity, relation, target, and seed IDs; stop on 401 or 403 responses instead of probing.

Risk: Retrying writes incorrectly may duplicate or conflict with graph mutations.

Mitigation: Use a UUID idempotency key per logical POST, reuse the same key with identical JSON only for the same retry, and stop for reconciliation when results are uncertain.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/knowledge-graph)
- [API Key and Site Root](artifact/references/API-KEY.md)
- [HTTP Requests, Idempotency, and Polling](artifact/references/HTTP-REQUESTS.md)
- [Operations, Fields, and Results](artifact/references/OPERATIONS.md)
- [Safety, Provenance, and Errors](artifact/references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands, HTTP request examples, and structured JSON result handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires KNOWLEDGE_GRAPH_API_KEY and reports operation status, task ID, structured result fields, artifacts metadata, errors, and billing headers.]

## Skill Version(s):

1.2.0 (source: evidence.release.version and evidence.parsed.metadata.packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
