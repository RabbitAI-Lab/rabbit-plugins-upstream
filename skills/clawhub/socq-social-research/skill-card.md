## Description:

Research public social-platform content, accounts, keywords, and SEO search data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and marketing researchers use this skill to collect, compare, and analyze public social-platform and SEO data through SocQ endpoints. It helps select endpoints, estimate credits, submit asynchronous jobs, poll results, paginate records, and report coverage limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research targets, URLs, keywords, and public social data requests are sent to SocQ.

Mitigation: Use the skill only for lawful public-data collection with clear scope and retention limits.

Risk: Paid, large-volume, cross-platform, or multi-endpoint jobs can consume credits.

Mitigation: Estimate costs, check account limits, and obtain user confirmation before submitting broad collection jobs.

Risk: Ad hoc package execution can introduce supply-chain exposure.

Mitigation: Prefer pinned reviewed package versions over unpinned npx execution.

Risk: API keys can authorize spending and data access.

Mitigation: Keep SOCQ_API_KEY out of prompts, URLs, committed files, and retained commands; set spending and rate limits on the key.

Risk: Results can be incomplete when pagination stops early, providers fail, or filters are unsupported.

Mitigation: Report task status, result counts, remaining pages, failed platforms, unsupported filters, and any coverage limits.

## Reference(s):

- [SocQ Developer Tools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Platform Catalog](https://socq.ai/platforms)
- [SocQ API Documentation](https://docs.socq.ai/api-manual)
- [SocQ MCP and CLI](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Capability Catalog](references/catalog.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [Cross-platform Research](references/cross-platform.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, text]

**Output Format:** [Markdown guidance with endpoint selections, command examples, task status summaries, and normalized research findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include credit estimates, task IDs, result counts, pagination status, raw export locations, failed platforms, unsupported filters, and incomplete coverage notes.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
