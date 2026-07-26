## Description: <br>
Anymermaid helps agents create Mermaid diagrams and render them through the Mermaid CLI as SVG, PNG, or PDF files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyforge](https://clawhub.ai/user/anyforge) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical writers, and other agent users use this skill to turn workflows, system relationships, architecture, data flows, and other structured ideas into Mermaid diagram source and rendered image files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad diagram requests and produce an incorrect or misleading visualization. <br>
Mitigation: Review the generated Mermaid source against the user's intent before relying on or publishing the rendered diagram. <br>
Risk: The skill can run the local Mermaid CLI, write .mmd and rendered output files, and open rendered files in a local viewer. <br>
Mitigation: Use a trusted mmdc installation, inspect output paths before rendering, and skip local viewer opening in headless or restricted environments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/anyforge/skills/anymermaid-skill) <br>
- [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli) <br>
- [Mermaid Documentation](https://mermaid.nodejs.cn/) <br>
- [Mermaid Configuration Schema](https://mermaid.nodejs.cn/config/schema-docs/config.html) <br>
- [Mermaid Syntax Reference](references/syntax.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Files, Configuration] <br>
**Output Format:** [Markdown guidance with Mermaid source and shell command examples; may create .mmd, SVG, PNG, or PDF files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the local mmdc CLI when available, may retain .mmd source files for later edits, and may open rendered files in a local viewer outside headless environments.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
