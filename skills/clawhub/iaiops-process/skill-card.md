## Description:

iaiops-process helps agents support process-industry operations across HART-IP, OPC-UA, Modbus, optional MQTT/Sparkplug B UNS, and cross-protocol diagnostics for instrumentation, downtime root cause, data quality, and OEE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and plant engineers use this skill to guide read-first monitoring and diagnosis for chemical, pharmaceutical, food and beverage, and oil and gas process environments spanning HART-IP instruments, OPC-UA/DCS gateways, Modbus devices, and optional UNS/Sparkplug workflows. It is suited to troubleshooting data flow, alarm and downtime causes, tag quality, loop health, and process asset context while requiring review before any write-capable deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read-only safety framing conflicts with documented write, export, publish, and Modbus write-capable paths.

Mitigation: Review before installation in any plant or production-like environment; require explicit approval, dry-run controls, and documented change management for any write-capable action.

Risk: Production control network exposure could occur if historian, export, stream, UNS, or Modbus write paths are enabled before the documentation and tool surface are aligned.

Mitigation: Confirm the exposed tool surface before deployment and avoid connecting to production control networks until the enabled capabilities and controls are clear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-process)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline tool names and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational approval and dry-run guidance for write-capable paths.]

## Skill Version(s):

0.23.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
