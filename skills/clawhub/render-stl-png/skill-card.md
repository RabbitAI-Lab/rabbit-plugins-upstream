## Description: <br>
Render an STL file to a PNG image with a solid color using a deterministic software renderer and adjustable 3D perspective parameters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ajmwagar](https://clawhub.ai/user/ajmwagar) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, designers, and product teams use this skill to create reproducible PNG preview or marketing images from ASCII or binary STL files without Blender or OpenGL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The wrapper downloads Pillow into a local cached Python environment on first use. <br>
Mitigation: Use it only where first-run PyPI downloads are acceptable, or preinstall and pin Pillow in a controlled environment. <br>
Risk: The renderer reads the STL path and writes the PNG path supplied by the caller. <br>
Mitigation: Pass only intended input and output paths, and run the skill with normal workspace file permissions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ajmwagar/skills/render-stl-png) <br>
- [Skill documentation](SKILL.md) <br>
- [Renderer script](scripts/render_stl_png.py) <br>


## Skill Output: <br>
**Output Type(s):** [files, shell commands, code, guidance] <br>
**Output Format:** [PNG image file with Markdown or shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts STL input and PNG output paths plus size, background color, mesh color, camera angle, field of view, margin, and light direction options.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
