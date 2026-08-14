## Description:

Search Experience Optimization reads Google SERPs backwards to detect page-type mismatches, derive user stories from search intent signals, and score pages from multiple persona perspectives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, SEO practitioners, content strategists, and developers use this skill to compare a target page against live SERP expectations, identify intent or page-type mismatches, derive search-driven user stories, and prioritize UX and content improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target URLs and keywords may be sent to search, rendering, or DataForSEO services during analysis.

Mitigation: Use only URLs and keywords appropriate for those services, and review data handling expectations before running the workflow.

Risk: DataForSEO usage can incur external API cost.

Mitigation: Run a cost estimate and obtain explicit user confirmation before any DataForSEO API call.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/asale-ai/skills/seo-sxo)
- [Page Type Taxonomy for SERP Classification](references/page-type-taxonomy.md)
- [Persona-Based Scoring Methodology](references/persona-scoring.md)
- [User Story Framework: SERP Signals to User Intent](references/user-story-framework.md)
- [Wireframe Templates: IST/SOLL Patterns](references/wireframe-templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown analysis with tables, scored findings, prioritized recommendations, and optional semantic HTML wireframe outlines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include DataForSEO-backed SERP and keyword data when available; DataForSEO calls require cost estimation and user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
