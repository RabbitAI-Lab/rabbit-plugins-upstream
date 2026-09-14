## Description:

Shisan Xinuo Workflow guides coding agents through a tiered engineering workflow with task triage, quality gates, rollback practices, project memory, and optional platform-specific rule injection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zxc663](https://clawhub.ai/user/zxc663)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to make coding agents follow auditable engineering workflows for hands-on coding, multi-file changes, bug fixes, component work, reviews, and project governance. It is not intended for casual chat, read-only single-file lookups, or non-engineering conversations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill deliberately persists workflow rules into agent instruction and memory locations, including automatic project file creation.

Mitigation: Install only when agent-wide engineering governance is intended; prefer on-demand or project-local use, and review every proposed AGENTS.md, CLAUDE.md, memory, or config change before writing.

Risk: Hard injection can affect future sessions and agent behavior beyond the immediate task.

Mitigation: Avoid hard injection unless the cross-session impact is understood and wanted; keep changes scoped to controlled projects when possible.

Risk: Optional hook templates can run platform-specific scripts, and relative paths can be unsafe when copied into uncontrolled projects.

Mitigation: Do not enable hook templates with relative project paths unless the referenced scripts and platform behavior are controlled and reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zxc663/skills/shisan-xinuo-workflow)
- [Project homepage](https://github.com/zxc663/shisan-xinuo-workflow)
- [details.md](artifact/references/details.md)
- [injection-core.md](artifact/references/injection-core.md)
- [never-list.md](artifact/references/never-list.md)
- [platform-adaptation.md](artifact/references/platform-adaptation.md)
- [rules.md](artifact/references/rules.md)
- [security.md](artifact/references/security.md)
- [skill-usage.md](artifact/references/skill-usage.md)
- [workflows.md](artifact/references/workflows.md)
- [Hook templates README](artifact/templates/hooks/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, checklists, templates, and inline shell commands/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes workflow templates, optional hook examples, and a detail lookup script for local reference lookup.]

## Skill Version(s):

1.0.15 (source: ClawHub release; embedded skill metadata version: 2.7.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
