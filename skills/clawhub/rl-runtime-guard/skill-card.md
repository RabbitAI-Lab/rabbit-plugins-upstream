## Description:

Pre-tool-call runtime guardrails for AI agents that add soft prompt reminders for complex tasks, retry loops, and tool or path mismatches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huanmeng9527](https://clawhub.ai/user/huanmeng9527)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add advisory runtime checks to multi-step coding agents before tool calls. It helps surface likely retry loops, complex-task overload, and platform path or command-size issues without blocking execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can alter prompt flow by inserting advisory system messages before tool use.

Mitigation: Install only when advisory guardrails are desired, review threshold settings, and test agent behavior before production rollout.

Risk: Audit logging can create local telemetry that may matter for privacy, debugging, or compliance workflows.

Mitigation: Keep audit logging disabled unless needed, use metadata-only logging in v1.0.5, protect enabled logs with restrictive permissions, and avoid deleting logs that may be required later.

Risk: Default thresholds may not match every deployment and can produce missed reminders or unnecessary prompt overhead.

Mitigation: Tune thresholds using the bundled threshold guide and disable the guard by environment variable or configuration when benchmarking or troubleshooting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huanmeng9527/skills/rl-runtime-guard)
- [Threshold Tuning Guide](references/thresholds.md)
- [How to Disable rl-runtime-guard](references/disabling.md)
- [Audit Log](references/audit-log.md)
- [Companion skill: claw-rl-prm-judge](https://github.com/huanmeng9527/claw-rl-prm-judge)
- [OpenClaw docs](https://docs.openclaw.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON configuration examples and JavaScript handler references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Soft prompt augmentation; audit logging is opt-in and records metadata only when enabled.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
