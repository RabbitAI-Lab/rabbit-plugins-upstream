## Description: <br>
Generates a Mermaid sequence diagram showing how data moves between components. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to trace request flows, understand data transformation pipelines, and document API call chains in a codebase. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill inspects code structure and may expose sensitive architecture or flow details during diagram generation or rendering. <br>
Mitigation: Use a narrow scope such as a specific feature, endpoint, or module, and review any Mermaid MCP rendering step before sharing sensitive structure. <br>
Risk: Generated diagrams may omit or simplify data paths, especially when flows are conditional or circular. <br>
Mitigation: Review the Mermaid sequence diagram against the relevant source flow and keep circular calls or complex branches documented with notes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-cartograph-data-flow) <br>
- [Cartograph Plugin Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Guidance] <br>
**Output Format:** [Markdown with Mermaid sequence diagram code and a brief prose description] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a rendered Mermaid diagram when the configured Mermaid MCP renderer is available.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
