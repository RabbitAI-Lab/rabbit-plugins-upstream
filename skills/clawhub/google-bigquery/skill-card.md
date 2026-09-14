## Description:

Google BigQuery API integration with managed OAuth for running SQL queries, managing datasets and tables, and analyzing data at scale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data engineers, and analysts use this skill to connect an authorized Google BigQuery account, run BigQuery API calls, inspect projects, query data, and manage datasets or tables with user approval for sensitive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Homebrew installation depends on trusting and verifying the Maton tap.

Mitigation: Prefer the pinned NPM install command, or verify and pin the Homebrew tap before relying on it.

Risk: BigQuery write, delete, and query jobs can change data, disclose sensitive data, or create cost exposure.

Mitigation: Use the least-privileged BigQuery account needed and review every write, delete, and data-changing query before execution.

Risk: Hosted functions, triggers, or destinations can create persistent automation that runs without repeated manual prompts.

Mitigation: Create persistent automation only after explicit approval, keep function network access restricted where possible, and delete automation when it is no longer needed.

Risk: Long-lived API keys can be exposed through shell environments or child processes.

Mitigation: Prefer OAuth-backed Maton login and operating-system credential storage; use raw API keys only where the CLI cannot be installed.

## Reference(s):

- [Google BigQuery skill on ClawHub](https://clawhub.ai/byungkyu/skills/google-bigquery)
- [byungkyu publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Google BigQuery REST API reference](https://cloud.google.com/bigquery/docs/reference/rest)
- [BigQuery datasets REST reference](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON examples, code snippets, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should default to read/list workflows and ask for explicit user approval before writes, connection creation, deletion, hosted functions, triggers, or other persistent automation.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact metadata version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
