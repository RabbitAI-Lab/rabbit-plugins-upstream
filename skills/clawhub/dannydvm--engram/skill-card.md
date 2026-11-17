## Description:

Persistent semantic memory layer for AI agents with local-first storage, Ollama embeddings, typed memories, semantic search, context-aware recall, import/export, REST API, and MCP support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dannydvm](https://clawhub.ai/user/dannydvm)

### License/Terms of Use:


## Use Case:

Developers and agent operators use Engram to persist and retrieve task facts, decisions, preferences, events, and relationships across agent sessions. It is intended to reduce context loss by adding local semantic memory, scoped recall, and MCP or REST access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent local memory may retain sensitive credentials, regulated personal data, or private client material.

Mitigation: Avoid storing sensitive material unless encryption, access control, redaction, retention, and deletion behavior have been verified.

Risk: Broad conversation ingestion can capture more information than intended.

Mitigation: Review content before ingestion and define retention and deletion practices before operational use.

Risk: Installing and running the npm package introduces supply-chain and local service exposure risk.

Mitigation: Pin and audit the npm package before installation and keep the service bound to localhost.

Risk: Reset commands can delete local memory data.

Mitigation: Back up memory data before using reset commands.

## Reference(s):

- [Engram Skill Page](https://clawhub.ai/dannydvm/skills/engram)
- [dannydvm Publisher Profile](https://clawhub.ai/user/dannydvm)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents in adding, searching, recalling, importing, exporting, and managing local semantic memories.]

## Skill Version(s):

0.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
