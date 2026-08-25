## Description:

Research public Google Play content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to collect and analyze public Google Play app details, rankings, and reviews through SocQ. It helps select endpoints, validate inputs, estimate credits, submit asynchronous tasks, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys could be exposed through prompts, URLs, command history, or committed files.

Mitigation: Keep SOCQ_API_KEY in the environment, prefer configured MCP or CLI authentication, and avoid placing keys in prompts, URLs, retained commands, or files.

Risk: Large or multi-endpoint collections can consume credits unexpectedly.

Mitigation: Review endpoint billing and account limits, report expected costs, reduce result limits when appropriate, and obtain explicit approval before broad paid collection.

Risk: Async task failures, early pagination stops, or unsupported filters can make results incomplete.

Mitigation: Poll tasks to a terminal status, preserve task IDs, follow pagination cursors until the requested cap or completion, and label incomplete coverage or unsupported filters.

Risk: Blind retries can duplicate paid work or hide the normalized cause of failure.

Mitigation: Inspect normalized errors, respect rate and credit reset guidance, and reuse idempotency keys when retrying the same submission after transient failures.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Google Play API Documentation](https://docs.socq.ai/api-manual/google-play)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Google Play Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, execution path, task status, credit usage, normalized findings, and optional shell commands or raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination status, incomplete coverage notes, failed request details, and unsupported filter labels.]

## Skill Version(s):

1.0.0 (source: server release metadata and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
