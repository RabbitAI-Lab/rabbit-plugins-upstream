## Description:

Generates a Mermaid class diagram showing types, inheritance, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect a codebase and produce a Mermaid class diagram that summarizes public types, inheritance, composition, and key interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill can involve inspecting source code in the requested scope and sending generated Mermaid diagram text to a Mermaid Chart MCP renderer.

Mitigation: Keep the requested scope narrow for private repositories and review diagram content before rendering or sharing it.

## Reference(s):

- [Cartograph plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph)
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-cartograph-class-diagram)

## Skill Output:

**Output Type(s):** [markdown, code, guidance]

**Output Format:** [Markdown with Mermaid classDiagram code and analysis notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call a Mermaid Chart MCP renderer to validate and render the diagram.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
