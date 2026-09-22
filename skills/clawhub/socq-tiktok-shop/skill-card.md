## Description:

Research public TikTok Shop products, shops, creators, categories, and sales signals with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to select and run SocQ endpoints for public TikTok Shop research, including product, shop, creator, review, search, pagination, credit-estimation, and raw-export workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends TikTok Shop research inputs to SocQ's hosted service and requires a SocQ API key.

Mitigation: Use a dedicated API key with limits or allowlists, keep SOCQ_API_KEY in the environment, and avoid placing credentials in prompts, URLs, committed files, or retained commands.

Risk: SocQ requests are credit-metered, so broad or repeated collections can spend credits unexpectedly.

Mitigation: Estimate costs, check account balance or limits, reduce result scope when needed, and get confirmation before paid large-volume or multi-endpoint runs.

Risk: Using npx or an unpinned CLI fallback can execute a newer package version than the reviewed artifact expects.

Mitigation: Prefer a trusted preinstalled or pinned @socq/cli version when operating in controlled environments.

Risk: Pagination stops, provider failures, unsupported filters, or differing date windows can make findings incomplete or hard to compare.

Mitigation: Report pagination state, failed requests, unsupported filters, collection time, and any differences in date windows, filters, locales, or content types.

## Reference(s):

- [SocQ TikTok Shop API Documentation](https://docs.socq.ai/api-manual/tiktok-shop)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [TikTok Shop Endpoint Reference](artifact/references/platform.md)
- [Authentication](artifact/references/authentication.md)
- [Billing and Cost Control](artifact/references/billing.md)
- [Asynchronous Tasks](artifact/references/async-tasks.md)
- [Pagination and Files](artifact/references/pagination.md)
- [Errors and Recovery](artifact/references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with endpoint selections, SocQ MCP/CLI/REST commands, task status, cost notes, and normalized findings or raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference SocQ task IDs, credit usage, pagination state, incomplete coverage, unsupported filters, and raw JSONL export locations when available.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
