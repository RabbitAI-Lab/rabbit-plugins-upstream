## Description: <br>
Helps agents support Unity3D game development workflows, including scene management, script generation, asset optimization, automated builds, and debugging or testing guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cx75227-ops](https://clawhub.ai/user/cx75227-ops) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical artists use this skill to coordinate Unity Editor workflows through an agent, including inspecting scenes, generating C# scripts and templates, managing play mode, and starting builds. It is best used in a version-controlled Unity project where generated code and editor actions can be reviewed before commit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unauthenticated local Unity Editor bridge commands can modify projects, create scripts, delete objects, and start builds. <br>
Mitigation: Use the skill only in a version-controlled Unity project, start the bridge only when needed, stop it afterward, and review generated scripts or build actions before saving or committing. <br>
Risk: Generated Unity code, templates, or editor actions may introduce incorrect behavior or unwanted project changes. <br>
Mitigation: Review and test generated C# scripts, scene changes, and build settings before integrating them into production branches. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cx75227-ops/skills/unity3d-game-dev) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, PowerShell examples, C# code, and JSON responses from local bridge actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or invoke local Unity Editor bridge actions that modify project files, scenes, play mode, and builds.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
