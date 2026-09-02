## Description:

Claudify guides agents through creating, improving, persisting, and polling Claude Code automations such as agents, skills, rules, commands, and hooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Claudify to turn repeated Claude Code workflows into reusable automations and to maintain those automations through improvement, persistence, and background-polling procedures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change future Claude behavior by authoring or modifying persistent automations.

Mitigation: Prefer project-local scope and review every target path and proposed write before applying changes.

Risk: Example hooks or automation patterns may run automatically if enabled without hardening.

Mitigation: Avoid enabling example hooks until they have been reviewed, hardened, and scanned for the target environment.

Risk: Persistence workflows may save session-derived knowledge through memory or RAG mechanisms.

Mitigation: Confirm that memory, RAG persistence, and local tool-use logs are acceptable for the project before using persistence topics.

## Reference(s):

- [Claudify on ClawHub](https://clawhub.ai/drumrobot/skills/claudify)
- [SKILL.md](artifact/SKILL.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)
- [Improve topic](artifact/improve.md)
- [Persist topic](artifact/persist.md)
- [Background polling topic](artifact/background-polling.md)
- [Automation decision guide](artifact/resources/automation-decision-guide.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct creation or modification of automation files when the host agent has write-capable tools.]

## Skill Version(s):

0.8.0 (source: ClawHub release metadata and CHANGELOG, released 2026-09-01)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
