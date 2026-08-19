## Description:

Claudify helps Claude Code users create, improve, and persist agentic automations such as agents, skills, rules, slash commands, hooks, and plugins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use Claudify to convert repeated Claude Code workflows into reusable automations and to review, improve, and persist automation behavior across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated automations may create or alter hooks, rules, memory entries, global or project automations, and local logs with broad local scope.

Mitigation: Review proposed global ~/.claude and project changes before accepting them, and prefer project-local scope unless global behavior is intentional.

Risk: Hook examples and detector behavior can persist local activity records or affect repository state if enabled.

Mitigation: Enable hooks selectively, inspect hook code and configuration, and avoid logging or auto-stage examples unless persistent local records and repository state changes are acceptable.

Risk: Persistence workflows can save session-derived knowledge such as infrastructure details, workflow decisions, or troubleshooting records.

Mitigation: Exclude secrets and sensitive data, and review memory or documentation destinations before saving.

## Reference(s):

- [Claudify Skill Page](https://clawhub.ai/drumrobot/skills/claudify)
- [SKILL.md](SKILL.md)
- [Background Polling](background-polling.md)
- [Improve](improve.md)
- [Persist](persist.md)
- [Automation Decision Guide](resources/automation-decision-guide.md)
- [Agent Templates](resources/agent-templates.md)
- [AskUserQuestion Usage Patterns](resources/askuserquestion-patterns.md)
- [Hook Examples](resources/hook-examples.md)
- [Plugin Creation Guide](resources/plugin-creation.md)
- [Rules Guide](resources/rules-guide.md)
- [Slash Command Syntax Reference](resources/slash-command-syntax.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code snippets and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file changes, hook scripts, and persistent memory or documentation updates for user review.]

## Skill Version(s):

0.6.1 (source: server release evidence and CHANGELOG, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
