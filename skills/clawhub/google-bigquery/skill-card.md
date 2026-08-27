## Description:

Google BigQuery API integration with managed OAuth for running SQL queries, managing datasets and tables, and analyzing data at scale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data analysts, and agent users use this skill to access BigQuery through Maton-managed OAuth, list resources, run SQL queries, and manage projects, datasets, tables, and jobs. It is intended for workflows that need explicit user confirmation before connection creation or data-changing BigQuery operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent access to BigQuery data through a Maton-connected Google account.

Mitigation: Use OAuth where possible, connect only the needed account and scopes, and specify the intended connection when more than one exists.

Risk: Queries or API calls may create, modify, delete, insert, cancel, or export BigQuery data.

Mitigation: Require explicit user confirmation before any data-changing operation and prefer read or list calls first.

Risk: Credentials or provider-issued tokens could be exposed if printed, logged, stored, or passed through commands.

Mitigation: Keep credentials in the Maton or operating system credential store and do not print, persist, or transmit tokens outside the intended Maton API flow.

## Reference(s):

- [Google BigQuery REST API](https://cloud.google.com/bigquery/docs/reference/rest)
- [BigQuery Datasets API](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets)
- [BigQuery Tables API](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables)
- [BigQuery Jobs API](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs)
- [BigQuery Standard SQL Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces BigQuery API call guidance through the Maton CLI; API responses may include JSON returned by BigQuery.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
