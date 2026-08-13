## Description:

Generates patent-analysis-supported project proposal reports by guiding technology scope definition, PatSnap search strategy, seven analysis modules, and final report assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate data-driven research project proposal reports supported by patent search, competitive landscape analysis, enterprise patent positioning, innovation assessment, IP planning, technical route validation, preliminary FTO risk review, and patent-related evaluation metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent-supported proposal generation may require sharing technical descriptions, company names, and search queries with the configured PatSnap MCP environment.

Mitigation: Confirm the PatSnap account, authorization, and data-sharing posture are acceptable before using the skill with proprietary project ideas.

Risk: The FTO section is preliminary and may be mistaken for legal advice.

Mitigation: Use the generated FTO analysis only for project decision support and obtain formal legal review from a qualified patent professional before relying on it.

Risk: Patent legal-status and landscape data can become stale after retrieval.

Mitigation: Record the search date in the report and refresh searches before making time-sensitive IP or project decisions.

## Reference(s):

- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-project-proposal)

## Skill Output:

**Output Type(s):** [markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown report sections with search records, tables, and structured analysis templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call configured PatSnap MCP tools and should ground patent counts, patent numbers, applicants, and legal-status observations in returned patent data.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
