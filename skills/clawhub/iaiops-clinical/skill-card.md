## Description:

iaiops-clinical helps agents inspect hospital facilities systems across BACnet/IP, Modbus, and OPC-UA, with checks for isolation-room pressure, medical-gas pressure, OR environment, alarms, data quality, and facilities root-cause analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Hospital facilities engineers and authorized agent operators use this skill to collect and analyze BMS, SCADA, and field-device evidence for patient-safety-adjacent checks and operational triage. It is suited for controlled clinical-facility environments where BACnet writes, exports, and publishing destinations are explicitly authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server security evidence flags a mismatch between read-only positioning and documented write, export, and publishing capabilities in a safety-sensitive clinical-facility context.

Mitigation: Install only where BACnet writes, exports, and publishing destinations are explicitly authorized, segregated from life-safety systems where appropriate, and backed by runtime approval, audit logging, and pinned dependency provenance.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/iaiops-clinical)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or structured text with tool-call guidance, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include readout summaries, safety-check findings, dry-run write plans, approval guidance, export instructions, or publishing configuration depending on the requested workflow.]

## Skill Version(s):

0.28.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
