## Description:

SQL Data Analyst helps an agent analyze local CSV, JSON, XLSX, and Parquet files with natural-language questions or read-only SQL and create local XLSX or HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect local datasets, ask data questions, execute read-only SQL, and generate local reports while keeping raw data on the user's machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local runner stores normalized dataset copies and generated reports in the OpenClaw workspace.

Mitigation: Use appropriate local file permissions, avoid shared workspaces for sensitive data, and delete local dataset copies when analysis is complete.

Risk: The security guidance warns against running the skill on untrusted files until the pyarrow pin is updated.

Mitigation: Only process files from trusted sources, and update the pinned dependency before using the skill with untrusted datasets.

Risk: The SQL_DATA_ANALYST_API_KEY authorizes paid platform operations.

Mitigation: Store the key only in the configured environment variable and do not include it in prompts, SQL, data files, logs, reports, or repositories.

Risk: Dataset deletion is irreversible for the local dataset copy.

Mitigation: Confirm the intended dataset identifier before deletion and do not claim cleanup succeeded until the delete command completes successfully.

Risk: Large or complex queries can return truncated results.

Mitigation: Tell users when truncated=true appears and refine the query or report scope before drawing conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/sql-data-analyst)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API Key configuration](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/API-KEY.md)
- [Local execution flow and commands](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/USAGE.md)
- [Privacy and security boundary](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/SECURITY.md)
- [Billing details](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/BILLING.md)
- [Platform authorization API](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with SQL snippets, shell commands, JSON result summaries, and local XLSX or HTML report paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query results are limited to 1,000 rows and 10 MiB; generated reports and normalized dataset copies remain in the local workspace.]

## Skill Version(s):

1.4.0 (source: server release evidence and SKILL.md metadata packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
