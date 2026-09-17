## Description:

Provides an auditable engineering workflow discipline for agent coding tasks, routing work through quick, short, or full workflows with quality gates, rollback practices, and platform-adaptable governance templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zxc663](https://clawhub.ai/user/zxc663)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to apply a consistent workflow to coding, debugging, review, project setup, and multi-file engineering tasks. It is intended to make agent work more auditable through task classification, explicit checkpoints, records, templates, and security review prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can exert broad persistent control over agent workflow behavior through global rules, memory anchors, or hooks.

Mitigation: Prefer on-demand or project-local installation first, and approve persistent controls only after reviewing the exact target paths, diffs, backups, and removal procedure.

Risk: The workflow may automatically modify project state, including repository initialization, baseline commits, project rules, or agent configuration directories.

Mitigation: Require explicit confirmation before git initialization, baseline commits, project AGENTS/CLAUDE/rules file creation, or changes under agent configuration directories.

Risk: Hook and hard-injection examples can alter how future agent sessions behave if copied into active configuration.

Mitigation: Treat hook files as optional examples, validate platform-specific configuration, and keep backups before enabling them.

## Reference(s):

- [Publisher profile](https://clawhub.ai/user/zxc663)
- [Project homepage](https://github.com/zxc663/shisan-xinuo-workflow)
- [Security and rollback reference](references/security.md)
- [Platform adaptation reference](references/platform-adaptation.md)
- [Workflow reference](references/workflows.md)
- [Skill usage reference](references/skill-usage.md)
- [OWASP GenAI LLM Top 10](https://genai.owasp.org/)
- [SLSA](https://slsa.dev/)
- [MCP security best practices](https://modelcontextprotocol.io/docs/draft/tutorials/security/security_best_practices)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, templates, configuration examples, and shell-command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include workflow checklists, project memory templates, risk-review prompts, security-audit prompts, and optional hook configuration examples.]

## Skill Version(s):

1.0.17 (source: ClawHub release evidence; artifact metadata version: 2.9.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
