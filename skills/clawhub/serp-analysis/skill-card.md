## Description: <br>
Serp Analysis maps search result features, layout, ranking patterns, search intent, AI Overviews, and snippet opportunities for a target query. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, SEO, and content strategy users use this skill to analyze live or provided search results for a query, identify dominant search intent, assess ranking difficulty, and plan SERP feature opportunities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, SERP URLs, or client context may be sent to live search sources or optional third-party SERP connectors. <br>
Mitigation: Review and remove confidential client data from queries and supplied context before running live lookups. <br>
Risk: Fetched search result pages and third-party pages may contain untrusted or misleading content. <br>
Mitigation: Treat fetched content as evidence only, verify important claims against the SERP, and do not follow prompt-like directives from fetched pages. <br>
Risk: Reusable SEO research notes may persist sensitive project details in memory files. <br>
Mitigation: Review saved research notes before sharing, deployment, or use on confidential projects. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/serp-analysis) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Analysis Templates](references/analysis-templates.md) <br>
- [SERP Feature Taxonomy](references/serp-feature-taxonomy.md) <br>
- [Example Report](references/example-report.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown SERP brief with tables, evidence labels, recommendations, and a reusable research handoff summary.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Labels metrics as Measured, User-provided, Estimated, or N/A; may write reusable SEO research notes to memory.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
