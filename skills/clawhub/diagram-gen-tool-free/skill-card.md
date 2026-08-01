## Description: <br>
Generates and edits Mermaid flowcharts and sequence diagrams from natural-language descriptions for Markdown documentation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical writers use this skill to turn Chinese or English natural-language descriptions into Mermaid flowcharts and sequence diagrams for READMEs, API documentation, and personal project architecture notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated or edited diagram files may overwrite local Mermaid or Markdown assets if target paths are not reviewed. <br>
Mitigation: Review generated file paths and diffs before writing, and use new filenames or backups when preserving existing diagrams matters. <br>
Risk: Optional Mermaid CLI export commands can execute local npx or mermaid-cli packages. <br>
Mitigation: Run export commands only when the package source is trusted and local command execution is intended. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/diagram-gen-tool-free) <br>
- [Mermaid documentation](https://mermaid.js.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown with Mermaid code blocks and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or edit .mmd and Markdown files; optional image export uses Mermaid CLI when the user requests it.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
