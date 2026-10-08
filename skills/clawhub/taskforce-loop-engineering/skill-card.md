## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users explicitly invoking a task or project loop use this skill to coordinate queued work, track progress, verify outcomes, and manage revisions and approval gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the CLI or integration can change workspace files, scheduler configuration, and dashboard availability.

Mitigation: Trust and pin a reviewed package version; inspect the installation plan and confirm changes only for the intended workspace and host account.

Risk: An active loop may perform work beyond what the user intended.

Mitigation: Require explicit loop invocation and separate approval for external communication, destructive actions, sensitive changes, and spending beyond an established budget.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm Package](artifact/references/npm-package.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task status, verification evidence, and next actions.]

## Skill Version(s):

0.15.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
