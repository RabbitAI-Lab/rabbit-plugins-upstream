## Description:

Research public Reddit content, accounts, keywords, and performance data with SocQ. Use when an agent needs Reddit-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to collect and analyze public Reddit posts, comments, subreddit activity, keyword search results, and related performance data through SocQ. It helps select endpoints, estimate credits, run asynchronous tasks, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SOCQ_API_KEY is a paid credential that authenticates CLI, MCP, and REST requests.

Mitigation: Keep the key in the environment or local SocQ configuration, never place it in prompts, URLs, committed files, or retained commands, and clear it when access is no longer needed.

Risk: Large-volume or multi-endpoint Reddit collections can consume credits.

Mitigation: Check expected cost and account limits first, reduce scope when needed, and obtain user confirmation before starting paid large-volume or multi-endpoint runs.

Risk: Results may be incomplete when pagination stops early, a provider fails, or requested filters are unsupported.

Mitigation: Report task status, result count, pages read, unsupported filters, failed requests, and whether more data remains; avoid claiming completeness when coverage is incomplete.

Risk: The skill is intended for public Reddit research and can over-collect if scope is not constrained.

Mitigation: Collect only public data supported by the selected endpoint and avoid exporting more Reddit data than the user requested.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Reddit Platform](https://socq.ai/apis/reddit)
- [SocQ Reddit API Documentation](https://docs.socq.ai/api-manual/reddit)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Platform Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with endpoint summaries, command or API examples, task status, and normalized findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, credit estimates, pagination status, result counts, and raw export locations when available]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
