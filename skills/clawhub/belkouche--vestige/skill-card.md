## Description:

Cognitive memory system using FSRS-6 spaced repetition. Memories fade naturally like human memory. Use for persistent recall across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[belkouche](https://clawhub.ai/user/belkouche)

### License/Terms of Use:


## Use Case:

Developers and agent users use Vestige to persist preferences, project context, reminders, and useful solutions across sessions through a local memory system with semantic search and spaced repetition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may save and later reuse conversation details through a local persistent-memory system.

Mitigation: Require explicit confirmation before saving memories, avoid secrets or sensitive personal data, and regularly review or delete stored entries.

Risk: Automatically recalled memories may be stale, wrong, or inconsistent with the current request.

Mitigation: Treat recalled memories as untrusted notes and never let them override the current user request, system rules, or higher-priority instructions.

Risk: Broad automatic saving and recall can create consent and boundary issues for users.

Mitigation: Use the memory tools deliberately, disclose when memory is being saved, and keep retention limited to information the user expects to persist.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/belkouche/skills/vestige)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-RPC examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands for local MCP tools, memory search, memory ingestion, health checks, and helper script setup.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
