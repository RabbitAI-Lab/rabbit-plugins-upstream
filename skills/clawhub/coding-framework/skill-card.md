## Description: <br>
Orchestrates coding workflows with stage detection, planning, implementation, testing, review, hook-based checks, and iterative development patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to structure software work through stage detection, planning, implementation, testing, review, hook-based checks, and iterative workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad local command execution can affect files, tools, or the host environment. <br>
Mitigation: Use the skill in a clean repository or sandbox and review command-producing workflows before execution. <br>
Risk: Automatic Git and worktree mutation paths can change repository state unexpectedly. <br>
Mitigation: Keep auto-commit and auto-rollback disabled by default, and require explicit approval before cleanup, checkout, or other state-changing Git actions. <br>
Risk: External-agent, push, and pull-request workflows may delegate work or write to remote systems. <br>
Mitigation: Review each external-agent or remote-write workflow before use and require approval gates before push or pull-request actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/coding-framework) <br>
- [Agent System](artifact/references/agent-system.md) <br>
- [Hook System](artifact/references/hook-system.md) <br>
- [Iteration Patterns](artifact/references/iteration-patterns.md) <br>
- [External Agents](artifact/references/external-agents.md) <br>
- [Security Patterns Detail](artifact/references/security-patterns-detail.md) <br>
- [Worktree Guide](artifact/references/worktree-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with code snippets, shell commands, and structured review output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May coordinate local scripts, hooks, agent definitions, and Git worktree workflows.] <br>

## Skill Version(s): <br>
13.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
