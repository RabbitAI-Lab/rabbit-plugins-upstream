## Description: <br>
Automate TIA Portal via Openness API for PLC project engineering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and PLC engineers use this skill to operate TIA Portal V21 Openness workflows for creating or opening projects, exporting and importing SCL blocks, and compiling PLC projects from an agent-assisted workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to run elevated PowerShell and may use ExecutionPolicy Bypass. <br>
Mitigation: Install and run it only on an authorized TIA Portal engineering workstation, review the PowerShell script before execution, and avoid ExecutionPolicy Bypass unless the operator understands why it is needed. <br>
Risk: The workflow can automate PLC project create, import, save, and compile actions. <br>
Mitigation: Confirm project paths before create, import, or save actions and keep backups of PLC projects before running the workflow. <br>
Risk: The setup may require adding users to the Siemens TIA Openness local group. <br>
Mitigation: Grant Siemens TIA Openness group membership only with appropriate approval and remove access when it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/tia-portal-openness) <br>
- [Publisher profile](https://clawhub.ai/user/paudyyin) <br>
- [Environment configuration reference](references/env.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with PowerShell commands and PLC engineering guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may guide updates to env.json and TIA Portal project files when executed on an authorized engineering workstation.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
