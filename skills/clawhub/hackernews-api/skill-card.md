## Description:

Provides read-only access to Hacker News public data including stories, items, users, feeds, and search with bounded pagination and comment threading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agents use this skill to read public Hacker News feeds, items, user profiles, and search results through normalized, bounded API and tool contracts. It is suited for retrieval, summarization, monitoring, and lightweight research workflows that do not require posting, voting, login, or other mutation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup queries are sent to the ReplyNodes gateway.

Mitigation: Use the skill only when sending Hacker News query terms, item IDs, and user handles to ReplyNodes is acceptable for the workflow.

Risk: Workspace keys or payer credentials could be exposed if handled in prompts, logs, or files.

Mitigation: Store API keys and payer configuration in a secret store and avoid printing or committing credential material.

Risk: A 402 response can be mistaken for completed payment or successful access.

Mitigation: Treat HTTP 402 as a payment-requirements advertisement and only rely on data returned after a successful follow-up request.

Risk: The bundle checksum list references a missing skill-card.md file.

Mitigation: Validate the package files against the current artifact and treat the inconsistency as packaging metadata rather than evidence of hidden behavior.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/replynodes-ai/skills/hackernews-api)
- [Endpoint Catalog](artifact/references/endpoints.md)
- [OpenAPI Specification](artifact/references/hackernews-public-v1.openapi.json)
- [MCP Tool Schema](artifact/references/hackernews-mcp.schema.json)
- [Publication Evidence](artifact/evidence/publication-evidence.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, JSON, Shell commands, Configuration]

**Output Format:** [Markdown guidance, JSON schemas, shell examples, and normalized JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only GET operations with bounded pagination, bounded comment depth, normalized error metadata, Bearer workspace-key authentication, or x402 v2 payment negotiation.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
