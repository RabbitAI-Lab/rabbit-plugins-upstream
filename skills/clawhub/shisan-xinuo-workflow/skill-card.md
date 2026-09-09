## Description:

Shisan Xinuo Workflow is an auditable engineering workflow for coding agents that routes hands-on engineering tasks through L1, L2-S, or L2-F tracks with quality gates, rollback discipline, project memory, and platform-adaptable rule injection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zxc663](https://clawhub.ai/user/zxc663)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to impose repeatable workflow governance on coding agents for implementation, refactoring, bug fixing, reviews, project memory, and quality-gate handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent instruction installation can affect future agent sessions or project rules.

Mitigation: Install only when persistent workflow governance is intended; prefer on-demand injection and review every target path before writing.

Risk: Automatic project rule, memory, or configuration file creation can modify a working tree.

Mitigation: Use a scoped workspace, inspect diffs before accepting changes, and avoid global hard injection unless future-session behavior should change.

Risk: Hook templates can run session-start or session-end commands if enabled.

Mitigation: Inspect and pin hook scripts before enabling them, and keep hook templates disabled when platform behavior has not been verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zxc663/skills/shisan-xinuo-workflow)
- [GitHub project homepage](https://github.com/zxc663/shisan-xinuo-workflow)
- [Workflow and quality gates](references/workflows.md)
- [Platform adaptation](references/platform-adaptation.md)
- [Injection core](references/injection-core.md)
- [Security and rollback](references/security.md)
- [Work discipline rules](references/rules.md)
- [Hook templates](templates/hooks/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with templates, command examples, configuration snippets, and review checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation or updates of project rule files, memory files, plans, task records, hook examples, and sub-agent prompts.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; skill metadata version 2.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
