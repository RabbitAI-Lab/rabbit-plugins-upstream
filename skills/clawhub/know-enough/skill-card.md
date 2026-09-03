## Description:

Acquire the minimum sufficient knowledge needed to make the next material decision by identifying knowledge gaps, choosing authoritative or contextual sources, retrieving selectively, assessing sufficiency, and stopping when more retrieval is unlikely to change the outcome.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill when missing organization-specific, historical, current, or contextual knowledge could materially affect a decision. It helps the agent form focused retrieval objectives, select sources by authority and role, and stop once the decision is sufficiently supported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected RAG or search tools may expose sources the agent is not allowed to consult.

Mitigation: Before installation, confirm that configured retrieval tools expose only authorized sources for the intended users and tasks.

Risk: Historical precedent may be mistaken for current policy or authority.

Mitigation: Use the source registry roles to separate authoritative, precedent, observational, and reference sources, and prefer authoritative sources for current requirements.

Risk: Unfocused retrieval may disclose or process more information than needed for the decision.

Mitigation: Require an explicit information objective before retrieval and stop when additional evidence is unlikely to change the decision.

## Reference(s):

- [Knowledge Source Registry](references/knowledge-source-registry.md)
- [Knowledge Sources Example](references/knowledge-sources.example.yaml)
- [Pi / pi-rag Integration Pattern](references/pi-rag-integration.md)
- [ClawHub skill page](https://clawhub.ai/raguets/skills/know-enough)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text knowledge-state summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include the decision being supported, known facts, material gaps, sources consulted with roles, learned evidence, remaining uncertainty, and an ENOUGH or NOT ENOUGH sufficiency judgment.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
