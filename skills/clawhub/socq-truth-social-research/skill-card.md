## Description:

Research public Truth Social content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to collect and analyze public Truth Social profiles, posts, and account timelines through SocQ endpoints. It helps select endpoints, estimate credit usage, run asynchronous tasks, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SocQ external services and requires a SOCQ_API_KEY tied to an account.

Mitigation: Trust SocQ for submitted public research queries, keep the key out of prompts and retained commands, and use key limits such as rate, IP, or credit controls when available.

Risk: Large or multi-endpoint runs can consume paid SocQ credits.

Mitigation: Estimate costs, check account limits, reduce scope when needed, and obtain user confirmation before paid large-volume or multi-endpoint collection.

Risk: Results can be incomplete when pagination stops early, a provider fails, or requested filters are unsupported.

Mitigation: Report pages read, remaining pagination, failed requests, unsupported filters, and coverage gaps instead of claiming completeness.

## Reference(s):

- [SocQ Truth Social API Documentation](https://docs.socq.ai/api-manual/truth-social)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [Platform Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration, Text, Markdown]

**Output Format:** [Markdown with endpoint choices, commands or API calls, task status, cost notes, normalized findings, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, pagination state, credit estimates, result counts, and coverage caveats.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
