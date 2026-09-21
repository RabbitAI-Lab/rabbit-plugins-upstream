## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate durable task and project loops for agent work, including queueing, verification, revision handling, progress reporting, and governed completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Durable loop orchestration can add persistent queue, scheduler, dashboard, or service behavior to a workspace.

Mitigation: Install only in the intended workspace, review the generated install plan before confirmation, and run doctor and smoke checks before enabling scheduler or service setup.

Risk: An unpinned or unreviewed npm package install could introduce unexpected CLI behavior.

Mitigation: Pin or otherwise verify the npm package version before installation and prefer read-only help or plan commands before mutable operations.

Risk: Dashboard exposure beyond localhost may depend on Tailnet ACLs rather than application-level login.

Mitigation: Keep the dashboard bound to localhost unless Tailnet access controls are explicitly acceptable for the deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm Package Reference](references/npm-package.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce installation plans, status summaries, verification commands, and risk-aware next steps; mutable operations are gated by explicit confirmation.]

## Skill Version(s):

0.15.19 (source: server release metadata and npm package reference)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
