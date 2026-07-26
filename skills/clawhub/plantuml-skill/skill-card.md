## Description: <br>
Turn natural language into uml-diagrams.org style PlantUML diagrams, including sequence, class, activity, use case, component, and state diagrams, and render them to SVG, PNG, PDF, or text output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samonysh](https://clawhub.ai/user/samonysh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical writers use this skill to convert natural language requirements, flows, and architecture descriptions into PlantUML source and rendered UML diagram artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional remote rendering can upload diagram source to Kroki or a configured remote server when --use-public-server is enabled. <br>
Mitigation: Use Docker or a local plantuml.jar for confidential diagrams; enable remote rendering only for non-sensitive diagrams after verifying PLANTUML_PUBLIC_SERVER. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/samonysh/skills/plantuml-skill) <br>
- [uml-diagrams.org](https://www.uml-diagrams.org) <br>
- [Kroki](https://kroki.io) <br>
- [PlantUML style evolution](https://plantuml.com/style-evolution) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with PlantUML code blocks and shell commands; rendered diagram files may be SVG, PNG, PDF, or text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local-first rendering uses Docker or a local plantuml.jar by default; remote Kroki rendering is opt-in.] <br>

## Skill Version(s): <br>
1.7.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
