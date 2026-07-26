## Description: <br>
PLCnext and virtualized-PLC edition of iaiops that guides agents through read-first OPC-UA and Modbus diagnostics, cross-protocol analysis, and industrial data workflows for Phoenix Contact PLCnext environments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and industrial automation engineers use this skill to route agents toward read-first PLCnext Control and vPLC diagnostics over built-in OPC-UA and Modbus-TCP services. It is suited for connection diagnosis, dataflow triage, downtime root cause analysis, predictive maintenance, OEE, alarm, baseline, and compliance workflows using existing iaiops tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unintended access to PLCnext endpoints or operational data destinations. <br>
Mitigation: Before installation or use, confirm the iaiops MCP tools are configured only for intended PLCnext endpoints and that export, historian, streaming, baseline, and alias-map destinations are approved for the operational data involved. <br>
Risk: Write-capable profiles could enable controlled changes outside this read-first edition. <br>
Mitigation: Keep write-capable profiles disabled unless controlled changes are explicitly required; when enabled, apply the documented approval, dry-run, undo, and change-management controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-plcnext) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown instructions with tool names and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-first PLCnext OPC-UA and Modbus workflow guidance; no new connector or PLCnext vendor SDK is introduced by the skill text.] <br>

## Skill Version(s): <br>
0.19.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
