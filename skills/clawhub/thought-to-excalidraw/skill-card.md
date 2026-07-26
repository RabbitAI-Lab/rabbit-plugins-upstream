## Description: <br>
Visualizes Product Manager thoughts (Why, What, How, User Journey) into an editable Excalidraw diagram. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sairammahadevan](https://clawhub.ai/user/sairammahadevan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Product managers and product teams use this skill to turn unstructured feature notes, requirements, implementation ideas, and user journeys into an editable Excalidraw visual specification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow writes a local .excalidraw file and may overwrite an existing file at the chosen output path. <br>
Mitigation: Check the output path before running the generator and choose a new filename when preserving an existing diagram matters. <br>
Risk: The workflow creates a temporary JSON input file containing the user's product notes. <br>
Mitigation: Delete the temporary input file after the diagram is generated, as described by the skill workflow. <br>


## Reference(s): <br>
- [Excalidraw JSON Schema Reference](references/excalidraw-schema.md) <br>
- [Excalidraw](https://excalidraw.com) <br>
- [ClawHub skill page](https://clawhub.ai/sairammahadevan/skills/thought-to-excalidraw) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with JSON input and a generated .excalidraw file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a local Excalidraw diagram file from structured product notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
