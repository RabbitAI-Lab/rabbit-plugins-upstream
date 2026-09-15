## Description:

Agentic AI lifecycle support for creating Claude Code automations, improving agent behavior, persisting useful session knowledge, and managing long-running background polling discipline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to convert recurring work into Claude Code agents, skills, rules, commands, hooks, or plugins, then review and preserve useful automation patterns across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can manage Claude automation and may review global Claude configuration.

Mitigation: Install it only when that behavior is desired, prefer project-scoped use, and require approval before global configuration inspection.

Risk: The persist workflow can save session knowledge to memory or RAG-backed stores.

Mitigation: Require explicit approval before memory or RAG writes, and exclude sensitive data such as credentials and secrets.

Risk: Hook examples may be copied into active automation without enough hardening.

Mitigation: Review and harden hook examples before use, including pinning external commands and avoiding shared temporary files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/claudify)
- [Creation workflow](SKILL.md)
- [Background polling](background-polling.md)
- [Improve workflow](improve.md)
- [Persist workflow](persist.md)
- [Automation decision guide](resources/automation-decision-guide.md)
- [Hook examples](resources/hook-examples.md)
- [Plugin creation guide](resources/plugin-creation.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code, shell command, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or recommend automation files when used in an agent environment with write-capable tools.]

## Skill Version(s):

0.10.0 (source: release metadata and CHANGELOG, released 2026-09-13; SKILL.md frontmatter lists 0.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
