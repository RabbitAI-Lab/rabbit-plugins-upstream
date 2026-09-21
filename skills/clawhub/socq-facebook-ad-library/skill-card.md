## Description:

Research public ads, advertisers, creatives, and campaign activity with SocQ. Use when an agent needs Facebook Ad Library-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to collect and analyze public Facebook Ad Library ads, advertisers, creatives, and campaign activity through SocQ. It helps choose endpoints, estimate credits, submit asynchronous tasks, page through results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SocQ's hosted service and requires a SOCQ_API_KEY.

Mitigation: Install it only for SocQ Facebook Ad Library workflows, keep the key in the environment, and avoid placing credentials in prompts, URLs, committed files, or retained commands.

Risk: Running an unpinned npx fallback can increase supply-chain risk.

Mitigation: Prefer a vetted or pinned SocQ CLI installation when lower supply-chain risk is required.

Risk: Large or multi-endpoint collections can consume paid credits.

Mitigation: Check account balance and endpoint billing before submission, reduce scope when needed, and get user confirmation before large paid runs.

Risk: Collected results may be incomplete when pagination stops early, providers fail, filters are unsupported, or date windows differ.

Mitigation: Report pagination state, failed requests, unsupported filters, collection time, and differences in date windows, filters, locales, or content types.

## Reference(s):

- [SocQ](https://socq.ai/)
- [SocQ Facebook Ad Library Platform](https://socq.ai/apis/facebook-ad-library)
- [SocQ Facebook Ad Library API Documentation](https://docs.socq.ai/api-manual/facebook-ad-library)
- [SocQ MCP and CLI Documentation](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [Facebook Ad Library Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summaries with endpoint and execution details, task status, credit usage, result counts, normalized findings, and optional raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ MCP, CLI, or REST execution paths and task IDs; raw exports are referenced by location when requested.]

## Skill Version(s):

1.0.4 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
