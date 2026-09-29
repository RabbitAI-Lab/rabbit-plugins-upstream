## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to run explicitly requested task and project loops with progress updates, verification, revisions, and human approval before sensitive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can create workspace queues, runtime artifacts, dashboard services, gateway coupling, and scheduled wakeups.

Mitigation: Review the installation plan and destination before confirming writes; use a pinned package version or vetted source checkout in sensitive environments.

Risk: Exposing the dashboard can make loop controls reachable over a network.

Mitigation: Keep dashboard access local or protect network access with appropriate controls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm package commands](references/npm-package.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown status reports and setup guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task and project status with verification evidence and next actions]

## Skill Version(s):

0.15.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
