## Description:

Research public Threads content, accounts, keywords, and performance data with SocQ. Use when an agent needs Threads-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to select and run SocQ Threads endpoints for public Threads research, including account, post, and user-post collection. It helps estimate credits, submit asynchronous jobs, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Threads research inputs, target URLs or usernames, task metadata, and the SocQ API key are used with SocQ's hosted service.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid submitting secrets or regulated data as research inputs, and do not place keys in prompts, URLs, committed files, or retained commands.

Risk: SocQ requests are credit-metered and large or multi-endpoint collections can consume credits.

Mitigation: Check the account and endpoint billing details, report expected cost, and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: Collections can be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Report result counts, pages read, remaining data, failed requests, unsupported filters, and any incomplete coverage.

Risk: Retrying failed paid requests blindly can duplicate work or spend.

Mitigation: Inspect the normalized error, preserve task IDs, reuse idempotency keys for retryable submissions, and avoid automatic duplicate submissions.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Threads Platform](https://socq.ai/apis/threads)
- [SocQ Threads API Documentation](https://docs.socq.ai/api-manual/threads)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Threads Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with endpoint choices, command or API examples, task status summaries, and normalized findings or raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, credit estimates, pagination status, failed requests, unsupported filters, and incomplete coverage notes.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
