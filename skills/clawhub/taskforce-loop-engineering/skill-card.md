## Description:

Document complete Loop Engineering install, upgrade, scheduler, and verification lifecycle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they explicitly invoke Loop Engineering to install, upgrade, verify, or run managed task queues and OpenClaw scheduler integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading Loop Engineering may add workspace files and user-level systemd timers.

Mitigation: Review the npm package and read-only installer plan before confirmation, then run doctor and smoke checks and verify the scheduler status.

Risk: Loop execution can enqueue and run task work in a workspace when explicitly invoked.

Mitigation: Require explicit loop language, preserve the requested scope, inspect run artifacts, and require separate confirmation for destructive actions, credential changes, production deployment, outreach, paid usage, or device instrumentation.

Risk: A missing CLI, integration, or scheduler heartbeat can leave Loop Engineering only partially installed or upgraded.

Mitigation: Check the installed CLI and integration before running loop commands, and treat scheduler_missing or stale heartbeat evidence as an incomplete upgrade.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [GitHub repository listed by skill artifact](https://github.com/ambitioncn/taskforce-loop-engineering)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes explicit confirmation gates, scheduler checks, and verification guidance for Loop Engineering operations.]

## Skill Version(s):

0.8.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
