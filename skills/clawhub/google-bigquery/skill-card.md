## Description:

Guides agents in querying and managing Google BigQuery datasets, tables, and jobs through a Maton-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query BigQuery data, manage datasets and tables, and run analytics jobs. With separate approval, they can set up scheduled or event-driven BigQuery actions through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Maton connection can access BigQuery resources within the permissions the user grants.

Mitigation: Authorize only the needed account and scopes, and keep credentials out of logs and outputs.

Risk: Writes, deletions, and hosted functions can change data or run actions without further interaction.

Mitigation: Start with read-only calls and confirm each target, payload, and intended effect before making a change or deploying a function.

Risk: Triggers and destinations can run repeatedly or forward event data to another service.

Mitigation: Approve each trigger and destination separately; avoid third-party forwarding unless the user explicitly requests it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/byungkyu/skills/google-bigquery)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [BigQuery REST API](https://cloud.google.com/bigquery/docs/reference/rest)
- [GoogleSQL query syntax](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, SQL, Shell commands, Code]

**Output Format:** [Markdown with SQL, shell, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account and an authorized BigQuery connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
