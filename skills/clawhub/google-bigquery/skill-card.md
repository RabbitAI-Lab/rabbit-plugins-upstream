## Description:

Google BigQuery API integration with managed OAuth for running SQL queries, managing datasets and tables, and analyzing data at scale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and data teams use this skill to query BigQuery projects, inspect and manage datasets or tables, and run approved analytics jobs through a Maton-managed Google BigQuery connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton-mediated BigQuery access can reach business data authorized by the user's connection.

Mitigation: Use OAuth, prefer read-only calls first, confirm writes and deletes, and select only the scopes needed for the task.

Risk: Hosted functions, triggers, and destinations can create persistent automation against connected accounts.

Mitigation: Require explicit approval, keep functions narrowly scoped, use restrictive network policy where possible, and remove automation when it is no longer needed.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key.

Mitigation: Use the CLI when available; if raw HTTP is necessary, keep the key out of logs, command lines, files, and user-visible output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-bigquery)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [BigQuery API overview](https://cloud.google.com/bigquery/docs/reference/rest)
- [BigQuery datasets API](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets)
- [BigQuery tables API](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables)
- [BigQuery jobs API](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs)
- [BigQuery standard SQL reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)
- [GitHub trigger reference](references/github/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce BigQuery API request guidance, CLI commands, raw HTTP examples, hosted function snippets, and trigger configuration guidance.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
