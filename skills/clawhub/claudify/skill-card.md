## Description: <br>
Claudify helps agents convert requested functionality into Claude Code automations and maintain them through improvement, persistence, and background polling workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use Claudify to decide whether requested functionality should become an agent, skill, rule, command, hook, or plugin, then produce the corresponding automation guidance and artifacts. It also supports follow-up maintenance workflows for self-improvement, knowledge persistence, and long-running background work discipline. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create persistent agent automations, including hooks that may run commands automatically. <br>
Mitigation: Review proposed hooks and automation files before installation, require confirmation before writes, and prefer project-local scope. <br>
Risk: The skill can inspect global Claude plugin metadata and write memory or failed-attempt records from session context. <br>
Mitigation: Limit persistence to non-sensitive information, avoid global scope unless needed, and review memory or documentation changes before saving. <br>
Risk: Example automations may stage git changes, install extensions, or log broad tool use if enabled without review. <br>
Mitigation: Enable only examples that are needed for the project and remove or narrow commands that change repositories, install software, or collect excessive logs. <br>


## Reference(s): <br>
- [Claudify on ClawHub](https://clawhub.ai/drumrobot/skills/claudify) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Background Polling](artifact/background-polling.md) <br>
- [Improve](artifact/improve.md) <br>
- [Persist](artifact/persist.md) <br>
- [Automation Decision Guide](artifact/resources/automation-decision-guide.md) <br>
- [Hook Examples](artifact/resources/hook-examples.md) <br>
- [Plugin Creation](artifact/resources/plugin-creation.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with code, JSON, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose file writes, hook configuration, persistent memory records, and automation artifacts that should be reviewed before installation or execution.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release metadata and CHANGELOG, released 2026-07-23; SKILL.md frontmatter lists 0.1.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
