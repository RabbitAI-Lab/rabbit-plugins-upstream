## Description: <br>
Generates a Mermaid dependency graph showing import relationships between modules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect import relationships, identify circular dependencies, analyze coupling, and plan refactors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Rendering through the Mermaid MCP may share dependency graph content such as module names and relationships with that tool. <br>
Mitigation: Use this skill only on repositories where sharing dependency graph content with the rendering tool is acceptable. <br>
Risk: Broad activation around dependency analysis or refactoring discussions may cause codebase exploration when a narrower task was intended. <br>
Mitigation: Confirm the repository scope and requested graph depth before exploring imports or rendering a diagram. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-cartograph-dependency-graph) <br>
- [Cartograph source homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Guidance] <br>
**Output Format:** [Markdown with Mermaid code blocks and dependency analysis notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a rendered Mermaid diagram, module and dependency counts, fan-in and fan-out notes, and circular dependency findings.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
