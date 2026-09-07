## Description:

Soft, opt-in runtime guardrails for AI agents that inject advisory reminders before each request without blocking requests or modifying tool output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huanmeng9527](https://clawhub.ai/user/huanmeng9527)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to add advisory runtime reminders when agents repeat user requests, face long multi-step tasks, or receive platform-mismatched paths. It is a soft first line of defense before offline quality review or stricter guardrail enforcement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The hook can add high-priority advisory instructions to agent requests and may steer behavior when a guard fires.

Mitigation: Install only where advisory prompt augmentation is acceptable, review the guard prompts before deployment, and use RL_GUARD_DISABLED=1 for testing or incident response.

Risk: One advertised file-based off switch depends on the host integration loading config, and the security evidence says that path is not implemented in the included default hook.

Mitigation: Verify the OpenClaw integration actually loads config before relying on file-based disable or threshold settings; prefer the environment variable disable path for immediate control.

Risk: Default thresholds are calibrated for workstation usage and may create false positives or missed reminders in cloud, sandbox, or high-stakes deployments.

Mitigation: Tune thresholds with the bundled threshold guide and validate behavior with opt-in audit logs before production use.

Risk: Audit logging creates local telemetry when explicitly enabled.

Mitigation: Keep audit logging disabled unless needed, avoid storing raw prompts, and restrict permissions on the audit log file when telemetry is enabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huanmeng9527/skills/rl-runtime-guard)
- [Threshold tuning guide](references/thresholds.md)
- [Disable guide](references/disabling.md)
- [Audit log guide](references/audit-log.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON configuration examples and JavaScript hook code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory prompt augmentation only; no network access or external dependencies are described in the artifact.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
