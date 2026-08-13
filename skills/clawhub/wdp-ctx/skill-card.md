## Description:

Use when the user runs /wdp-ctx to save, load, verify, export, or clear the project's context so it survives session reset and can be resumed by any coding agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckystar513](https://clawhub.ai/user/luckystar513)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding-agent users use this skill to preserve project context across resets, compaction, session changes, and agent handoffs. It writes and reads Markdown profile, snapshot, verification, export, listing, and cleanup workflows for ongoing software projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project context snapshots may accidentally include sensitive information if users record credential values.

Mitigation: Follow the skill rule to record only credential locations, not secrets, tokens, or passwords, and review snapshots before sharing them.

Risk: The optional hook persists in Claude settings when installed globally.

Mitigation: Use project-scoped settings for project-only reminders and review the hook path before adding it to global settings.

Risk: The clear workflow removes saved snapshots.

Mitigation: Use the built-in list-and-confirm flow, keep profiles by default, and use --keep when retaining recent snapshots is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luckystar513/skills/wdp-ctx)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown files, concise text reports, and shell/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates timestamped snapshots and stable profile documents; optional hook only emits reminder messages.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
