## Description:

Shisan Xinuo Workflow gives coding agents a strict, auditable engineering workflow built around research, triage, planning, verification, rollback discipline, and persistent task records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zxc663](https://clawhub.ai/user/zxc663)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to make agent-led coding tasks follow a repeatable governance process with explicit research, L1/L2/L3 triage, planning, rollback, verification, and session records. It is especially relevant for teams that want consistent agent behavior across Codex, Claude Code, Cursor, Windsurf, Trae, WorkBuddy, and similar CLI coding agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to make persistent changes to agent rule files and workspace memory across sessions.

Mitigation: Install it only when a strict workflow is intended; prefer on-demand project-local injection, review the exact files before editing, and keep backups for rule or memory changes.

Risk: Workspace memory records can capture project decisions or sensitive business context if used carelessly.

Mitigation: Keep secrets out of memory files, consider excluding memory records from version control, and review records before sharing or publishing a repository.

Risk: Force injection can affect future agent sessions and possibly other projects when configured globally.

Mitigation: Use global or force injection only after understanding the scope, token cost, and affected platforms; otherwise use the default project-local on-demand mode.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zxc663/skills/shisan-xinuo-workflow)
- [Project homepage](https://github.com/zxc663/shisan-xinuo-workflow)
- [Workflow details](references/workflows.md)
- [Platform adaptation](references/platform-adaptation.md)
- [Security and rollback](references/security.md)
- [Never list](references/never-list.md)
- [Skill usage](references/skill-usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, checklists, shell commands, configuration snippets, and template files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include task records, plans, acceptance criteria, rollback notes, workspace memory entries, agent templates, and optional hook configuration examples.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter reports 1.9.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
