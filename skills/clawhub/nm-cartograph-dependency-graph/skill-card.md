## Description: <br>
Generates a Mermaid dependency graph showing import relationships between modules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to map module import relationships, identify circular dependencies and coupling, and plan refactors with Mermaid dependency graphs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose module names and import relationships to a Mermaid rendering MCP. <br>
Mitigation: Use it only on codebases where that structural information may be shared with the rendering tool, and provide a clear project or module scope. <br>
Risk: Generated dependency graphs or analysis notes may be incomplete or misleading if code exploration misses imports or dynamic dependencies. <br>
Mitigation: Review the Mermaid graph and dependency notes against the relevant source files before using them to make refactoring decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-cartograph-dependency-graph) <br>
- [Cartograph source homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, guidance] <br>
**Output Format:** [Markdown with Mermaid code blocks, rendered diagram references, and analysis notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dependency counts, fan-in and fan-out observations, and circular dependency notes.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
