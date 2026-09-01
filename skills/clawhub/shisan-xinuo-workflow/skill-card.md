## Description:

Shisan Xinuo Workflow is an agent workflow governance skill that routes engineering tasks through auditable L1, L2-S, and L2-F tracks, quality gates, safety rules, and optional platform adaptation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zxc663](https://clawhub.ai/user/zxc663)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to make coding agents follow a structured, auditable workflow for implementation, debugging, review, documentation, and release tasks across supported agent platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist workflow rules and memory across future sessions or projects.

Mitigation: Prefer on-demand or project-scoped installation and review proposed changes to AGENTS.md, CLAUDE.md, memory, docs, and platform memory files before relying on them.

Risk: Hard injection and shell hook configuration can affect future agent sessions.

Mitigation: Do not enable hard injection or shell hooks unless the scope, target files, and ongoing session impact are understood and accepted.

Risk: Generated logs, preferences, and memory files may capture project context.

Mitigation: Keep generated logs and preferences out of public repositories unless they have been reviewed and sanitized.

Risk: Auto-created project documentation and rule files can change workspace behavior.

Mitigation: Review proposed or generated project files before committing them and remove entries that do not match the intended workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zxc663/skills/shisan-xinuo-workflow)
- [Publisher profile](https://clawhub.ai/user/zxc663)
- [Project homepage](https://github.com/zxc663/shisan-xinuo-workflow)
- [Skill definition](artifact/SKILL.md)
- [Security and rollback guidance](artifact/references/security.md)
- [Platform adaptation guidance](artifact/references/platform-adaptation.md)
- [Workflow and quality gates](artifact/references/workflows.md)
- [Global workflow injection core](artifact/references/injection-core.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, templates, configuration snippets, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or propose workflow records, memory files, project rule files, platform rule snippets, and optional hook configuration depending on installation mode.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
