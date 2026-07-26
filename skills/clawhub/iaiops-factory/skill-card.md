## Description: <br>
Iaiops Factory helps agents inspect and troubleshoot discrete-manufacturing systems across PLC, CNC, fieldbus, MES/SCADA, MQTT/Sparkplug B, and Unified Namespace workflows with read-first diagnostics and approval-gated writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, controls engineers, and industrial operations teams use this skill to browse tags, diagnose connectivity and dataflow, analyze downtime and OEE, inventory assets, and prepare controlled write actions for factory production lines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact write tools could affect production control equipment if used without authorization. <br>
Mitigation: Keep write tools disabled unless a formal MOC or approval workflow is active, require dry-run review first, and preserve rollback or undo information before any approved change. <br>
Risk: EtherCAT and PROFINET operations may require raw-socket or privileged network access. <br>
Mitigation: Run the skill only in environments where the agent is authorized to inspect industrial systems, and limit privileged access to the required dedicated industrial network interface. <br>
Risk: SCADA API tokens, MQTT publish access, and PLC write functions can create operational impact if over-scoped or misused. <br>
Mitigation: Use scoped credentials from a secret store, prefer read-only tokens where possible, and audit write-capable actions across MCP and CLI use. <br>


## Reference(s): <br>
- [Iaiops Factory on ClawHub](https://clawhub.ai/zw008/skills/iaiops-factory) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and structured tool-use guidance with inline commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include read-first diagnostics, evidence-linked analysis, dry-run write plans, and rollback notes.] <br>

## Skill Version(s): <br>
0.19.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
