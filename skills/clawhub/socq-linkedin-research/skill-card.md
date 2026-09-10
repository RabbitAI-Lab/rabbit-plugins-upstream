## Description:

Research public LinkedIn content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to collect and analyze public LinkedIn profiles, companies, jobs, posts, comments, and search results through SocQ endpoints while managing authentication, billing, asynchronous tasks, pagination, and raw exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn URLs, search terms, retrieved public LinkedIn data, and the SocQ API key are used with SocQ services.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid placing credentials in prompts, URLs, committed files, or retained commands, and collect only public data supported by the selected endpoint.

Risk: Some SocQ runs consume paid credits, and large-volume or multi-endpoint runs can incur unintended cost.

Mitigation: Report expected cost, check account or endpoint billing details, reduce scope when needed, and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: Results can be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Report result counts, pages read, remaining pagination state, failed requests, unsupported filters, and incomplete coverage instead of claiming completeness.

Risk: Installing an unpinned @socq/cli package can conflict with strict supply-chain controls.

Mitigation: Prefer a pinned @socq/cli version or managed install in controlled environments.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ LinkedIn API](https://socq.ai/apis/linkedin)
- [LinkedIn API Documentation](https://docs.socq.ai/api-manual/linkedin)
- [SocQ MCP and CLI](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [LinkedIn Platform Reference](references/platform.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown with endpoint choices, command or API guidance, task status, credit usage, result summaries, and optional raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, pagination state, terminal status, and notes about incomplete coverage or unsupported filters.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
