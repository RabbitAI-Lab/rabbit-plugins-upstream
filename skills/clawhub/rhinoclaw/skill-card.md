## Description: <br>
Control Rhino 3D via the RhinoClaw plugin over TCP to create, modify, query, measure, render, manage layers and materials, run Boolean and transform operations, drive Grasshopper definitions, work with VisualARQ BIM objects, or batch multiple steps as one atomic operation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mcmuff86](https://clawhub.ai/user/mcmuff86) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, designers, and automation agents use RhinoClaw to control a Rhino 7/8 session for model creation and editing, scene inspection, rendering, Grasshopper workflows, VisualARQ BIM tasks, and file import or export. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent powerful live control over Rhino documents, including destructive edits. <br>
Mitigation: Use it only with a Rhino host you control, keep backups of active models, and require explicit approval before clear, delete, save, open, export, or large batch operations. <br>
Risk: The skill can execute arbitrary Rhino Python or native Rhino commands. <br>
Mitigation: Prefer typed helpers and allowlisted commands, and require explicit approval before arbitrary Python or native command execution. <br>
Risk: TCP control can affect an unintended Rhino session if connection settings are wrong. <br>
Mitigation: Run preflight first, use an auth token, and point RHINOCLAW_HOST and RHINOCLAW_PORT only at the intended Rhino server. <br>


## Reference(s): <br>
- [RhinoClaw command reference](references/commands.md) <br>
- [ClawHub RhinoClaw listing](https://clawhub.ai/mcmuff86/skills/rhinoclaw) <br>
- [RhinoCommon API](https://developer.rhino3d.com/api/rhinocommon/) <br>
- [Rhino.Python guide](https://developer.rhino3d.com/guides/rhinopython/) <br>
- [rhinoscriptsyntax index](https://developer.rhino3d.com/api/RhinoScriptSyntax/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline Python, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Rhino 7/8 and a RhinoClaw plugin server; commands may modify live Rhino documents.] <br>

## Skill Version(s): <br>
0.7.2 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
