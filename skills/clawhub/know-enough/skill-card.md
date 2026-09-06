## Description:

Part of the Overpowered skill suite, Know Enough guides agents to identify material knowledge gaps, choose authoritative or contextual sources, retrieve selectively, assess sufficiency, and stop when more retrieval is unlikely to change the next decision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and agents use this skill when organization-specific, historical, current, or otherwise missing knowledge could materially affect a task and retrieval, RAG, or search tools are available. It helps them retrieve only decision-relevant information, keep a compact knowledge state, and stop once the next material decision is sufficiently supported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can steer an agent to search connected knowledge bases, including private or business records, when retrieval tools are available.

Mitigation: Use it only in environments where retrieval permissions, source registries, and corpus access controls are configured for the intended user and task.

## Reference(s):

- [Knowledge Source Registry](references/knowledge-source-registry.md)
- [Knowledge Sources Example](references/knowledge-sources.example.yaml)
- [Pi / pi-rag Integration Pattern](references/pi-rag-integration.md)
- [Overpowered skill suite](https://github.com/raguets/overpowered)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Markdown or plain text knowledge state]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include the decision being supported, known facts, material gaps, sources consulted with roles, learned evidence, remaining uncertainty, and an ENOUGH or NOT ENOUGH sufficiency judgment.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
