## Description: <br>
Generates a Mermaid sequence diagram showing how data moves between components. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to trace request flows, document data transformation pipelines, and explain API call chains in codebases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Repository structure or code behavior could be summarized incorrectly in the generated flow diagram. <br>
Mitigation: Review the Mermaid diagram and prose against the source code before sharing or relying on the documentation. <br>
Risk: Rendering through the Mermaid Chart MCP may share diagram text and related prompts with the configured renderer. <br>
Mitigation: Use the skill only on repositories and flow details that are appropriate for the configured rendering service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-cartograph-data-flow) <br>
- [Cartograph plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with Mermaid sequence diagram code and concise prose] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May request rendering through the configured Mermaid Chart MCP and retry Mermaid syntax fixes up to two times.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
