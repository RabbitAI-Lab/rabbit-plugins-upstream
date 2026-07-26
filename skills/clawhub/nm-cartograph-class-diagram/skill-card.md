## Description: <br>
Generates a Mermaid class diagram showing types, inheritance, and composition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect a scoped codebase and generate a Mermaid class diagram of public types, inheritance, composition, and key relationships. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A broad prompt can cause unnecessary repository-wide context review. <br>
Mitigation: Use an explicit bounded scope, such as a specific module or path. <br>
Risk: Generated diagrams can omit details or simplify relationships because the artifact limits diagrams to about 12-15 classes. <br>
Mitigation: Review the Mermaid output and analysis notes against the target code before using the diagram as documentation. <br>


## Reference(s): <br>
- [Cartograph plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Guidance] <br>
**Output Format:** [Markdown with Mermaid classDiagram code and concise analysis notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Mermaid class diagrams are scoped to public methods, key attributes, relationships, and approximately 12-15 classes.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
