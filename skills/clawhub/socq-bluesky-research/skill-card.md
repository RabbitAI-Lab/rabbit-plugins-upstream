## Description:

Research public Bluesky content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to collect, paginate, and analyze public Bluesky posts and profiles through SocQ's MCP, CLI, or REST workflows while tracking task status and credit usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ requests send public Bluesky research targets, query terms, and task requests to SocQ under SOCQ_API_KEY.

Mitigation: Avoid submitting secrets, private data, or regulated information, and keep SOCQ_API_KEY in the environment rather than prompts, URLs, files, or retained commands.

Risk: Bluesky collection is credit-metered and API keys may have rate or credit limits.

Mitigation: Inspect expected costs before large or multi-endpoint runs, obtain user confirmation, and prefer API-key credit and rate limits in controlled environments.

Risk: Results can be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Report pages read, remaining data, failed requests, unsupported filters, and incomplete coverage instead of claiming completeness.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Bluesky API Documentation](https://docs.socq.ai/api-manual/bluesky)
- [SocQ MCP and CLI Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Bluesky Platform Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, task status, credit usage, result counts, findings, and optional shell commands or export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include normalized SocQ results, pagination status, task IDs, and incomplete-coverage notes.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
