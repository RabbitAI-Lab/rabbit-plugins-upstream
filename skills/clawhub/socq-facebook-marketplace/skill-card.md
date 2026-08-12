## Description:

Research public Marketplace listings, sellers, prices, and product details with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to collect, compare, and analyze public Facebook Marketplace listings, sellers, prices, and product details through SocQ endpoints while preserving cost, pagination, and task-status context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires SocQ API-key configuration and network calls to SocQ.

Mitigation: Keep SOCQ_API_KEY in the environment and do not place keys in prompts, URLs, committed files, or retained commands.

Risk: Large-volume or multi-endpoint collections can incur SocQ credit charges.

Mitigation: Report expected cost, check account limits when appropriate, and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: Marketplace research may be incomplete when pagination stops early, a provider fails, or filters are unsupported.

Mitigation: Report pages read, result count, remaining pagination, failed requests, unsupported filters, and incomplete coverage.

## Reference(s):

- [SocQ website](https://socq.ai/)
- [SocQ Facebook Marketplace platform page](https://socq.ai/apis/facebook-marketplace)
- [SocQ Facebook Marketplace API documentation](https://docs.socq.ai/api-manual/facebook-marketplace)
- [SocQ API key dashboard](https://socq.ai/dashboard/api-key)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [SocQ devtools homepage](https://github.com/SocQAPI/socq-devtools)
- [Facebook Marketplace endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous tasks](references/async-tasks.md)
- [Pagination and files](references/pagination.md)
- [Errors and recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with endpoint selections, command/API examples, task status, cost notes, and normalized findings or export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination state, credit estimates, terminal status, and incomplete-coverage notes.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
