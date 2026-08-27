## Description:

Analyzes local CSV, JSON, XLSX, and Parquet files with natural-language questions or read-only SQL, then produces bounded results or local XLSX/HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to analyze local CSV, JSON, XLSX, or Parquet files with natural-language questions or read-only SQL, inspect schemas, and generate local XLSX/HTML reports without uploading raw data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Processing untrusted Parquet or Arrow-related files may expose users to the vulnerable data-parsing dependency identified by the security evidence.

Mitigation: Prefer trusted local data and wait for, or upgrade to, a release with pyarrow beyond the affected Arrow versions before processing untrusted Parquet or Arrow-related files.

Risk: Paid operations send remote billing authorization metadata to the platform.

Mitigation: Use the skill only if operation, runner version, installation ID, and input fingerprint transmission is acceptable; keep API keys out of prompts, logs, reports, and repositories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/sql-data-analyst)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key configuration](references/API-KEY.md)
- [Local execution flow](references/USAGE.md)
- [Privacy and security boundaries](references/SECURITY.md)
- [Billing notes](references/BILLING.md)
- [Local authorization API](references/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with SQL snippets, shell commands, JSON summaries, and local XLSX/HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query results are bounded to 1,000 rows or 10 MiB; generated reports and source data remain local.]

## Skill Version(s):

1.3.0 (source: ClawHub release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
