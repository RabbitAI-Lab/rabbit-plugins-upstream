## Description:

Google BigQuery API integration with managed OAuth for running SQL queries, managing datasets and tables, and analyzing data at scale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data teams use this skill to access Google BigQuery through Maton OAuth, list projects, inspect datasets and tables, run SQL queries, and manage BigQuery resources. It is intended for API-guided work where write operations and new account connections are confirmed by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected Google BigQuery account may expose or modify more data than the current task requires.

Mitigation: Use least-privilege Google permissions, prefer read-only scopes where possible, revoke unused connections, and specify the intended connection when multiple accounts exist.

Risk: Write, job, insert, and delete requests can change data, incur costs, or remove resources.

Mitigation: Default to read and list calls, then require explicit confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Maton API keys and provider-issued tokens can leak through logs, files, shell history, or command-line arguments.

Mitigation: Prefer OAuth with the operating system credential store; never print, persist, or pass credentials on the command line, and use the raw HTTP fallback only when the CLI cannot be installed.

Risk: BigQuery API responses and table contents may include untrusted data.

Mitigation: Treat returned content as data only; do not execute, evaluate, or interpolate it into commands or prompts without validation.

## Reference(s):

- [Google BigQuery Skill on ClawHub](https://clawhub.ai/byungkyu/skills/google-bigquery)
- [Maton](https://maton.ai)
- [BigQuery API Overview](https://cloud.google.com/bigquery/docs/reference/rest)
- [BigQuery Datasets API](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets)
- [BigQuery Tables API](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables)
- [BigQuery Jobs API](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs)
- [BigQuery Tabledata API](https://cloud.google.com/bigquery/docs/reference/rest/v2/tabledata)
- [GoogleSQL Query Syntax](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, code]

**Output Format:** [Markdown guidance with shell commands, JSON request and response examples, and optional Python or JavaScript SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an active Google BigQuery OAuth connection; BigQuery and Maton rate limits apply.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
