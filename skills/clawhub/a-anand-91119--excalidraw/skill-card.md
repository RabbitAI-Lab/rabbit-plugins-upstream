## Description: <br>
Generate hand-drawn style diagrams, flowcharts, and architecture diagrams as PNG images from Excalidraw JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[a-anand-91119](https://clawhub.ai/user/a-anand-91119) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to create architecture diagrams, flowcharts, and other hand-drawn style visuals from Excalidraw JSON and render them as PNG files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup installs npm dependencies and downloads fonts before rendering diagrams. <br>
Mitigation: Run setup in a controlled local environment and review the dependency lockfile and setup script before installation. <br>
Risk: Generated Excalidraw inputs and PNG outputs may remain as local temporary files. <br>
Mitigation: Avoid including secrets or confidential architecture details unless local file retention is acceptable, and remove temporary files after use. <br>
Risk: Generated diagrams can misrepresent a requested architecture or flow if the JSON layout is wrong. <br>
Mitigation: Review rendered PNG output before sharing or using it as authoritative documentation. <br>


## Reference(s): <br>
- [Excalidraw Element Schema Reference](references/element-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with Excalidraw JSON, shell commands, and PNG file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The renderer reads Excalidraw JSON from a file or stdin and writes a PNG image file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
