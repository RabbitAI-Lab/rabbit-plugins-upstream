## Description:

Generates Mermaid and ASCII diagrams of palace structure, knowledge topology, and synapse connectivity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect memory-palace graph structure, entity relationships, synapse strength, and palace layout as Mermaid diagrams or inline ASCII overviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic memory or diagram requests may activate this skill when the user did not intend to visualize palace data.

Mitigation: Confirm the user wants a memory-palace diagram before generating Mermaid or ASCII output.

Risk: Generated diagrams can expose knowledge-graph details, especially when rendered through Mermaid Chart MCP.

Mitigation: Use only palace data intended for visualization and review diagram content before sharing or rendering externally.

Risk: The artifact states the skill contract is unwired and direct command integration is pending.

Mitigation: Use the referenced palace manager or renderer workflow directly until command wiring is available.

## Reference(s):

- [Memory Palace plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/memory-palace)
- [palace-diagram ClawHub listing](https://clawhub.ai/athola/skills/nm-memory-palace-palace-diagram)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown containing Mermaid flowchart code or ASCII text diagrams]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use Mermaid Chart MCP for rendering Mermaid diagrams; ASCII output can be displayed inline.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
