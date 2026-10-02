## Description:

MindVault helps agents archive conversations locally as JSONL and turn past conversations into durable rules and project snapshots for context recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouxin121](https://clawhub.ai/user/zhouxin121)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users archive local conversation histories, extract reusable rules, and create project snapshots to restore context across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local long-term archives can retain sensitive prompts, tool metadata, file paths, URLs, attachments, and secrets.

Mitigation: Use explicit source paths and session IDs; review and redact or delete sensitive JSONL and raw records before syncing or sharing.

Risk: Conversation archives persist without automatic cleanup.

Mitigation: Set a retention practice and remove archives no longer needed.

## Reference(s):

- [MindVault on ClawHub](https://clawhub.ai/zhouxin121/skills/mindvault-agent-memory)
- [MindVault usage guide](README.md)
- [MindVault skill instructions](SKILL.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance and commands; local JSONL conversation archives and Markdown memory documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Archives may retain sensitive conversations and metadata; users manage retention and sharing.]

## Skill Version(s):

1.2.5 (source: frontmatter, CHANGELOG, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
