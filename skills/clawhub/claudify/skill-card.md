## Description:

Claudify guides agents through creating, improving, persisting, and monitoring Claude Code automations such as agents, skills, rules, slash commands, hooks, and plugin structures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to decide which Claude Code automation type to create, collect requirements, generate or improve automation assets, preserve durable workflow knowledge, and keep long-running background work actively monitored.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automation changes can affect agent behavior outside the immediate task.

Mitigation: Prefer project-local scope unless global behavior is intentional, and review generated automations before installation.

Risk: Hook examples or hook configuration can run automatically on tool events.

Mitigation: Review hook examples and settings before enabling them, and keep hook ownership tied to an appropriate skill.

Risk: Persistence workflows can save sensitive or unnecessary session details.

Mitigation: Avoid saving secrets, credentials, or sensitive session details into memory, documentation, or logs.

Risk: Long-running background work can hang or leave the user without progress visibility.

Mitigation: Use explicit command timeouts and active polling or wakeups for long-running background dispatches.

## Reference(s):

- [Claudify Skill Page](https://clawhub.ai/drumrobot/skills/claudify)
- [Skill Definition](artifact/SKILL.md)
- [Background Polling](artifact/background-polling.md)
- [Improve Topic](artifact/improve.md)
- [Persist Topic](artifact/persist.md)
- [Automation Decision Guide](artifact/resources/automation-decision-guide.md)
- [Hook Examples](artifact/resources/hook-examples.md)
- [Plugin Creation Guide](artifact/resources/plugin-creation.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tables, checklists, code blocks, file paths, and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Topic-routed guidance for create, improve, persist, and background-polling workflows.]

## Skill Version(s):

0.5.2 (source: server release metadata and CHANGELOG, released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
