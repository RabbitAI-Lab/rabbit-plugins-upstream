## Description:

Iaiops-plcnext helps agents work with Phoenix Contact PLCnext and virtual PLC telemetry through OPC-UA and Modbus-TCP, with read-first workflows for diagnosis, alarms, baselines, OEE, predictive maintenance, and evidence-oriented investigations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation engineers, and operations teams use this skill when an agent needs to inspect PLCnext Control or virtual PLC process data over OPC-UA or Modbus-TCP, diagnose dataflow and downtime, assess alarms and baselines, or draft onboarding configuration from observed connection facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the skill describes itself as read-only while also listing export, broker publication, historian writes, and local evidence records for operational data.

Mitigation: Install only where PLC telemetry export, broker publication, historian writes, and local evidence records are explicitly allowed; require human approval before transmitting or persisting operational data.

Risk: Industrial control telemetry may be sensitive or operationally material even when the skill is device-read-focused.

Mitigation: Use least-privilege credentials, allowlist destinations, and limit deployments to approved PLC monitoring and evidence-retention workflows.

Risk: If a workflow needs writes or setpoint changes, the artifact says this edition should not perform them directly.

Mitigation: Switch to a write-capable profile only under the documented management-of-change flow with dry-run behavior, undo values, and named approval.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured text with command snippets, configuration drafts, diagnostics, reports, and evidence records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include PLC telemetry summaries, diagnostic findings, onboarding config drafts, compliance evidence bundles, program change baselines, and approval-oriented guidance.]

## Skill Version(s):

0.28.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
