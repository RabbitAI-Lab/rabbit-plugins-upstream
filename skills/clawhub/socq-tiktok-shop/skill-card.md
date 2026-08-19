## Description:

Research public TikTok Shop products, shops, creators, categories, and sales signals with SocQ for endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to collect and analyze public TikTok Shop data with SocQ, including endpoint selection, cost estimation, task polling, pagination, and exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ requests can spend API credits, especially for large-volume or multi-endpoint research.

Mitigation: Report expected costs before submission, obtain confirmation for large paid runs, and reduce scope when the user has not authorized broad collection.

Risk: SOCQ_API_KEY exposure could allow unauthorized SocQ usage.

Mitigation: Keep the key in environment variables, never place it in prompts, URLs, committed files, or retained commands, and use API-key limits where available.

Risk: Research results can be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Report pages read, whether more data remains, failed requests, unsupported filters, and incomplete coverage instead of claiming completeness.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ TikTok Shop Platform](https://socq.ai/apis/tiktok-shop)
- [SocQ TikTok Shop API Documentation](https://docs.socq.ai/api-manual/tiktok-shop)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Asynchronous Tasks](references/async-tasks.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Errors and Recovery](references/errors.md)
- [Pagination and Files](references/pagination.md)
- [TikTok Shop Endpoint Reference](references/platform.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with command or API call examples and result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoints, execution path, credit estimates and usage, task IDs, pagination status, normalized findings, and raw export locations.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
