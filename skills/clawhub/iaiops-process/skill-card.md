## Description:

Helps process-plant engineers inspect industrial instrumentation and telemetry, assess data quality and downtime, and investigate equipment issues across HART-IP, OPC UA, and Modbus.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Process-plant engineers and operators use this skill to read instrumentation and control-system telemetry, triage alarms and data-quality issues, and investigate downtime without making unapproved control changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Industrial telemetry and operations files may contain sensitive plant information.

Mitigation: Use only in approved environments and restrict IAIOPS_AGENT_READ_DIRS and IAIOPS_AGENT_WRITE_DIRS to authorized locations.

Risk: Optional publishing can affect production data flows.

Mitigation: Keep publishing behind the documented dry-run and named-approval workflow; do not authorize production writes without operator review.

## Reference(s):

- [iaiops-process on ClawHub](https://clawhub.ai/zw008/skills/iaiops-process)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Configuration instructions]

**Output Format:** [Text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first diagnostics; optional publishing requires approval.]

## Skill Version(s):

0.32.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
