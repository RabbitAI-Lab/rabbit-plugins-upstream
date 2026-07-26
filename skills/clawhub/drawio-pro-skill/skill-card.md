## Description: <br>
Drawio Skill helps agents create editable draw.io diagrams, convert project and infrastructure inputs into visual diagrams, apply style presets, validate diagram structure, and export diagrams to common formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agents365-ai](https://clawhub.ai/user/agents365-ai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, architects, and technical teams use this skill to produce architecture diagrams, flowcharts, UML and ER diagrams, infrastructure views, PR diagram reviews, and exported draw.io assets from natural-language requests or structured project inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live Terraform, Docker, and Kubernetes diagramming can expose project topology and sensitive resource names, including Kubernetes Secret names, in generated diagrams. <br>
Mitigation: Use sanitized snapshots for shareable diagrams, omit Kubernetes Secrets unless their relationships are intentionally needed, and review generated outputs before distribution. <br>
Risk: The skill runs local CLI tools and renders local diagram files, which can be risky when processing untrusted repositories or pull requests. <br>
Mitigation: Run rendering and PR-review workflows in an isolated environment, review proposed commands before execution, and grant only the filesystem and tool access needed for the diagram task. <br>
Risk: Preset-management flows can rename or delete user style files if paths or preset names are misunderstood. <br>
Mitigation: Use simple normalized preset names and confirm exact file paths before delete or rename operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agents365-ai/skills/drawio-pro-skill) <br>
- [Toolbox reference](references/toolbox.md) <br>
- [XML authoring reference](references/xml-authoring.md) <br>
- [Auto-layout reference](references/autolayout.md) <br>
- [Live infrastructure reference](references/live-infra.md) <br>
- [Style presets reference](references/style-presets.md) <br>
- [Troubleshooting reference](references/troubleshooting.md) <br>
- [Tube-map reference](references/tubemap.md) <br>
- [draw.io desktop releases](https://github.com/jgraph/drawio-desktop/releases) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance, shell commands, JSON or XML diagram inputs, .drawio files, and exported PNG/SVG/PDF/JPG or HTML/PPTX artifacts depending on the workflow.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may require local draw.io desktop CLI for rendering and Graphviz for optional auto-layout; embedded final PNG/SVG/PDF exports can preserve editable diagram XML.] <br>

## Skill Version(s): <br>
1.34.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
