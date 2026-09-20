## Description:

SQL Data Analyst analyzes local CSV, JSON, XLSX, and Parquet files with natural-language requests or read-only SQL and can generate local XLSX/HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze local tabular data files, run read-only SQL against local datasets, interpret limited results, and produce local XLSX or HTML reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an API key and contacts ai-skills.open-idea.net for paid authorization before paid operations.

Mitigation: Keep SQL_DATA_ANALYST_API_KEY in the configured environment only, do not paste it into chats or files, and confirm the billing model before running paid operations.

Risk: The local runner parses complex file formats including CSV, JSON, XLSX, and Parquet.

Mitigation: Use the runner only with datasets you intend to process locally and review dependency updates over time.

Risk: Query results may be limited or truncated before the agent explains them.

Mitigation: Check the returned truncation status and communicate result limits when presenting analysis.

## Reference(s):

- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/API-KEY.md)
- [Local Execution Workflow](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/USAGE.md)
- [Privacy and Security Boundaries](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/SECURITY.md)
- [Billing](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/BILLING.md)
- [Platform Authorization API](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands, SQL snippets, JSON result handling, and local XLSX/HTML report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local runner output is bounded to 1,000 rows or 10 MiB for query results; reports are written as local XLSX and self-contained HTML files.]

## Skill Version(s):

1.5.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
