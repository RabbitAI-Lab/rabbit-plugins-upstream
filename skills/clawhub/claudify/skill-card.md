## Description:

Claudify guides agents through creating, improving, persisting, and safely managing Claude Code automations such as agents, skills, rules, slash commands, hooks, and plugins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Claudify to select and build the right Claude Code automation type, improve existing automation behavior, persist useful project knowledge, and keep long-running background work actively monitored.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help create or modify Claude Code automations, including hooks and global files with local side effects.

Mitigation: Prefer project-local scope and review generated hooks, global files, and automation changes before installation or deployment.

Risk: Persistence and improvement workflows may write memory or prune accumulated notes.

Mitigation: Approve the content and destination before memory writes, documentation updates, or pruning actions are applied.

Risk: Hook examples are templates and may not be hardened for a specific environment.

Mitigation: Adapt hook examples to the target project, scan them before use, and avoid treating examples as ready-to-run defaults.

## Reference(s):

- [Claudify skill page](https://clawhub.ai/drumrobot/skills/claudify)
- [Automation decision guide](resources/automation-decision-guide.md)
- [AskUserQuestion usage patterns](resources/askuserquestion-patterns.md)
- [Agent templates](resources/agent-templates.md)
- [Rules guide](resources/rules-guide.md)
- [Slash command syntax reference](resources/slash-command-syntax.md)
- [Hook examples](resources/hook-examples.md)
- [Plugin creation guide](resources/plugin-creation.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with code, shell command, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or create Claude Code automation files when the host agent has suitable write tools and user-approved scope.]

## Skill Version(s):

0.5.3 (source: release metadata and changelog, released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
