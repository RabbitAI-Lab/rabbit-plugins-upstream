## Description: <br>
Converts 2D images with labeled dimensions into SVG blueprints and STL files for 3D printing or machining workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[auto-dog](https://clawhub.ai/user/auto-dog) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and makers use this skill to turn dimensioned part images or sketches into reviewed SVG plans and STL meshes. The workflow supports iterative adjustment after visual review or print feedback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unpinned Python dependencies can reduce reproducibility in stricter environments. <br>
Mitigation: Install dependencies in a project-local virtual environment and review or pin package versions before use where reproducibility matters. <br>
Risk: Incorrect image interpretation or dimensions can produce an inaccurate STL. <br>
Mitigation: Review and confirm the generated SVG blueprint before running the STL generation step, then iterate from print or machining feedback. <br>
Risk: Generated SVG and STL artifacts are written locally and may be reused without review. <br>
Mitigation: Keep generated work in the current project directory and inspect outputs before fabrication or downstream use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/auto-dog/skills/image-to-3d-model) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with Python code edits, shell commands, SVG blueprints, and STL file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated SVG and STL files should remain in the current project workspace and be reviewed before fabrication.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
