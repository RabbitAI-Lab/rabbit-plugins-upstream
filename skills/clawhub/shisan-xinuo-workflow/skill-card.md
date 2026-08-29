## Description:

This Chinese-language agent workflow guides engineering tasks through a research-driven 11-step process, L1/L2/L3 triage, dual execution modes, and auditable quality gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zxc663](https://clawhub.ai/user/zxc663)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to make coding agents follow a consistent Chinese-language workflow for task intake, research, reuse checks, risk grading, planning, execution, validation, rollback, and audit records across supported agent platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow asks agents to persistently modify agent rule files, which can alter behavior beyond the current chat.

Mitigation: Install only when persistent workflow behavior is intended, prefer project-scoped on-demand injection, and review the exact diff before any AGENTS.md, CLAUDE.md, or rules-file write.

Risk: Global hard injection can affect all future sessions for a user or environment.

Mitigation: Avoid global hard injection unless that scope is explicitly desired; use project-scoped configuration for narrower adoption.

Risk: Cross-session memory and task-log files may capture project context that should not be shared publicly.

Mitigation: Keep memory and task-log files out of shared or public repositories when they may contain sensitive project context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zxc663/skills/shisan-xinuo-workflow)
- [Project homepage from skill metadata](https://github.com/zxc663/shisan-xinuo-workflow)
- [Platform adaptation](artifact/references/platform-adaptation.md)
- [Workflow and quality gates](artifact/references/workflows.md)
- [Work discipline rules](artifact/references/rules.md)
- [Security and rollback](artifact/references/security.md)
- [Injection core](artifact/references/injection-core.md)
- [Never list](artifact/references/never-list.md)
- [Skill usage routing](artifact/references/skill-usage.md)
- [Implementation details](artifact/references/details.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with templates, example shell hooks, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes optional agent, planning, rollback, task-record, memory, and hook templates for adapting the workflow to supported coding-agent environments.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter metadata.version reports 1.11.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
