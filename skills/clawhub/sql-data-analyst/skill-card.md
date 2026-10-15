## Description:

Analyzes local CSV, JSON, XLSX, and Parquet files with read-only SQL and produces local reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users analyze local datasets by asking questions or providing read-only SQL, then review query results or generate local XLSX and HTML reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A vulnerable Parquet/Arrow parsing dependency may expose users who process untrusted files.

Mitigation: Avoid untrusted Parquet or Arrow inputs until the pyarrow dependency is upgraded to a patched version.

Risk: Paid authorization checks and local workspace persistence may create unexpected charges or retain sensitive analysis files.

Mitigation: Review platform pricing and local storage practices before installation and paid operations; keep API keys private.

Risk: Deleting a dataset permanently removes its local copy.

Mitigation: Confirm the dataset and retain needed backups before using the delete command.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/youteacher/skills/sql-data-analyst)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/API-KEY.md)
- [Local analysis workflow](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/USAGE.md)
- [Privacy and security boundaries](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/SECURITY.md)
- [Billing information](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/BILLING.md)
- [Authorization API specification](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Code, JSON, Files]

**Output Format:** [Markdown explanations, SQL queries, JSON results, and local XLSX or HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query results are limited to 1,000 rows and 10 MiB; report paths refer to local files.]

## Skill Version(s):

1.7.0 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
