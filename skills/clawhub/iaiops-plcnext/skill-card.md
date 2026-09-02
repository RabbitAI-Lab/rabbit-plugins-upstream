## Description:

iaiops-plcnext helps agents read PLCnext Control and virtual PLC operational data through built-in OPC-UA and Modbus-TCP services, then diagnose dataflow, downtime, predictive maintenance, OEE, alarms, and baselines with iaiops cross-protocol analysis tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and industrial automation engineers use this skill when an agent needs to inspect PLCnext or virtualized PLC data over OPC-UA or Modbus-TCP, triage operational issues, and summarize industrial data quality, alarms, downtime, and baseline changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is framed as read-only for PLC writes, but listed export, publish, historian push, UNS publish, and compliance evidence bundle workflows could move sensitive operational data.

Mitigation: Require explicit destination approval, local site policy review, and authorized operator confirmation before using any workflow that exports or publishes plant data.

Risk: Agents may use the skill around PLCnext operational data where incorrect summaries or recommendations could affect incident response decisions.

Mitigation: Use outputs as decision support only; review findings against site telemetry, maintenance records, and approved operating procedures before acting.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or text with inline commands and structured analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first skill posture; security evidence notes that export and publish tools may move sensitive plant data outside the environment.]

## Skill Version(s):

0.26.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
