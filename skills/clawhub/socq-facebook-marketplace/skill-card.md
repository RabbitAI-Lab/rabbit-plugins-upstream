## Description:

Research public Facebook Marketplace listings, sellers, prices, and product details with SocQ through endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports via CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to collect and analyze public Facebook Marketplace listings, sellers, prices, locations, and product details through SocQ. It guides endpoint selection, credit estimation, task submission, polling, pagination, and export retrieval through MCP, CLI, or REST.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace research inputs and target details are sent to SocQ for collection.

Mitigation: Use the skill only when SocQ processing is acceptable, and collect only public data supported by the selected endpoint.

Risk: SOCQ_API_KEY may authorize billable requests.

Mitigation: Report expected credits, obtain confirmation before large-volume or multi-endpoint runs, and use API key rate, IP, and credit limits where available.

Risk: Ad hoc npx execution can use an unpinned CLI package.

Mitigation: Prefer the configured hosted MCP server or a pinned, vetted @socq/cli installation.

Risk: Results may be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Preserve task IDs, report pages read and terminal status, and label unsupported filters, failed requests, and incomplete coverage.

## Reference(s):

- [SocQ Devtools Homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ Facebook Marketplace Platform](https://socq.ai/apis/facebook-marketplace)
- [SocQ Facebook Marketplace API Documentation](https://docs.socq.ai/api-manual/facebook-marketplace)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Facebook Marketplace Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with endpoint selections, CLI/MCP/REST commands, cost estimates, task status, normalized findings, and raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination state, reported credit usage, failed requests, unsupported filters, and incomplete coverage notes.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
