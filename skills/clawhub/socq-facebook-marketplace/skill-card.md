## Description:

Research public Facebook Marketplace listings, sellers, prices, and product details with SocQ, including endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports through SocQ CLI, MCP, or REST.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to collect and analyze public Facebook Marketplace listings with SocQ while tracking endpoint choice, credit cost, task status, pagination, and coverage limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends public Facebook Marketplace research requests through SocQ services and requires a SOCQ_API_KEY.

Mitigation: Install only when SocQ use is intended, keep SOCQ_API_KEY in the environment, and avoid placing credentials in prompts, URLs, retained commands, or committed files.

Risk: SocQ requests are credit-metered and larger or multi-endpoint jobs can spend account credits.

Mitigation: Review expected credit cost, check account limits, and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: Runtime npx installation can fetch the current SocQ CLI package at execution time.

Mitigation: Prefer a preinstalled or pinned socq CLI when reproducibility or supply-chain control is required.

## Reference(s):

- [SocQ Facebook Marketplace skill page](https://clawhub.ai/socq/skills/socq-facebook-marketplace)
- [SocQ devtools homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ Facebook Marketplace API documentation](https://docs.socq.ai/api-manual/facebook-marketplace)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Facebook Marketplace endpoint reference](references/platform.md)
- [Authentication reference](references/authentication.md)
- [Billing and cost control reference](references/billing.md)
- [Asynchronous task reference](references/async-tasks.md)
- [Pagination and files reference](references/pagination.md)
- [Error handling reference](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, task status, credit usage, normalized findings, and optional shell commands or raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include result counts, pages read, whether more data remains, collection time, failed requests, unsupported filters, and incomplete coverage notes.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
