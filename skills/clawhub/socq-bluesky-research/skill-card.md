## Description:

Research public Bluesky content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research agents use this skill to select SocQ Bluesky endpoints, estimate credit usage, submit authenticated collection tasks, poll asynchronous results, paginate responses, and report normalized public Bluesky findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bluesky research requests and SocQ authorization are sent to SocQ's hosted service.

Mitigation: Configure SOCQ_API_KEY carefully, keep it out of prompts, URLs, committed files, and retained commands, and use environment-based authentication.

Risk: Paid SocQ API credits may be consumed, especially for large-volume or multi-endpoint runs.

Mitigation: Report expected cost, check account or key limits, reduce scope when needed, and obtain confirmation before large paid runs.

Risk: Ad hoc npx execution can fetch the current CLI package at runtime.

Mitigation: Prefer a pinned or preinstalled @socq/cli when operating in controlled environments.

Risk: Pagination, provider failures, unsupported filters, or early stopping can make research coverage incomplete.

Mitigation: Track pages read and has_more status, preserve task IDs for resumption, label incomplete coverage, and avoid claiming completeness when collection stops early.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Bluesky API Documentation](https://docs.socq.ai/api-manual/bluesky)
- [SocQ MCP and CLI Documentation](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Bluesky Platform Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, text, markdown]

**Output Format:** [Markdown guidance with endpoint summaries, inline CLI or REST examples, task status, credit usage, result counts, normalized findings, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference SocQ task IDs, pagination cursors, credit estimates, terminal statuses, unsupported filters, incomplete coverage, and paid API usage.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
