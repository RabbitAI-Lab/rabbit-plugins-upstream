## Description: <br>
Converts 2D images with labeled dimensions and metric constraints into SVG floor plans and STL files for engineering and 3D printing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[auto-dog](https://clawhub.ai/user/auto-dog) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and makers use this skill to turn dimensioned part images or sketches into confirmed SVG plans and generated STL files for 3D printing or machining. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags the release as suspicious because the workflow asks the agent to modify its packaged generator script despite a rule limiting edits to generated SVG/STL files. <br>
Mitigation: Review before installing, run in a project-specific workspace, and copy src/generate.py to a working file before editing. <br>
Risk: The Python dependencies are unpinned, which can change install-time behavior. <br>
Mitigation: Pin or lock numpy, trimesh, shapely, and mapbox_earcut before installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/auto-dog/skills/image-to-3d-model) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with code edits, shell commands, SVG, and STL file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation of the SVG plan before STL generation; the packaged generator is a template that should be copied or adapted in a project workspace before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
