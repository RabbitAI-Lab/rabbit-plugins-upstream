## Description: <br>
Tracks keyword rankings, SERP feature ownership, and AI visibility over time from provided exports or connected tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing and SEO practitioners use this skill to set up rank tracking, compare ranking snapshots, analyze SERP feature and AI visibility changes, and produce ranking reports with source-labeled metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Rank checks may use web fetching or connected SEO data sources that expose queried domains, keywords, or markets to external services. <br>
Mitigation: Review connected-tool credentials separately, prefer user-provided exports when appropriate, and approve any saved monitoring summaries before writing them. <br>
Risk: Ranking movement explanations and traffic impact estimates can be misleading if they are treated as measured facts. <br>
Mitigation: Keep source labels on every metric, mark unavailable values as N/A, and verify estimated causes before using the report for business decisions. <br>


## Reference(s): <br>
- [Ranking Analysis Output Templates](references/ranking-analysis-templates.md) <br>
- [Rank Tracking Setup Guide](references/tracking-setup-guide.md) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown reports, setup tables, delta summaries, and optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Every metric should be labeled as Measured, User-provided, Estimated, or N/A; saved monitoring summaries require user approval.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
