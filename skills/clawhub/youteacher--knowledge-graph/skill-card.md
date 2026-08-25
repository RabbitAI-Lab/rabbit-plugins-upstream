## Description:

Helps agents create, update, query, source, and summarize a user's AI Skills platform knowledge graph through the platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage user-owned knowledge-graph data through the AI Skills platform API, including upserting entities and relations, querying subgraphs, attaching user-supplied HTTPS source links, and generating source-aware summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required KNOWLEDGE_GRAPH_API_KEY could be exposed in requests, logs, graph content, or user-visible output.

Mitigation: Read the key only from the environment, never place it in JSON payloads or logs, and stop if a secret appears in graph fields or source metadata.

Risk: User-supplied source URLs and summaries could be mistaken for platform-verified facts.

Mitigation: Label attached sources as user supplied, avoid fetching or validating the URLs, and explain that source IDs support traceability rather than truth verification.

Risk: Writes or queries could target graph records outside the current user's ownership boundary.

Mitigation: Use only explicit user-provided IDs, rely on platform ownership checks, and do not guess, scan, or probe IDs.

Risk: Repeated write requests after timeouts could create ambiguous or conflicting state.

Mitigation: Use a unique idempotency key for each logical POST and reuse the same key with identical JSON only for retries of that same logical request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/knowledge-graph)
- [AI Skills API root](https://ai-skills.open-idea.net/api/v1)
- [API Key and Site Root](references/API-KEY.md)
- [HTTP Requests, Idempotency, and Polling](references/HTTP-REQUESTS.md)
- [Operations, Fields, and Results](references/OPERATIONS.md)
- [Security, Provenance, and Errors](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown with inline shell commands and JSON request or response details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operation status, task IDs, structured result fields, artifacts metadata, error codes, billing headers, and verification notes.]

## Skill Version(s):

1.0.0 (source: server release evidence and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
