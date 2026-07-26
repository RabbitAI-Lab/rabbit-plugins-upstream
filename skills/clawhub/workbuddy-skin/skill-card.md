## Description: <br>
Build, modify, debug, and publish a Windows WorkBuddy Skin Studio desktop skinning tool using Tauri v2 and Rust. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pddsa](https://clawhub.ai/user/pddsa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create and package a Windows GUI skinning tool for WorkBuddy, including theme application, WorkBuddy path handling, local CDP style injection, custom skin workflows, and NSIS installer builds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local CDP-based styling workflow can restart WorkBuddy and affect active user work. <br>
Mitigation: Warn users to save work before applying themes and keep CDP access limited to 127.0.0.1. <br>
Risk: Generated app code or installer packaging could include unintended behavior before distribution. <br>
Mitigation: Review generated app code before distributing an installer and run the documented build checks. <br>
Risk: Changing WorkBuddy installation files could damage the application or bypass expected integrity boundaries. <br>
Mitigation: Do not modify WorkBuddy app.asar, installation directories, or signature files; use the local styling and packaging workflow only. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pddsa/skills/workbuddy-skin) <br>
- [Server-resolved GitHub provenance](https://github.com/PDDsa/WorkBuddy-skin) <br>
- [Publisher profile](https://clawhub.ai/user/pddsa) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code, JSON, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides local Windows WorkBuddy skin-tool development, packaging, and safety checks.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
