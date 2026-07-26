## Description: <br>
Iaiops routes industrial and OT troubleshooting tasks to the appropriate edition skill and MCP profile for read-first diagnostics, analytics, and gated writes across PLC, SCADA, machine tool, IIoT, building, and fab protocols. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and OT engineers use Iaiops to select the right industrial protocol profile, inspect configured endpoints, run diagnostics, and prepare governed dry-run write actions for authorized control systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can route users toward high-impact write-capable OT operations. <br>
Mitigation: Use it only with authorized OT systems, keep credentials narrowly scoped, and require dry-run plus approval controls before any production write. <br>
Risk: A broad MCP profile can expose more protocol tools than needed for a site. <br>
Mitigation: Select the narrowest MCP profile that covers the target equipment or protocol before starting diagnostic work. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes users toward narrower MCP profiles and emphasizes read-first, dry-run, and approval-controlled operation for write-capable OT actions.] <br>

## Skill Version(s): <br>
0.19.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
