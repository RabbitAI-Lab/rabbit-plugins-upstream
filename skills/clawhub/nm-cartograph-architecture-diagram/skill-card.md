## Description:

Generates a Mermaid architecture diagram showing high-level component relationships.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to explore a codebase and produce a high-level Mermaid flowchart for onboarding, architecture documentation, or pull request review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagram generation may expose private repository structure to a Mermaid rendering MCP.

Mitigation: Choose an explicit scope before use on private repositories and review generated Mermaid content before rendering.

Risk: High-level architecture diagrams can omit or simplify component relationships.

Mitigation: Review the diagram against the source code before using it for onboarding, documentation, or pull request decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-cartograph-architecture-diagram)
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Guidance]

**Output Format:** [Markdown with Mermaid code blocks and a brief prose summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call a Mermaid rendering MCP after generating and validating the diagram syntax.]

## Skill Version(s):

1.9.19 (source: server release evidence; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
