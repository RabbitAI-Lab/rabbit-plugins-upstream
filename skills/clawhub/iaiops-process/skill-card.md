## Description:

Process-industry edition of iaiops for process plants that supports read-first HART-IP, OPC-UA, Modbus TCP/RTU, optional MQTT/Sparkplug B UNS, and cross-protocol diagnostics for downtime root cause, data quality, and OEE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and process or plant engineers use this skill to configure agents for read-first diagnostics across HART-IP, OPC-UA, Modbus, and optional Sparkplug/UNS data in chemical, pharma, food and beverage, and oil and gas plants. It helps triage downtime, data quality, alarm behavior, asset inventory, compliance evidence, and change baselines while keeping production writes behind MOC approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write, export, publish, and historian-write capabilities may be enabled in high-impact industrial or plant-connected environments.

Mitigation: Review before production installation, run under a restricted account, and disable or protect export, publish, and historian-write tools with explicit approval gates unless the site intends to use them.

Risk: Unpinned dependencies or uncontrolled package sources can increase supply-chain risk for plant-connected deployments.

Mitigation: Require pinned packages or an internal artifact repository before installing in production or plant-connected environments.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands, configuration snippets, and structured diagnostic summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference plant process data, protocol reads, and approval-gated publish or export actions depending on enabled tools.]

## Skill Version(s):

0.28.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
