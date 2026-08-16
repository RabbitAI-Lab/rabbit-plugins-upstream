## Description:

Claudify helps Claude Code agents create, improve, persist, and coordinate automations such as agents, skills, rules, hooks, commands, and long-running background workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use Claudify to turn repeated Claude Code workflows into durable automations, review and improve existing automations, and persist reusable session knowledge in the right project or skill location.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic long-term storage can capture session or project knowledge without clear per-item consent.

Mitigation: Review proposed persistence targets before running persist or cleanup flows, and avoid saving secrets, credential locations, personal data, or project-private details unless explicitly approved.

Risk: Generated or modified hooks can perform unexpected logging, staging, validation, or build actions.

Mitigation: Inspect generated hook configuration and scripts before deployment, with extra attention to logging, auto-stage, and build hooks.

Risk: Global automations can unintentionally encode project-specific assumptions.

Mitigation: Prefer project-local automations unless the behavior is clearly reusable across projects.

## Reference(s):

- [Claudify Skill Page](https://clawhub.ai/drumrobot/skills/claudify)
- [Background Polling](artifact/background-polling.md)
- [Improve](artifact/improve.md)
- [Persist](artifact/persist.md)
- [Automation Decision Guide](artifact/resources/automation-decision-guide.md)
- [AskUserQuestion Usage Patterns](artifact/resources/askuserquestion-patterns.md)
- [Hook Examples](artifact/resources/hook-examples.md)
- [Plugin Creation Guide](artifact/resources/plugin-creation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, configuration snippets, and structured recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or modify automation files, hook settings, slash commands, rules, and persistent documentation depending on user approval and workflow path.]

## Skill Version(s):

0.5.4 (source: server release metadata and CHANGELOG.md, released 2026-08-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
