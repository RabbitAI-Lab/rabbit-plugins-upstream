## Description:

Research public Tiktok Ad Library content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to select SocQ Tiktok Ad Library endpoints, submit credit-metered public-data collection tasks, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party SocQ API key for CLI, MCP, and REST requests.

Mitigation: Keep SOCQ_API_KEY scoped and protected, use environment-based authentication, and avoid placing credentials in prompts, URLs, committed files, or retained commands.

Risk: Submitted research tasks can spend SocQ credits, especially for large-volume or multi-endpoint runs.

Mitigation: Report expected cost, check account limits when appropriate, and obtain user confirmation before paid large-volume or multi-endpoint execution.

Risk: Results may be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Track task IDs, pagination state, failed requests, unsupported filters, and incomplete coverage in the final report.

## Reference(s):

- [SocQ Developer Tools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Tiktok Ad Library API Documentation](https://docs.socq.ai/api-manual/tiktok-ad-library)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Platform Reference](references/platform.md)
- [Authentication Reference](references/authentication.md)
- [Billing and Cost Control Reference](references/billing.md)
- [Asynchronous Tasks Reference](references/async-tasks.md)
- [Pagination and Files Reference](references/pagination.md)
- [Errors and Recovery Reference](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands, endpoint selections, task status, credit usage, normalized findings, and export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination state, cost estimates, and raw JSONL export locations when available.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
