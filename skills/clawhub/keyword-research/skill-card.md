## Description: <br>
Discovers, scores, and clusters keywords for SEO and GEO planning, prioritizing search volume, keyword difficulty, intent, and topic clusters from provided or connected data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketing, SEO, and content strategy users use this skill to research keyword opportunities for a topic, page, product, service, or campaign. It produces prioritized keyword briefs with intent, difficulty, opportunity, topic clusters, content calendar recommendations, and a reusable research handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can save reusable keyword priorities, competitor facts, and strategy decisions into agent memory. <br>
Mitigation: Review memory writes and avoid storing sensitive search, competitor, or business metrics unless the workspace policy allows it. <br>
Risk: Keyword volume, difficulty, and ranking data may be unavailable or estimated when SEO tools or Search Console are not connected. <br>
Mitigation: Require each metric to be labeled Measured, User-provided, Estimated, or N/A, and do not present estimates as measured facts. <br>
Risk: Competitor-relative content gap requests can fall outside this skill's intended scope. <br>
Mitigation: Route competitor coverage gap work to content-gap-analysis or competitor-analysis as directed by the skill and security guidance. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/keyword-research) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Instructions Detail](references/instructions-detail.md) <br>
- [Keyword Intent Taxonomy](references/keyword-intent-taxonomy.md) <br>
- [Topic Cluster Templates](references/topic-cluster-templates.md) <br>
- [Keyword Prioritization Framework](references/keyword-prioritization-framework.md) <br>
- [Example Report](references/example-report.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands] <br>
**Output Format:** [Markdown keyword brief with tables, scores, topic clusters, content calendar recommendations, next steps, and a reusable handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Metrics are labeled Measured, User-provided, Estimated, or N/A; results may include reusable memory summaries under memory/research/.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
