## Description: <br>
Generates a Mermaid class diagram showing types, inheritance, and composition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect a code scope and produce a concise class diagram for understanding type relationships, inheritance, composition, and public APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The assistant inspects the code scope named by the user and may include structural details in the generated diagram. <br>
Mitigation: Use a limited scope for sensitive repositories and review the diagram content before sharing or rendering it externally. <br>
Risk: The generated Mermaid diagram content is sent to the configured Mermaid rendering MCP. <br>
Mitigation: Avoid rendering sensitive code structures through external or untrusted rendering services. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-cartograph-class-diagram) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/athola) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown containing Mermaid classDiagram code and analysis notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Limits diagrams to about 12-15 classes and focuses on public methods, key attributes, inheritance, composition, aggregation, and dependency relationships.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
