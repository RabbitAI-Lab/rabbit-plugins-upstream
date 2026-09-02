## Description:

Cross Session Memory gives agents a local cross-session memory workflow using human-readable Markdown as the source of truth, a derived SQLite index for selective recall, and lint checks for broken links, duplicates, and stale project facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sharinchan233](https://clawhub.ai/user/sharinchan233)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to add persistent local memory to agents across sessions while keeping memories editable as Markdown and recallable through a local index. It is intended for workflows that need selective recall, deduplication checks, broken-link checks, and stale-fact reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local memory files and memory.db may contain sensitive information that the user intends the agent to recall later.

Mitigation: Keep the memory directory limited to information intended for future recall and protect or delete memory.db as a copy of the Markdown facts.

Risk: Stale project memories, duplicate facts, or broken memory links can lead to incorrect recall.

Mitigation: Run the lifecycle lint checks and verify stale project facts before using recalled information in decisions or edits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sharinchan233/skills/cross-session-memory)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands and local Python script usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local Markdown memory files and a derived SQLite memory.db; no network use is indicated by the security evidence.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
