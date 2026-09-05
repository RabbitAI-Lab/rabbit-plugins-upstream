## Description:

Search and manage a Qdrant vector knowledge base via local CLI helper

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhlhlf](https://clawhub.ai/user/zhlhlf)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to search, populate, inspect, and manage a Qdrant-backed knowledge base for reusable project documents, manuals, and operational knowledge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches, upserts, and migrations can send text to the configured Qdrant and embedding endpoints.

Mitigation: Review QDRANT_URL, QDRANT_COLLECTION, EMBEDDING_BASE_URL, and related credentials before use, and only configure endpoints approved for the data being indexed or queried.

Risk: The migrate-sqlite command can bulk-copy local OpenClaw memory into Qdrant.

Mitigation: Run migration only when that transfer is intended, and check the selected SQLite database path and destination collection first.

Risk: The delete command removes persistent vector entries by point ID without a built-in confirmation step.

Mitigation: Verify the collection and point ID before deleting, and prefer listing or searching the target record first.

## Reference(s):

- [ClawHub qdrant-db skill page](https://clawhub.ai/zhlhlf/skills/qdrant-db)
- [ClawHub publisher profile](https://clawhub.ai/user/zhlhlf)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call configured Qdrant and embedding endpoints and may read local files or SQLite memory when those commands are used.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
