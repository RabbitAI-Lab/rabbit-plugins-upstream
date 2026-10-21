## Description:

Audits and restructures large SKILL.md files into routed skill packs, with backup, validation, rollback, and long-conversation handoff support.

This skill is for research and development only.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

Developers and skill maintainers use this skill to audit and reorganize large SKILL.md files into smaller, navigable packs with backups and rollback. They can also create conversation snapshots and transfer summarized context between chats or users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restructuring can alter local skill files beyond the intended sections.

Mitigation: Review the proposed edits, explicitly approve their scope, make a backup first, and validate or roll back changes.

Risk: Running an untrusted test command can execute arbitrary shell actions.

Mitigation: Avoid --test-command unless the exact command is trusted and reviewed.

Risk: Conversation snapshots or exported archives can expose sensitive transcript content.

Mitigation: Inspect and redact transcripts before creating snapshots or exports; specify source and output paths explicitly.

## Reference(s):

- [Skill Architect on ClawHub](https://clawhub.ai/lisong2003-lgtm/skills/skill-architect)
- [Skill restructuring best practices](artifact/references/瘦身最佳实践.md)
- [Long-conversation summarization best practices](artifact/references/长对话归纳最佳实践.md)
- [Cross-user transfer best practices](artifact/references/跨用户传输最佳实践.md)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown and JSON files with shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local skill packs, routing indexes, backups, and conversation snapshots.]

## Skill Version(s):

0.3.3 (source: frontmatter, manifest.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
