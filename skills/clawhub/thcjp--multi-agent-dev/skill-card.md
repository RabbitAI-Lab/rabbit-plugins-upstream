## Description:

多代理开发框架 guides an agent to execute implementation plans by decomposing tasks, dispatching fresh subagents, coordinating selective parallel work, and applying staged specification and code-quality review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to coordinate multi-task software implementation from a clear plan, including task decomposition, subagent execution, staged review, testing, and completion of a development branch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to read repository files, edit code, run commands or tests, coordinate subagents, and create commits.

Mitigation: Install only in repositories where active coding automation is intended; use a worktree or sandbox, review generated changes, and require tests before merge.

Risk: Server security evidence flags a pure-Markdown classification mismatch around write and execution authority.

Mitigation: Treat the skill as an active coding workflow, not passive documentation, and review its behavior before installation.

Risk: The artifact mentions callback URLs and API-key configuration that may expose data if used without review.

Mitigation: Avoid callback URLs and API keys unless required, scope any credentials narrowly, and check what data the agent may send.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/multi-agent-dev)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code, command, review, and workflow instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to read files, edit code, run tests or commands, coordinate subagents, and produce review notes or commits.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
