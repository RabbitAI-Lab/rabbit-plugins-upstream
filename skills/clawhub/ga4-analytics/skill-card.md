## Description: <br>
Google Analytics 4, Search Console, and Indexing API toolkit for analyzing website traffic, page performance, user demographics, real-time visitors, search queries, SEO metrics, and URL indexing status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adamkristopher](https://clawhub.ai/user/adamkristopher) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, site owners, and analytics practitioners use this skill to query GA4, Search Console, and Indexing API data, then turn saved results into summaries, tables, trends, and recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Google service account credentials for GA4, Search Console, and Indexing API access. <br>
Mitigation: Use a dedicated least-privilege service account limited to the intended GA4 property and Search Console site. <br>
Risk: Local .env credentials and saved results may expose sensitive analytics or property details if committed or shared. <br>
Mitigation: Keep .env and results/ out of version control and review saved output before sharing. <br>
Risk: The removeFromIndex() action can request URL removal and affect search visibility. <br>
Mitigation: Avoid exposing or invoking removeFromIndex() unless URL removal is intended and each URL has been confirmed. <br>


## Reference(s): <br>
- [API Reference](references/api-reference.md) <br>
- [GA4 Analytics ClawHub Skill Page](https://clawhub.ai/adamkristopher/skills/ga4-analytics) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with TypeScript and shell command examples; API results are saved as timestamped JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Google service account credentials and writes results under results/ by category.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and scripts/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
