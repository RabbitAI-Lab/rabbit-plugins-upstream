## Description:

Research public Google Maps content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external agents use this skill to select SocQ Google Maps endpoints, estimate paid usage, run authenticated collection tasks, and summarize public place, review, or search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a SocQ API key for paid Google Maps research, so unauthorized scope or key exposure could create cost and access risk.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid putting it in prompts or URLs, confirm trust in SocQ before installation, and use credit limits or IP allowlists where available.

Risk: Large-volume or multi-endpoint runs can consume paid SocQ credits.

Mitigation: Estimate credits, inspect account limits, reduce result limits when appropriate, and require user confirmation before large paid runs.

Risk: Provider failures, unsupported filters, or early pagination stops can make collected data incomplete.

Mitigation: Report task status, pages read, remaining pagination, failed requests, unsupported filters, and incomplete coverage clearly in the final result.

## Reference(s):

- [SocQ platform homepage](https://socq.ai/)
- [SocQ Google Maps API documentation](https://docs.socq.ai/api-manual/google-maps)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ agent skill guide](https://docs.socq.ai/integrations/skill)
- [SocQ devtools](https://github.com/SocQAPI/socq-devtools)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [Google Maps](references/platform.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, text, markdown]

**Output Format:** [Markdown summaries with endpoint choices, command or API examples, task status, credit usage, and normalized findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination state, raw export locations, unsupported filters, and incomplete coverage notes.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
