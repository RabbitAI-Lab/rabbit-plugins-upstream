## Description:

Manages Claude Code and Antigravity sessions, including session lookup, listing, search, import, summarization, analysis, archive, classification, cleanup, compression, context measurement, migration, movement, purge, rename, repair, rewind, and URL generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to inspect and manage Claude Code and Antigravity session records, recover or rewrite session metadata, and coordinate local session cleanup, migration, compression, and context measurement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect Claude Code and Antigravity session history, which may include sensitive transcript content.

Mitigation: Install only in trusted environments and review session content before using import, summarization, or RAG-related dispatch.

Risk: Some workflows can move, delete, truncate, or rewrite session files.

Mitigation: Prefer dry-run and backup modes, confirm session IDs before acting, and verify backup paths before using migrate, purge, destroy, repair, or rewind operations.

Risk: Hook registration can persist session ID injection commands in settings.json.

Mitigation: Review SessionStart and UserPromptSubmit hook entries before enabling or distributing the configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/session)
- [Session skill overview](artifact/SKILL.md)
- [Install session ID hook](artifact/install.md)
- [Repair session](artifact/repair.md)
- [Session rewind](artifact/rewind.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run local session file operations; review destructive commands before execution.]

## Skill Version(s):

0.12.1 (source: server release metadata and CHANGELOG, released 2026-09-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
