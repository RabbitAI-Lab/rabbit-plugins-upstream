## Description: <br>
Generates Mermaid diagrams from natural-language descriptions for developers and technical writers, with optional ASCII sketches and PNG rendering guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, product teams, and technical writers use this skill to turn process, architecture, API interaction, data model, class, and state descriptions into concise Mermaid diagrams for documentation and review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional PNG rendering can involve local file output or command-line Mermaid rendering. <br>
Mitigation: Ask the skill to create files or render PNGs only when local output or command-line Mermaid rendering is intentionally needed, and review proposed commands before execution. <br>
Risk: The trigger wording is broader than necessary and may invite use for general analytics or reporting tasks unrelated to diagrams. <br>
Mitigation: Limit invocation to diagram creation, refinement, or export requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/diagram-tool-free) <br>
- [Skill source](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Mermaid code blocks, ASCII sketches, and optional PNG-rendering command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Free edition; one chart per session; PNG export requires Node.js 16+ and Mermaid CLI.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
