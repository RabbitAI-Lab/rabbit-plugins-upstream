## Description:

Research public TikTok Shop products, shops, creators, categories, and sales signals with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and commerce teams use this skill to select SocQ TikTok Shop endpoints, collect public product, shop, creator, category, and sales-signal data, and summarize normalized findings with billing and pagination context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocQ API key for CLI, MCP, and REST requests.

Mitigation: Keep SOCQ_API_KEY in the environment and do not place it in prompts, URLs, committed files, or retained command history.

Risk: TikTok Shop data collection may spend SocQ credits, especially for large or multi-endpoint runs.

Mitigation: Check account balance and endpoint billing, report expected cost, obtain confirmation before large paid runs, and set account or API-key limits when credit spend matters.

Risk: Results can be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Report pages read, result counts, task status, unsupported filters, failed requests, and whether more data remains.

## Reference(s):

- [SocQ Developer Tools](https://github.com/SocQAPI/socq-devtools)
- [SocQ](https://socq.ai/)
- [TikTok Shop Platform](https://socq.ai/apis/tiktok-shop)
- [TikTok Shop API Documentation](https://docs.socq.ai/api-manual/tiktok-shop)
- [MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Async Tasks](references/async-tasks.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Errors and Recovery](references/errors.md)
- [Pagination and Files](references/pagination.md)
- [TikTok Shop Endpoint Selection](references/platform.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with endpoint summaries, task IDs, billing notes, pagination status, normalized findings, and optional shell commands or raw export references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected SocQ endpoint, execution path, input summary, credit usage, terminal task status, result count, collection caveats, and raw export location when requested.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
