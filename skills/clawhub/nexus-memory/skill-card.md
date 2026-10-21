## Description:

Gives Claude Code persistent, searchable memory across sessions, with automatic recall and capture backed by Qdrant and local embeddings by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neboy72](https://clawhub.ai/user/neboy72)

### License/Terms of Use:

MIT-0

## Use Case:

Claude Code users and developers use this skill to retain and search project context between sessions, with optional shared memory across agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic capture can retain sensitive conversation details or client material and resurface them later.

Mitigation: Avoid use with secrets or regulated data without retention rules; disable automatic capture and delete unwanted memories with the forget tool.

Risk: Agents or projects using the same Qdrant collection can see one another's memories.

Mitigation: Use a separate NEXUS_COLLECTION for contexts that must not share memory.

Risk: Selecting a cloud embedding provider sends memory text to that provider.

Mitigation: Keep the default local embedding provider when memory must remain local.

## Reference(s):

- [Nexus Memory on ClawHub](https://clawhub.ai/neboy72/skills/nexus-memory)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown memory recall and responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recalls up to five memories per prompt by default; captured facts persist for future sessions.]

## Skill Version(s):

0.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
