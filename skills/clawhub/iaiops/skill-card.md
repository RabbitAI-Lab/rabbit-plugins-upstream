## Description: <br>
iaiops routes industrial and OT troubleshooting tasks to edition skills and MCP profiles for read-first data access, diagnostics, analytics, and gated control actions across supported protocols. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, controls engineers, and OT operators use this skill to route industrial protocol, PLC, SCADA, historian, CNC, IIoT, OEE, downtime, and asset-inventory requests to the right iaiops edition and MCP profile. It is intended for authorized industrial environments where read-only investigation is the default and writes require formal change approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unauthorized or incorrect write actions against industrial control systems could affect operations or safety. <br>
Mitigation: Install only where the user is authorized to inspect or control OT systems, keep workflows read-only by default, and require formal change approval with dry-run, double confirmation, undo capture, and enforcement checks before any write. <br>
Risk: Troubleshooting conclusions can be misleading when industrial signal evidence is incomplete or stale. <br>
Mitigation: Require outputs to cite observed signal sources and prefer an insufficient-evidence result when the available data does not support a conclusion. <br>


## Reference(s): <br>
- [ClawHub iaiops skill page](https://clawhub.ai/zw008/skills/iaiops) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes agent tasks to edition skills and MCP profiles; does not itself expose tool definitions.] <br>

## Skill Version(s): <br>
0.22.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
