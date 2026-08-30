## Description:

Claudify helps an agent create, improve, and persist Claude Code automations such as agents, skills, rules, hooks, commands, and plugin guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and automation authors use this skill to choose and draft Claude Code automation artifacts, improve existing automation behavior, and persist useful session knowledge in appropriate documentation or memory locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help create or modify Claude automations, including hooks and global behaviors.

Mitigation: Review generated hooks, agents, skills, rules, commands, and plugin configuration before enabling them globally.

Risk: The persist workflow can save session knowledge into longer-term memory or documentation.

Mitigation: Confirm what will be saved and where; prefer project-local destinations for project-specific information and avoid saving sensitive data.

## Reference(s):

- [Claudify Skill Definition](artifact/SKILL.md)
- [Background Polling](artifact/background-polling.md)
- [Improve Workflow](artifact/improve.md)
- [Persist Workflow](artifact/persist.md)
- [Automation Decision Guide](artifact/resources/automation-decision-guide.md)
- [Plugin Creation Guide](artifact/resources/plugin-creation.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or create Claude Code automation files and memory/documentation updates depending on the selected workflow.]

## Skill Version(s):

0.7.1 (source: server release metadata and changelog, released 2026-08-26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
