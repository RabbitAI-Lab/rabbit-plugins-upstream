## Description: <br>
Lightweight Mermaid diagram generation tool for quickly creating and editing flowcharts and sequence diagrams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical writers, and project maintainers use this skill to turn natural-language diagram requests into Mermaid flowcharts or sequence diagrams for Markdown documentation. It can also help read and revise existing .mmd diagram files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may help create or edit local Mermaid files, which can overwrite existing diagrams if paths are reused. <br>
Mitigation: Ask the agent to write to a new filename or confirm before replacing an existing diagram file. <br>
Risk: Optional image export can involve local mermaid-cli or npx command execution. <br>
Mitigation: Run export commands only when explicitly requested, and review input and output paths before execution. <br>


## Reference(s): <br>
- [Diagram Gen Tool Free on ClawHub](https://clawhub.ai/thcjp/skills/diagram-gen-tool-free) <br>
- [Mermaid documentation](https://mermaid.js.org) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown with Mermaid code blocks and optional shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Mermaid syntax for .mmd files and Markdown documents; optional image export commands require local mermaid-cli or npx.] <br>

## Skill Version(s): <br>
1.0.0 (source: server metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
