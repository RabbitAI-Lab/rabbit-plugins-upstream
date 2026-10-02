## Description:

Provides persistent, searchable memory across Claude Code sessions using Qdrant, with local embeddings by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neboy72](https://clawhub.ai/user/neboy72)

### License/Terms of Use:

MIT-0

## Use Case:

Claude Code users and developers use the skill to retain, search, and recall project context across sessions, optionally sharing a memory store with other agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conversation facts may be retained automatically and reused in later sessions.

Mitigation: Avoid secrets, regulated data, and client material without an approved retention policy; establish a deletion process or disable automatic capture.

Risk: A shared memory collection can expose project context to other connected agents.

Mitigation: Use separate NEXUS_COLLECTION values where project contexts must remain isolated.

Risk: Selecting cloud embeddings can send memory text to an external provider.

Mitigation: Keep the default local embedding provider unless external processing is approved.

## Reference(s):

- [Nexus Memory on ClawHub](https://clawhub.ai/neboy72/skills/nexus-memory)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Relevant memories can be injected into subsequent prompts.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
