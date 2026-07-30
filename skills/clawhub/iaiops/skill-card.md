## Description: <br>
iaiops routes industrial and operational technology tasks to the appropriate edition skill and MCP profile for governed reads, diagnostics, analytics, and gated writes across PLCs, controllers, machine tools, IIoT brokers, facilities systems, and related protocols. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and operations teams use iaiops to route industrial protocol, PLC, SCADA, HMI, historian, CNC, IIoT, OEE, downtime, and OT asset inventory requests to the smallest suitable edition skill and MCP profile. The skill emphasizes read-first workflows and requires dry-run, approval, and double-confirmation safeguards before high-impact writes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Industrial and operational technology workflows can include high-impact write actions. <br>
Mitigation: Keep write actions in dry-run unless formally approved, use named approval with double confirmation, and review undo-value handling before enabling production writes. <br>
Risk: Overbroad MCP profiles can expose more protocol tools than a task requires. <br>
Mitigation: Configure the smallest MCP profile that covers the site protocol or workflow, and use read-first diagnostics before any write path. <br>
Risk: Credentials, approvals, and undo values may be sensitive in OT environments. <br>
Mitigation: Review how the backing MCP server stores encrypted credentials, approvals, and undo values in the deployment environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes users to edition skills and MCP profiles; write actions are described as dry-run, approval-gated, and double-confirmed.] <br>

## Skill Version(s): <br>
0.20.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
