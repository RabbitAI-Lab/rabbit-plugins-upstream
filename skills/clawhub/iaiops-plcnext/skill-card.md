## Description:

PLCnext/vPLC packaging edition of iaiops for reading PLCnext Control data over built-in OPC-UA and Modbus-TCP servers and routing it into existing diagnostic, downtime, predictive-maintenance, OEE, alarm, baseline, compliance, and program-analysis workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and plant engineers use this skill to route PLCnext Control or virtual PLC tasks through existing OPC-UA and Modbus read, diagnostic, alarm, downtime, OEE, baseline, compliance, and program-analysis workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The claimed read-only scope conflicts with listed export, stream publish, UNS publish, and historian-push capabilities that may move operational data.

Mitigation: Verify which underlying iaiops tools are enabled before deployment, and restrict export, publish, and historian paths unless destinations and data-handling rules are approved.

Risk: Use against unauthorized PLCnext or virtual PLC systems could expose plant data or operational context.

Mitigation: Use the skill only with authorized PLCnext/vPLC systems and approved OPC-UA or Modbus endpoints.

Risk: Operational instructions are primarily in Chinese, which can lead to review or configuration mistakes for teams that cannot read them accurately.

Mitigation: Require an accurate translation or a qualified Chinese-language reviewer before installation and plant use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-plcnext)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline tool names and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include operational diagnostics, data-quality findings, baseline checks, advisory matches, program-analysis summaries, and configuration guidance.]

## Skill Version(s):

0.27.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
