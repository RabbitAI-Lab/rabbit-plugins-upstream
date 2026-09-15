## Description:

Shisan Xinuo Workflow helps coding agents follow an auditable engineering workflow with task triage, quality gates, rollback discipline, platform adaptation, and prompt-injection safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zxc663](https://clawhub.ai/user/zxc663)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to make coding agents follow consistent task triage, planning, validation, documentation, rollback, and review practices across Codex, Claude Code, Cursor, Trae, Windsurf, WorkBuddy, and similar CLI agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent workflow injection can change future agent behavior across sessions.

Mitigation: Prefer on-demand, project-local use and enable hard injection, global memory or rule writes, or hooks only after reviewing exact target paths and diffs.

Risk: Automatic project file changes or baseline commits can affect third-party, temporary, or read-only repositories.

Mitigation: Avoid automatic carrier creation and git baseline commits unless the repository owner has approved them and rollback is clear.

## Reference(s):

- [Project homepage](https://github.com/zxc663/shisan-xinuo-workflow)
- [Workflow and quality gates](references/workflows.md)
- [Security and rollback guidance](references/security.md)
- [Platform adaptation](references/platform-adaptation.md)
- [Injection core](references/injection-core.md)
- [Hooks templates overview](templates/hooks/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code, shell, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project file templates and optional hook examples; review target paths before applying persistent changes.]

## Skill Version(s):

1.0.16 (source: server release metadata; artifact metadata version 2.8.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
