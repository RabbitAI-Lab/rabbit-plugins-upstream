## Description:

Research public ads, advertisers, creatives, and campaign activity with SocQ. Use when an agent needs Facebook Ad Library-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to select SocQ Facebook Ad Library endpoints, collect public ad data, manage asynchronous tasks and pagination, estimate credits, and summarize normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facebook Ad Library queries, public identifiers, and collection parameters are sent to SocQ.

Mitigation: Use the skill only for data you are comfortable processing through SocQ's hosted tools and limit submitted inputs to the requested public research scope.

Risk: The skill requires a SocQ API key that may consume credits.

Mitigation: Keep `SOCQ_API_KEY` in the environment, avoid placing it in prompts, URLs, shared files, or retained commands, and confirm expected cost before large-volume or multi-endpoint runs.

Risk: Results can be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Report pages read, remaining data indicators, failed requests, unsupported filters, and incomplete coverage instead of claiming completeness.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [Facebook Ad Library Platform Page](https://socq.ai/apis/facebook-ad-library)
- [Facebook Ad Library API Documentation](https://docs.socq.ai/api-manual/facebook-ad-library)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Facebook Ad Library Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with endpoint summaries, command or API guidance, task status, credit usage, result counts, normalized findings, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination state, incomplete-coverage notes, failed request details, and unsupported-filter warnings.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
