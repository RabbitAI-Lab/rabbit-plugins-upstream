## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering operators use this skill to run explicit task and project loops with queueing, verification, progress reporting, revision handling, and governed completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer or runtime actions may affect the wrong workspace, queue, worker agent, service, or dashboard listen mode if the plan is not reviewed.

Mitigation: Review the generated installation plan before confirming writes, then run the relevant doctor and smoke checks before using a real task.

Risk: Tailnet dashboard access relies on Tailscale ACLs rather than an application login.

Mitigation: Use the default localhost dashboard binding unless Tailnet access is appropriate for the environment and its Tailscale ACL boundary.

Risk: A dispatcher or worker exit code alone can give a misleading impression that a loop completed successfully.

Mitigation: Inspect task artifacts, acceptance reviews, verification evidence, and final judgement before reporting completion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm package reference](artifact/references/npm-package.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes queue status, verification guidance, installation plans, and confirmation-gated operational steps.]

## Skill Version(s):

0.15.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
