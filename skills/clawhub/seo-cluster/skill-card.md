## Description:

seo-cluster plans SERP-overlap-based topic clusters for SEO content architecture, including keyword expansion, hub-and-spoke structure, internal linking, interactive maps, and optional content brief or draft generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

SEO strategists, content marketers, and developers use this skill to expand seed keywords, cluster them by live SERP overlap, design hub-and-spoke content architecture, and generate plans, briefs, link matrices, scorecards, and interactive maps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Execution mode can create, overwrite, and modify local SEO content files in the working directory.

Mitigation: Run the skill in a dedicated project folder and keep version control or backups before invoking execution.

Risk: The cluster plan can drive broad draft generation and backlink injection before safeguards are clear.

Mitigation: Review cluster-plan.json before execution and inspect generated drafts and link changes before publishing.

## Reference(s):

- [SERP Overlap Methodology](artifact/references/serp-overlap-methodology.md)
- [Hub-and-Spoke Content Architecture](artifact/references/hub-spoke-architecture.md)
- [Execution Workflow](artifact/references/execution-workflow.md)
- [seo-cluster on ClawHub](https://clawhub.ai/asale-ai/skills/seo-cluster)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown, JSON, HTML, and structured text files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create cluster-plan.json, cluster-plan.md, cluster-map.html, cluster-briefs, and cluster-scorecard.md in the current working directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
