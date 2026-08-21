## Description:

Claudify helps developers convert workflow needs into Claude Code automations and maintain them through creation, improvement, persistence, and background-polling guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to choose and create Claude Code automation types such as skills, agents, rules, slash commands, hooks, and plugins, then review and persist workflow knowledge. It also guides active polling discipline for long-running background work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide creation or modification of persistent Claude Code automations, including hooks and global behavior.

Mitigation: Prefer project-local scope for project-specific work and review generated hooks or global automations before enabling them.

Risk: Persistence workflows can save session knowledge into long-term stores, which may be inappropriate for sensitive repositories.

Mitigation: Avoid no-ask persistence patterns for sensitive work unless confirmation, scoping, and retention controls are in place.

Risk: Generated automation can introduce incorrect or misleading guidance if accepted without review.

Mitigation: Review and scan generated automation files before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/claudify)
- [SKILL.md](artifact/SKILL.md)
- [Automation Decision Guide](artifact/resources/automation-decision-guide.md)
- [Background Polling](artifact/background-polling.md)
- [Improve](artifact/improve.md)
- [Persist](artifact/persist.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify persistent Claude Code automation files when the agent follows the skill workflow.]

## Skill Version(s):

0.7.0 (source: server release metadata and CHANGELOG.md, released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
