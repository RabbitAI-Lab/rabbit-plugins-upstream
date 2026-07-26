## Description: <br>
Generate and export basic 3D models using Blender CLI scripting, including object creation, scaling, positioning, and .obj/.blend exports in background mode. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rong-da](https://clawhub.ai/user/rong-da) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and 3D content creators use this skill to have an agent generate Blender Python scripts, run Blender in background mode, and export simple model files for review or further editing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Blender scripts can clear the current scene or write to fixed local export paths. <br>
Mitigation: Run the skill in a new or temporary Blender file and choose unique output filenames before executing generated scripts. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/Rong-da/Modeling-Assistant-cli/tree/main/Modeling%20Assistant) <br>
- [ClawHub skill page](https://clawhub.ai/rong-da/skills/modeling-assistant) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown with Python and shell command snippets plus local file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or overwrite local .obj and .blend files and clears the active Blender scene before generating a model.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
