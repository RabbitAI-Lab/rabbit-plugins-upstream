## Description:

Analyzes local CSV, JSON, XLSX, and Parquet files with natural-language questions or read-only SQL, then generates local XLSX or HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to inspect local tabular files, run read-only SQL, answer data questions, and create local reports without uploading raw data to the platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package is flagged suspicious because release trust material appears missing or unstamped.

Mitigation: Review before installation and install only after the publisher ships RELEASE/SHA256SUMS, nonempty trusted keys, real stamped platform settings, executable scripts, and updated dependency pins.

Risk: Local data analysis can expose sensitive information if users select unintended files or share generated outputs.

Mitigation: Use only intended local files, keep SQL_DATA_ANALYST_API_KEY out of prompts, logs, reports, and repositories, review generated SQL and summaries, and respect truncation indicators.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/sql-data-analyst)
- [AI Skills homepage](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/API-KEY.md)
- [Local execution workflow](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/USAGE.md)
- [Privacy and security boundaries](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/SECURITY.md)
- [Billing](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/BILLING.md)
- [Authorization API](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with SQL, shell commands, JSON results, and generated local XLSX or HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local runner output is bounded by read-only SQL policy, query timeouts, row and byte limits, and report-generation safeguards.]

## Skill Version(s):

1.5.0 (source: server release metadata and skill metadata packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
