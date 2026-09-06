## Description:

Water-treatment edition of iaiops for waterworks, wastewater plants, and pump stations, covering Modbus-TCP/RTU, OPC-UA, HART-IP instrumentation, downtime root-cause analysis, data quality checks, and OEE workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, industrial engineers, and plant operations teams use this skill to inspect water-treatment telemetry, diagnose dataflow and downtime issues, assess water-quality thresholds, and produce operational analysis across Modbus, OPC-UA, and HART-IP sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags a mismatch between read-only claims and advertised export, publish, push, and stream capabilities in an industrial operations context.

Mitigation: Install only where outbound actions are acceptable, network-scoped, logged, and subject to explicit operator approval.

Risk: The skill may be used near plant or OT-connected environments where incorrect guidance or unexpected outbound activity can affect operational risk.

Mitigation: Review before installation in plant environments and require human review before any action that could publish, export, or push operational data.

Risk: HART-IP real gateway support is marked as needing verification in the artifact.

Mitigation: Validate HART-IP behavior against the target gateway before relying on live instrumentation results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-water)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with tool names, configuration snippets, command examples, and structured operational findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should cite input readings, thresholds, baselines, source files, advisory records, or operator-declared relationships where the skill behavior requires evidence.]

## Skill Version(s):

0.27.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
