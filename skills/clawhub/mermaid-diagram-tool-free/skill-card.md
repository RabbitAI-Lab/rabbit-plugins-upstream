## Description: <br>
Generates Mermaid diagram code from text descriptions for common diagram types, including flowcharts, sequence diagrams, mind maps, state diagrams, ER diagrams, timelines, and user journeys. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, technical writers, and individual users use this skill to turn plain-language descriptions into Mermaid code blocks for documentation, notes, simple business process visualization, and Mermaid syntax learning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad file and shell command access may affect local files or execute commands beyond direct diagram-code generation. <br>
Mitigation: Use direct Markdown and Mermaid code generation by default, and require explicit confirmation before file writes, npm installs, Mermaid CLI rendering, conversions, or network diagnostics. <br>
Risk: Generated diagrams may contain Mermaid syntax or layout issues, especially with long labels or complex business logic. <br>
Mitigation: Review generated code and render it in a Mermaid-compatible preview before publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/mermaid-diagram-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Mermaid code blocks and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Mermaid syntax self-check notes; require confirmation before file writes, npm installs, Mermaid CLI rendering, conversions, or network diagnostics.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and target metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
