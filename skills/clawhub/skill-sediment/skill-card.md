## Description: <br>
Installs and operates the OpenClaw skill-sediment plugin extension, which turns successful conversations into generated SKILL.md files and can promote them into active skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users and developers use this skill to install, diagnose, repair, recover, configure, and uninstall a plugin that captures useful agent workflows as reusable skills. It is most relevant for controlled workspaces where generated skills can be reviewed before they influence future agent behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installed plugin can observe conversations and create, promote, modify, or delete skill content that may affect future agent behavior. <br>
Mitigation: Install only in a controlled workspace, require an explicit agent scope, and review generated skills before relying on promoted behavior. <br>
Risk: The release security evidence says the plugin can report metadata externally and restart services. <br>
Mitigation: Disable or restrict telemetry and background review where possible, keep restarts explicit unless operationally required, and verify bundle integrity before installation. <br>
Risk: The authoritative security verdict is suspicious because controls and disclosures are broad or unclear for default installation. <br>
Mitigation: Review the security summary before installing, run diagnostics after installation, and avoid use in sensitive or shared workspaces without additional review. <br>


## Reference(s): <br>
- [Skill Sediment ClawHub page](https://clawhub.ai/songhonglei/skills/skill-sediment) <br>
- [Sediment internals troubleshooting reference](references/sediment-internals.md) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands and generated SKILL.md files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can install an OpenClaw plugin that writes pending skills under sediment_skills/ and promotes selected skills into skills/.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence, README changelog, plugin manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
