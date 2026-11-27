## Description:

Knowledge Router routes knowledge queries to the most appropriate source based on question type, covering wiki-kb, memory-tencentdb, Ontology, memorySearch, and domain-kit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to classify knowledge questions and route searches across curated wiki content, conversation memory, ontology relationships, vector search, and domain-specific knowledge sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may search conversation history and persistent memory stores from broad prompts without clear consent or access limits.

Mitigation: Use it only where the underlying tools enforce user, tenant, project, and session boundaries; narrow triggers and require confirmation before raw conversation or persistent memory searches.

## Reference(s):

- [Knowledge Router on ClawHub](https://clawhub.ai/paudyyin/skills/knowledge-router)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source labels, confidence levels, conflict notes, and no-result suggestions.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
