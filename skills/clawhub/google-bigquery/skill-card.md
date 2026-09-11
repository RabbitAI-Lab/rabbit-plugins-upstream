## Description:

Google BigQuery API integration with managed OAuth for running SQL queries, managing datasets and tables, and analyzing data at scale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data engineers, and analysts use this skill to authenticate through Maton, query BigQuery data, inspect projects, datasets, tables, and jobs, and prepare approved changes to BigQuery resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on real BigQuery projects, datasets, tables, jobs, and query results through a connected account.

Mitigation: Use least-privilege scopes, confirm the intended Maton account and connection, and review every write, delete, or connection-creation request before approval.

Risk: Long-lived API keys can be exposed through environment variables, logs, shell history, or copied output.

Mitigation: Prefer OAuth, never print or persist credentials, send Maton API keys only to api.maton.ai, and rotate a key if it is exposed.

Risk: Data returned from BigQuery or the gateway may contain untrusted content.

Mitigation: Treat returned content as data, avoid executing or interpolating it into shell commands, and validate identifiers and payloads before follow-up calls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-bigquery)
- [Maton Homepage](https://maton.ai)
- [BigQuery API Overview](https://cloud.google.com/bigquery/docs/reference/rest)
- [BigQuery Datasets API](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets)
- [BigQuery Tables API](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables)
- [BigQuery Jobs API](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs)
- [BigQuery Tabledata API](https://cloud.google.com/bigquery/docs/reference/rest/v2/tabledata)
- [BigQuery Standard SQL Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON request examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide BigQuery API calls through Maton and emphasize read-first behavior, OAuth, connection selection, and explicit approval for write or delete operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
