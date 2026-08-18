## Description:

Research public Rednote content, accounts, keywords, and performance data with SocQ for endpoint selection, collection, pagination, and exports through MCP, CLI, or REST.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, analysts, and developers use this skill to collect and analyze public Rednote notes, creators, comments, and keyword results with SocQ while tracking endpoint choice, credits, task state, and pagination limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rednote URLs, queries, user IDs, and related research parameters are sent to SocQ under the user's SocQ account.

Mitigation: Use a scoped SOCQ_API_KEY where possible, collect only public data supported by the selected endpoint, and avoid placing keys in prompts, URLs, committed files, or command history.

Risk: Large or multi-endpoint collection can consume SocQ credits.

Mitigation: Check endpoint billing and account balance, cap results or pages to the approved scope, and obtain confirmation before broad paid runs.

Risk: Asynchronous or paginated collection can be incomplete if polling stops early, pagination is capped, or a provider fails.

Mitigation: Preserve task IDs, poll to a terminal status, follow opaque next_cursor values only through the approved cap, and label incomplete coverage in the final report.

Risk: Blind retries after paid failures, rate limits, or validation errors can duplicate work or spend.

Mitigation: Read the normalized error, respect retry guidance such as Retry-After, reuse idempotency keys for retried submissions, and do not resubmit failed paid tasks automatically.

## Reference(s):

- [SocQ Rednote API Documentation](https://docs.socq.ai/api-manual/rednote)
- [SocQ MCP and CLI Documentation](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [Rednote Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown reports with endpoint summaries, task status, normalized findings, optional shell commands, and raw export file locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, credit usage, task ID, pagination status, limitations, and raw JSONL export location when requested.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
