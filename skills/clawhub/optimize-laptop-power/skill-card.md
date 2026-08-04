## Description: <br>
Windows power-saving reference guide with verifiable commands for balanced plan, Defender tuning, and SysMain. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[frankxpj](https://clawhub.ai/user/frankxpj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Windows laptop users and support engineers use this skill to diagnose battery health, discharge rate, and high-power processes before manually applying reversible Windows power, Defender, and SysMain tuning commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Administrator PowerShell commands can change Windows power, security, and service behavior. <br>
Mitigation: Read each command before running it, execute only the needed steps, record the current power plan GUID, and use the included rollback commands if results are undesirable. <br>
Risk: Defender exclusions reduce real-time scanning for selected paths. <br>
Mitigation: Keep exclusions narrow, choose the paths yourself, and avoid excluding downloads, temporary folders, system directories, or broad drive roots. <br>
Risk: Power plan and SysMain changes may reduce performance or produce different results across Windows devices. <br>
Mitigation: Run the diagnostic checks first, apply one change at a time, compare before-and-after behavior, and revert changes that worsen performance or security posture. <br>


## Reference(s): <br>
- [Optimize-Laptop-Power on ClawHub](https://clawhub.ai/frankxpj/skills/optimize-laptop-power) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline PowerShell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Manual execution only; commands are presented for user review and include rollback guidance.] <br>

## Skill Version(s): <br>
1.3.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
