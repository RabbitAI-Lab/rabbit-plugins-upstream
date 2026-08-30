## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to route explicit loop requests into durable task or project queues with verification, revisions, live progress, and governed human gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent task or project automation may continue work beyond a single chat turn.

Mitigation: Install and enable it only when a durable queue is intended, and review generated plans and queue state before confirming execution or scheduler setup.

Risk: Dashboard exposure, notification routing, systemd services, patch application, and cleanup can affect the local environment.

Mitigation: Use the documented plan and doctor workflows first, keep dashboard access scoped, and require explicit confirm flags for higher-impact actions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [Official GitHub repository](https://github.com/ambitioncn/taskforce-loop-engineering)
- [npm Package](references/npm-package.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes verification steps, confirmation-gated actions, queue and project status guidance, and operational safety checks.]

## Skill Version(s):

0.15.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
