## Description:

多代理开发 guides coding agents through multi-agent implementation workflows with task decomposition, fresh subagents, selective parallel execution, and staged specification and code-quality review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate agent-assisted implementation of a prepared development plan, including task decomposition, selective parallelization, subagent handoffs, and staged reviews before branch completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to modify code, run shell commands, coordinate subagents, and affect a repository.

Mitigation: Use it only in a scoped worktree or repository after approving the plan, branch, allowed commands, and files that may be changed.

Risk: The artifact mixes a no-API-key statement with generic API key and external-service guidance.

Mitigation: Do not provide API keys or permit external calls unless the current task explicitly requires them and the user has approved that access.

Risk: Parallel implementation tasks can conflict when they touch the same files or depend on each other.

Mitigation: Run only independent tasks in parallel, serialize shared-file or dependent tasks, and fall back to serial execution if conflicts appear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/multi-agent-dev-v2)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands]

**Output Format:** [Markdown guidance with workflow steps, prompt-template references, review gates, and command-oriented development instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an agent environment with subagent delegation, repository read/write access, shell command capability, Git, and user-approved scope.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
