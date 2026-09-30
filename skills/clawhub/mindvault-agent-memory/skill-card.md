## Description:

Archives agent conversations in local JSONL files and helps extract lasting rules and project snapshots for context recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouxin121](https://clawhub.ai/user/zhouxin121)

### License/Terms of Use:

MIT

## Use Case:

Agent users and developers archive conversations locally, distill reusable preferences and rules, and generate project snapshots to restore context across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local conversation archives can contain secrets, personal data, prompts, tool parameters, paths, and attachment metadata.

Mitigation: Treat the archive directory as sensitive; avoid archiving secrets and redact or delete sensitive records when needed.

Risk: Exporting from the wrong source or to the wrong destination can retain unintended conversations.

Mitigation: Review source and destination paths before export and periodically remove archives no longer needed.

## Reference(s):

- [MindVault on ClawHub](https://clawhub.ai/zhouxin121/skills/mindvault-agent-memory)
- [Publisher profile: zhouxin121](https://clawhub.ai/user/zhouxin121)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, JSONL files]

**Output Format:** [Text instructions and local JSONL and Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-triggered local archive, memory/FACT.md, and PROJECT_SNAPSHOT.md]

## Skill Version(s):

1.2.3 (source: release metadata, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
