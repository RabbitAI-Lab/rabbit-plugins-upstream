## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route explicit loop requests into durable task or project workflows with queueing, verification, revision handling, progress notifications, and governed completion criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to install or execute an external CLI package without a pinned version.

Mitigation: Review the package and repository first, prefer a pinned package version or audited commit, and avoid global or npx execution in sensitive environments.

Risk: Queue workers, schedulers, notifications, or workspace-changing commands may affect the wrong workspace or route results to the wrong destination.

Mitigation: Use plan-only installation, confirm workspace, queue, worker identity, and routing destination, then run doctor and smoke checks before enabling writes or schedulers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/loop-engineering)
- [npm package reference](references/npm-package.md)
- [Taskforce Loop Engineering repository](https://github.com/ambitioncn/taskforce-loop-engineering)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command blocks and structured status or verification references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents through deployment checks, queue operations, project intake, verification, revision handling, and completion reporting.]

## Skill Version(s):

0.15.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
