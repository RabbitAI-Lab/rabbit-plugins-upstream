## Description:

Shisan Xinuo Workflow is an agent engineering discipline skill that routes coding, review, and multi-file engineering work through auditable workflow lanes, quality gates, rollback checks, and platform-adaptation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zxc663](https://clawhub.ai/user/zxc663)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to make agent-assisted engineering work more disciplined and auditable, especially for coding, bug fixing, component work, reviews, multi-file changes, and platform-specific agent workflow setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist workflow rules across sessions and modify project rule, memory, or global agent configuration files.

Mitigation: Prefer on-demand mode, review every target path before approving hard injection or hooks, and keep backups before allowing persistent changes.

Risk: Shared or sensitive repositories may be affected by added workflow files, logs, or configuration changes.

Mitigation: Use the skill only when the team agrees to the added files and logging, and avoid installation in sensitive repositories unless that risk is accepted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zxc663/skills/shisan-xinuo-workflow)
- [Project Homepage](https://github.com/zxc663/shisan-xinuo-workflow)
- [Global Agent Workflow Core](references/injection-core.md)
- [Platform Adaptation](references/platform-adaptation.md)
- [Skill Usage Module](references/skill-usage.md)
- [Workflows and Quality Gates](references/workflows.md)
- [Security and Rollback](references/security.md)
- [Never List](references/never-list.md)
- [Detailed Engineering Practices](references/details.md)
- [New Project Bootstrap](references/new-project-bootstrap.md)
- [Local Model Glossary](references/local-model-glossary.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance, checklists, templates, and shell/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or create workflow records, project rule files, memory files, and optional hook configuration as part of the agent workflow.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter metadata version is 2.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
