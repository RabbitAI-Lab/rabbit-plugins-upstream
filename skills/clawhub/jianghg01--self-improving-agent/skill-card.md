## Description:

Self-Improving Agent gives agents a three-level memory framework for session context, task digests, long-term lessons, failure review, memory compression, and reusable sub-skill extraction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jianghg01](https://clawhub.ai/user/jianghg01)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add memory, failure-review workflows, and reusable skill extraction to general-purpose agents that support session context and optional persistent storage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can broadly store and reuse long-term user history without enough consent or scoping controls.

Mitigation: Require explicit approval for L2 and L3 writes, keep memories scoped to a user or project, and exclude secrets and sensitive personal data.

Risk: Global automatic memory injection can reintroduce stale, irrelevant, or sensitive context into later tasks.

Mitigation: Disable global automatic memory injection by default and review retrieved memories before applying them.

Risk: Automatically generated or updated skills can preserve incorrect guidance or unsafe workflows.

Mitigation: Review and scan generated or updated skills before registration or deployment.

## Reference(s):

- [Memory Schema](artifact/memory-schema.md)
- [Review Templates](artifact/review-templates.md)
- [Skill Extraction Protocol](artifact/skill-extraction.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured memory templates, optional JSON memory exports, and generated skill drafts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request persistent memory writes and skill registration when supported; memory contents should exclude secrets and sensitive personal data.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
