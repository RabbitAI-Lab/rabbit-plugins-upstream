## Description:

Helps process-plant engineers inspect HART-IP, OPC-UA, and Modbus data and investigate instrument health, downtime, data quality, and OEE with read-first workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Process-plant engineers and operators use the skill to diagnose instrumentation and data-flow issues, investigate downtime, and review equipment performance across industrial protocols.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing, historian pushes, or exports could affect operational systems or disclose plant data despite the read-first workflow.

Mitigation: Require named approval, dry-run defaults, permitted destinations, and audit logging before enabling these actions on live plant data.

Risk: Incomplete or unverified instrument data could lead to misleading diagnostic conclusions.

Mitigation: Review cited measurements and data gaps with plant personnel; verify gateway connectivity and field behavior before acting on findings.

## Reference(s):

- [iaiops-process on ClawHub](https://clawhub.ai/zw008/skills/iaiops-process)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Diagnostic findings and operational guidance in text or Markdown, with commands and configuration drafts where applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings may include measured values, source references, confidence limits, and stated data gaps.]

## Skill Version(s):

0.29.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
