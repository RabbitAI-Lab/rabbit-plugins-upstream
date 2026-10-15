## Description:

Audits and restructures large skills into routed, reusable components and creates snapshots and handoff packages for long conversations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to audit and reorganize large SKILL.md files, or to preserve and transfer key decisions from long conversations through snapshots and reusable skill packs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local refactoring can change skill files or produce unexpected outputs.

Mitigation: Invoke explicitly, review configuration and planned changes, and back up files before editing.

Risk: An untrusted test command can execute local code.

Mitigation: Do not pass untrusted values to --test-command.

Risk: Imported handoffs may expose private conversation content to an agent.

Mitigation: Inspect handoff ZIP files and snapshots for sensitive content before importing them.

## Reference(s):

- [Skill Architect on ClawHub](https://clawhub.ai/lisong2003-lgtm/skills/skill-architect)
- [Skill slimming best practices](artifact/references/瘦身最佳实践.md)
- [Long-conversation summarization best practices](artifact/references/长对话归纳最佳实践.md)
- [Cross-user handoff best practices](artifact/references/跨用户传输最佳实践.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown reports, skill files, routing indexes, conversation snapshots, and optional ZIP handoffs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write local skill files, backups, and conversation handoffs.]

## Skill Version(s):

1.0.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
