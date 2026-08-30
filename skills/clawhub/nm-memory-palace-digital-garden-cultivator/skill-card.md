## Description:

Manages digital garden notes, link structures, and health metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and documentation maintainers use this skill to organize evolving note collections, maintain bidirectional links, track content maturity, and decide when knowledge should be archived or formalized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes note-cleanup guidance such as archive, move, remove, and delete actions.

Mitigation: Require user confirmation before changing, archiving, moving, or deleting garden files.

Risk: Broad activation terms may cause the skill to appear during general linking, curation, knowledge-base, or documentation tasks.

Mitigation: Confirm that the current task is specifically about digital garden maintenance before applying its workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-memory-palace-digital-garden-cultivator)
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/memory-palace)
- [Linking Patterns](artifact/modules/linking-patterns.md)
- [Maintenance Guide](artifact/modules/maintenance.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown with inline YAML and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe note layouts, maintenance schedules, link patterns, health metrics, and review actions for garden files.]

## Skill Version(s):

1.9.19 (source: server release evidence; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
