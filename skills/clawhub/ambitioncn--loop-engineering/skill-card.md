## Description: <br>
Loop Engineering v0.6 with lifecycle tools, explainable drift, live progress, amendments, supersede routing, workers, and gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ambitioncn](https://clawhub.ai/user/ambitioncn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when they explicitly want loop-managed task execution with preflight checks, queue routing, progress reporting, review artifacts, and gated repair or code-worktree handoffs in a trusted workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can execute workspace commands and manage queue artifacts. <br>
Mitigation: Use it only in trusted workspaces, keep queues scoped, and review loop configs and dispatcher commands before execution. <br>
Risk: Patch application, cleanup, cron, notifications, external sends, publishing, destructive commands, production config changes, memory operations, and credential changes can have high impact. <br>
Mitigation: Require the documented confirmation gates and separate approval before taking those actions. <br>
Risk: Live instrumentation or process-control work can leave child processes running after timeouts. <br>
Mitigation: Stop at artifacts and human review unless execution is explicitly approved, terminate the process group on timeout, and verify no child instrumentation or proxy process remains. <br>


## Reference(s): <br>
- [npm Package](references/npm-package.md) <br>
- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/loop-engineering) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration examples, and local artifact paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces read-only plans, status summaries, queue/worktree review artifacts, patch handoff commands, and confirmation-gated execution guidance.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
