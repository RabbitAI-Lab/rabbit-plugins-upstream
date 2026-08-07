## Description: <br>
Generates and edits Draw.io, Mermaid, and Excalidraw diagrams from natural-language intent or structured diagram specifications, with support for architecture, network topology, flowchart, swimlane, UML, and whiteboard-style diagrams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and documentation authors use this skill to turn text prompts or structured inputs into editable diagram files for architecture documentation, network planning, process mapping, UML documentation, and whiteboard-style collaboration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad command and file access for connector setup and diagram generation. <br>
Mitigation: Install and run it only in a trusted agent workspace, review connector configuration before use, and limit file-system access to directories intended for diagram inputs and outputs. <br>
Risk: Callback URLs may expose prompts, documents, or generated diagram content to an external endpoint. <br>
Mitigation: Use callback URLs only with trusted endpoints and avoid including sensitive prompts or source documents unless the endpoint is approved for that data. <br>
Risk: Generated diagrams can be structurally invalid or misleading if the prompt or JSON diagram specification is incomplete. <br>
Mitigation: Review generated files, validate diagram schema requirements, and confirm important architecture or process details before sharing or publishing outputs. <br>


## Reference(s): <br>
- [ClawHub diagram-generator release page](https://clawhub.ai/thcjp/skills/diagram-generator) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Diagram files such as .drawio, .mmd, and .excalidraw, plus Markdown guidance and JSON diagram specifications] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include generated file paths, connector configuration guidance, validation notes, and troubleshooting steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
