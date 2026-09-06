## Description:

Google BigQuery API integration with managed OAuth for running SQL queries, managing datasets and tables, and analyzing data at scale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data practitioners use this skill to query BigQuery, inspect projects, datasets, tables, and jobs, and prepare reviewed BigQuery API operations through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing a connection grants Maton access to the intended BigQuery account.

Mitigation: Install only when comfortable with Maton authorization, choose the narrowest Google scopes available, and revoke unused connections.

Risk: BigQuery writes, deletes, and job-running operations can alter data or incur cost.

Mitigation: Default to read and list operations, then require explicit review and approval of the target resource, payload, and intended effect before mutating or cost-bearing actions.

Risk: Multiple Maton accounts or BigQuery connections can route a request to the wrong account.

Mitigation: Specify the intended connection and profile when more than one is available.

## Reference(s):

- [Maton](https://maton.ai)
- [BigQuery API Overview](https://cloud.google.com/bigquery/docs/reference/rest)
- [BigQuery Datasets API](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets)
- [BigQuery Tables API](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables)
- [BigQuery Jobs API](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs)
- [BigQuery Tabledata API](https://cloud.google.com/bigquery/docs/reference/rest/v2/tabledata)
- [BigQuery Standard SQL Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash, JSON, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include BigQuery REST paths, JSON request bodies, and Maton CLI commands; write, delete, connection creation, and job-running operations require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
