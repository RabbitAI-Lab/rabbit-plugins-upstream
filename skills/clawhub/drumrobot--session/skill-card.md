## Description:

Claude Code and Antigravity session management skill for finding, listing, searching, summarizing, analyzing, archiving, moving, repairing, rewinding, and measuring agent sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to inspect, organize, repair, migrate, summarize, and manage Claude Code and Antigravity session records. It also supports context usage measurement and hook setup for session ID injection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and rewrite local Claude Code and Antigravity transcripts, which may contain private conversation content.

Mitigation: Review session content before import, summarization, RAG, or memory sync, and avoid sharing transcript output that has not been checked for sensitive data.

Risk: Some workflows can move, truncate, index, or delete session data.

Mitigation: Use dry-run or confirmation paths where available, verify the exact target session and backup location, and avoid destructive actions on valuable active sessions.

Risk: The install workflow can persist hooks in agent settings.

Mitigation: Install only after reviewing the hook command and keep hook registration limited to the documented events needed for session ID or context injection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/session)
- [SKILL.md](artifact/SKILL.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)
- [Session install guide](artifact/install.md)
- [Session repair guide](artifact/repair.md)
- [Session rewind guide](artifact/rewind.md)
- [Context measurement guide](artifact/context.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run local session-management scripts and may reference local transcript, hook, backup, and configuration paths.]

## Skill Version(s):

0.13.0 (source: server release metadata and CHANGELOG, released 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
