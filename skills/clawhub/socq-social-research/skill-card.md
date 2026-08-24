## Description:

Research public social-platform content, accounts, keywords, and SEO search data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external research teams use this skill to collect, compare, monitor, and analyze public social-platform and SEO data through SocQ endpoints. It supports endpoint discovery, credit estimation, asynchronous task submission and polling, pagination, and normalized result reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research targets, keywords, domains, URLs, and task results are sent to SocQ.

Mitigation: Use the skill only for approved public-data research and avoid submitting confidential or internal targets without authorization.

Risk: Credit-metered requests can incur cost, especially for large-volume, cross-platform, or multi-endpoint runs.

Mitigation: Estimate endpoint credits, check account limits, reduce scope when needed, and obtain confirmation before starting large paid runs.

Risk: API keys can be exposed through prompts, URLs, shell history, or retained commands.

Mitigation: Keep SOCQ_API_KEY in the environment or approved local configuration and avoid placing credentials in prompts, URLs, committed files, or command history.

Risk: Pagination limits, provider failures, unsupported filters, or early stops can make results incomplete or hard to compare.

Mitigation: Track task IDs and pagination state, label incomplete coverage, and compare platforms only across compatible windows, filters, locales, and content types.

Risk: Public social and SEO data can be misused for bulk profiling or surveillance.

Mitigation: Use the skill for lawful, authorized research and avoid bulk profiling, surveillance, or other non-consensual targeting workflows.

## Reference(s):

- [SocQ ClawHub Skill Page](https://clawhub.ai/socq/skills/socq-social-research)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Platform Catalog](https://socq.ai/platforms)
- [SocQ API Documentation](https://docs.socq.ai/api-manual)
- [SocQ MCP and CLI Documentation](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Capability Catalog](references/catalog.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [Cross-platform Research](references/cross-platform.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls, text]

**Output Format:** [Markdown with endpoint selections, commands or API call details, task status, cost notes, normalized findings, and raw export locations when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, pagination state, result counts, terminal statuses, incomplete coverage notes, and expected or reported credit usage.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
