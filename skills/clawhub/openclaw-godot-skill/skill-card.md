## Description: <br>
Controls Godot 4.x Editor through the OpenClaw Godot Plugin for scene management, node manipulation, input simulation, debugging, editor control, project metadata capture, and screenshots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tomleelive](https://clawhub.ai/user/tomleelive) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to let an agent inspect and control trusted local Godot 4.x projects for scene editing, node operations, gameplay testing, screenshots, logs, and editor state checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify, save, or delete Godot scenes and nodes, and can simulate input in a running project. <br>
Mitigation: Confirm state-changing actions with the user and keep projects under version control or backed up before automation sessions. <br>
Risk: Local bridge ports can allow editor commands if exposed beyond the intended local environment. <br>
Mitigation: Keep local bridge ports bound to localhost and do not expose them on shared or public networks. <br>
Risk: The skill can expose project name, engine version, scene structure, script contents, and viewport screenshots to the connected agent. <br>
Mitigation: Use only with trusted local projects and avoid projects whose contents must not leave the machine. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tomleelive/skills/openclaw-godot-skill) <br>
- [OpenClaw Godot Skill Homepage](https://github.com/TomLeeLive/openclaw-godot-skill) <br>
- [OpenClaw Godot Plugin](https://github.com/TomLeeLive/openclaw-godot-plugin) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown guidance with inline shell commands and Godot tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can issue explicit Godot editor control actions through godot_execute, including state-changing operations.] <br>

## Skill Version(s): <br>
1.2.10 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
