## Description:

Research public Marketplace listings, sellers, prices, and product details with SocQ. Use when an agent needs Facebook Marketplace-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill to collect, compare, and analyze public Facebook Marketplace listings through SocQ. It helps select the right endpoint, estimate credits, run asynchronous collection, handle pagination, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocQ API key for CLI, MCP, or REST access.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid putting keys in prompts, URLs, shell history, or project files, and use API-key limits where available.

Risk: SocQ requests may spend credits, especially for large-volume or multi-endpoint collection.

Mitigation: Check account balance and endpoint billing before submission, estimate expected cost, use smaller result caps when appropriate, and obtain confirmation for larger paid runs.

Risk: Marketplace collection may be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Report result counts, pages read, failed requests, unsupported filters, and whether more data remains instead of claiming complete coverage.

Risk: The skill sends public Facebook Marketplace queries to SocQ.

Mitigation: Confirm the user is comfortable using SocQ for the requested public Marketplace research before installing or running the integration.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [Facebook Marketplace API Platform Page](https://socq.ai/apis/facebook-marketplace)
- [Facebook Marketplace API Documentation](https://docs.socq.ai/api-manual/facebook-marketplace)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Facebook Marketplace Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [guidance, text, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands, endpoint summaries, task status, normalized findings, and optional raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, credit estimates, pagination status, and notes on incomplete coverage.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
