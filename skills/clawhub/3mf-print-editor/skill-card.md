## Description: <br>
Guideline for safely editing BambuStudio .3mf 3D-printing project files by modifying mesh geometry, XML/config relationships, multi-plate placement, and print settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clarezoe](https://clawhub.ai/user/clarezoe) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and technical operators use this skill when they need an agent to edit, split, reposition, merge, or reconfigure BambuStudio .3mf project files directly instead of using the slicer GUI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The helper can overwrite an existing output file when directed to that path. <br>
Mitigation: Use a project-specific working directory and review the output filename before running packaging helpers. <br>
Risk: The skill's multi-plate coordinate and metadata guidance is verified for BambuStudio and may not transfer to other slicers. <br>
Mitigation: Confirm the target slicer and re-verify constants and schema behavior before applying BambuStudio-specific formulas elsewhere. <br>
Risk: Manual .3mf edits can produce invalid XML, broken mesh geometry, or incorrect plate placement. <br>
Mitigation: Run XML, mesh integrity, volume/bounds, plate-placement, and fresh re-extraction checks before delivering edited files. <br>


## Reference(s): <br>
- [3MF Structure](references/3mf-structure.md) <br>
- [Plate Coordinate System](references/plate-coordinate-system.md) <br>
- [Mesh Editing Notes](references/mesh-editing-notes.md) <br>
- [Mesh Tools](scripts/mesh_tools.py) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline code and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local file paths, validation steps, and generated or modified .3mf package guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: skill metadata and server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
