## Description: <br>
Creates standardized stage costume design board collages and PDFs from user-supplied costume sketches and reference images. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[trumcy9987](https://clawhub.ai/user/trumcy9987) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Designers, creative teams, and agents use this skill to assemble stage costume full-body views, detail references, role metadata, color notes, fabric notes, and design notes into a consistent review board. It is intended for local image-collage generation and print-ready PNG/PDF outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill adds Pillow to the Python environment and processes local image folders. <br>
Mitigation: Install Pillow only in an environment where that dependency is acceptable, and run the skill on image folders intentionally selected for the task. <br>
Risk: Generated PNG/PDF boards may contain user-supplied images or design details that are not ready for public release. <br>
Mitigation: Review generated outputs before sharing them outside the intended design workflow. <br>


## Reference(s): <br>
- [V9.1 layout specification](artifact/references/v9.1-layout-spec.md) <br>
- [ClawHub skill page](https://clawhub.ai/trumcy9987/skills/costume-design-board) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with Python command examples; generated PNG and PDF files when the bundled script is run] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3 and Pillow; reads local image folders selected by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
