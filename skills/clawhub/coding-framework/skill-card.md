## Description: <br>
Orchestrates coding workflows across stage detection, design gates, implementation, review, verification, iteration, and worktree-based task management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to structure programming work, route tasks through specialized review agents, run verification loops, and manage plans, specs, iterations, and Git worktrees. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents to run local commands and delegate execution to review or workflow agents. <br>
Mitigation: Install only in environments where broad local command execution is acceptable, and keep approval gates or sandboxing enabled for command execution. <br>
Risk: Server security evidence flags unsafe command construction, including a shell=True validation gate. <br>
Mitigation: Fix or disable the shell=True validation path before relying on the skill for unattended workflows. <br>
Risk: Persistent audit logs, workflow state, rollback behavior, and worktree cleanup may expose private task data or remove local work. <br>
Mitigation: Review log paths, retention, rollback, and cleanup behavior against privacy and data-loss expectations before deployment. <br>
Risk: Static review agents may have exec capability. <br>
Mitigation: Restrict or remove exec permissions from static review agents unless command execution is explicitly needed. <br>


## Reference(s): <br>
- [Coding Framework ClawHub Page](https://clawhub.ai/paudyyin/skills/coding-framework) <br>
- [Agent System](references/agent-system.md) <br>
- [Hook System](references/hook-system.md) <br>
- [Workflow Examples](references/workflow-examples.md) <br>
- [Security Patterns Detail](references/security-patterns-detail.md) <br>
- [Git Worktree Guide](references/worktree-guide.md) <br>
- [TDD Anti-Patterns](references/tdd-anti-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline command examples, generated plan/spec files, JSON workflow state, and shell command suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local workflow files, logs, specs, plans, DAG state, and Git worktrees when the agent follows the skill's workflows.] <br>

## Skill Version(s): <br>
12.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
