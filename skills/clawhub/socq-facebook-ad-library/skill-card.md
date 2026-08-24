## Description:

Research public ads, advertisers, creatives, and campaign activity with SocQ. Use when an agent needs Facebook Ad Library-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research teams use this skill to collect, page through, and analyze public Facebook Ad Library ads, advertisers, creatives, and campaign activity through SocQ.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocQ API key for CLI, MCP, or REST access.

Mitigation: Keep SOCQ_API_KEY in the environment and out of prompts, URLs, committed files, retained commands, and command history.

Risk: SocQ requests are credit-metered, and large or multi-endpoint collections can consume paid credits.

Mitigation: Check expected endpoint costs and account limits, reduce scope when needed, and obtain user confirmation before paid large-volume or multi-endpoint runs.

Risk: Facebook Ad Library collections can be incomplete when pagination stops early, providers fail, or requested filters are unsupported.

Mitigation: Report pages read, whether more data remains, unsupported filters, failed requests, and any incomplete coverage rather than claiming completeness.

Risk: Raw exports may be large externally retrieved public ad-library datasets.

Mitigation: Use normalized standard views for routine reporting and retrieve raw files only when complete source payloads are required.

## Reference(s):

- [SocQ Skill Page](https://clawhub.ai/socq/skills/socq-facebook-ad-library)
- [SocQ Developer Tools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [Facebook Ad Library Platform Page](https://socq.ai/apis/facebook-ad-library)
- [Facebook Ad Library API Documentation](https://docs.socq.ai/api-manual/facebook-ad-library)
- [SocQ MCP and CLI Documentation](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Facebook Ad Library Endpoint Reference](references/platform.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, API calls]

**Output Format:** [Markdown with endpoint summaries, command examples, task status, credit usage, normalized findings, and optional raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include SocQ task IDs, pagination state, expected and reported credit usage, and notes about incomplete coverage.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
