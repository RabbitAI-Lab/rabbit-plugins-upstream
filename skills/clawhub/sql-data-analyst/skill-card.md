## Description:

SQL Data Analyst helps OpenClaw users analyze local CSV, JSON, XLSX, and Parquet files with natural-language questions or read-only SQL, then create local XLSX or HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External OpenClaw users and developers use this skill to inspect local tabular files, ask data questions, run bounded read-only SQL, and generate local XLSX or HTML reports. It is intended for local data analysis with metered platform authorization and an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles local user files while the server security summary flags a vulnerable pinned data-parsing dependency.

Mitigation: Install only from a trusted publisher, analyze trusted local files, and avoid untrusted Parquet or Arrow-family data until the dependency is patched.

Risk: A remote billing authorization call and API key are required for metered operations.

Mitigation: Configure the API key only through the documented environment variable and do not paste the full key into chat, logs, reports, SQL, or repositories.

Risk: Query outputs are intentionally bounded and may be truncated.

Mitigation: Disclose truncation or sample limits when explaining results and avoid presenting limited output as a complete dataset.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/sql-data-analyst)
- [AI Skills Homepage](https://ai-skills.open-idea.net)
- [API Key Configuration](artifact/references/API-KEY.md)
- [Local Execution Flow](artifact/references/USAGE.md)
- [Privacy and Security Boundaries](artifact/references/SECURITY.md)
- [Billing Notes](artifact/references/BILLING.md)
- [Local Authorization API](artifact/references/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with SQL and shell command snippets; runner outputs include JSON results and local XLSX or HTML report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query results are bounded and may be truncated; reports remain in the local workspace.]

## Skill Version(s):

1.2.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
