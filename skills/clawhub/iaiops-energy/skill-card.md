## Description: <br>
iaiops-energy routes agents to a read-only MCP server for utility SCADA telemetry over IEC 60870-5-104, DNP3/IEEE 1815, and IEC 61850 MMS, with substation event analysis and cross-protocol diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to read-only substation telemetry, run protocol status checks, perform monitored-point reads or integrity polls, and analyze utility SCADA data without exposing control operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live substation endpoints and telemetry links are sensitive operational environments. <br>
Mitigation: Install and run the skill only in authorized environments and test against non-production or approved endpoints first. <br>
Risk: The release depends on an external pip package source. <br>
Mitigation: Confirm the package source is trusted before installation. <br>
Risk: IAIOPS_MASTER_PASSWORD unlocks the secret store. <br>
Mitigation: Keep IAIOPS_MASTER_PASSWORD in a secret manager and do not place it in chat or static configuration. <br>
Risk: Read-only interrogations and integrity polls can still create traffic on operational links. <br>
Mitigation: Use the documented doctor-first workflow and approved targets before deeper reads. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-energy) <br>
- [Publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only telemetry and analysis workflows; no control commands are exposed.] <br>

## Skill Version(s): <br>
0.1.12 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
