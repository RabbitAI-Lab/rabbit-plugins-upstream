## Description: <br>
iaiops routes industrial and OT tasks to the appropriate edition skill and MCP profile for vendor-neutral, read-first diagnostics, analytics, and gated writes across PLCs, controllers, machine tools, IIoT brokers, building systems, and fab equipment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, OT engineers, and industrial operations teams use this skill to route protocol-specific troubleshooting, OEE and downtime analysis, asset inventory, and data-quality tasks to the correct iaiops edition skill and MCP profile. The skill is intended for authorized industrial environments and starts with read-only diagnostics before any gated write path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can route users toward high-impact write operations on industrial or OT systems. <br>
Mitigation: Use only with authorized systems, keep profiles narrowly scoped, begin with read-only diagnostics, and require formal change control, dry-run review, human approval, and rollback planning before real writes. <br>
Risk: Incorrect or overconfident troubleshooting guidance in OT environments could lead to unsafe operational decisions. <br>
Mitigation: Treat AI conclusions as advisory, cite real signal sources where available, and report insufficient evidence instead of guessing. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with routing tables and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes users to scoped MCP profiles and emphasizes read-first diagnostics, dry-run behavior, approval gates, and rollback planning for writes.] <br>

## Skill Version(s): <br>
0.20.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
