## Description:

Helps manage Claude Code, Antigravity, and OpenClaw sessions through discovery, analysis, context tracking, repair, migration, and cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to find, review, organize, repair, and clean up local agent sessions and monitor context usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reading session history may expose private conversation content.

Mitigation: Grant access only if local session history and settings are appropriate for this skill to read.

Risk: Import, RAG, or memory synchronization may forward sensitive transcript content.

Mitigation: Review and redact transcript content before sending it to other agents, stores, or memory.

Risk: Cleanup, repair, rewind, and migration can rewrite or delete session files.

Mitigation: Preview with dry-run modes and back up sessions; avoid destructive actions on live sessions.

Risk: Installed hooks and MCP registration can persist changes to agent settings.

Mitigation: Review hook and MCP configuration before installing or enabling them.

## Reference(s):

- [Session on ClawHub](https://clawhub.ai/drumrobot/skills/session)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files]

**Output Format:** [Markdown responses and shell commands; local session files when actions are executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some actions modify, move, or delete local session files.]

## Skill Version(s):

0.14.1 (source: ClawHub release and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
