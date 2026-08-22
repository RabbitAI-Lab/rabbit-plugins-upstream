## Description:

Research public Google Ad Library content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research agents use this skill to discover, collect, compare, and analyze public Google Ad Library data through SocQ endpoints. It helps select endpoints, estimate credits, submit asynchronous tasks, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ receives the user's Google Ad Library research queries and uses SOCQ_API_KEY for network requests.

Mitigation: Keep SOCQ_API_KEY in the environment or SocQ auth config, never place it in prompts or URLs, and avoid retaining commands that expose credentials.

Risk: Requests are credit-metered, and large or multi-endpoint collections can incur unexpected cost.

Mitigation: Check account limits and endpoint billing, estimate credits, reduce scope when needed, and obtain confirmation before large paid collections.

Risk: Asynchronous tasks, pagination limits, provider failures, or unsupported filters can produce incomplete coverage.

Mitigation: Preserve task IDs, poll to terminal status, follow cursor pagination, and clearly label early stops, failures, unsupported filters, and incomplete results.

## Reference(s):

- [SocQ website](https://socq.ai/)
- [SocQ platforms](https://socq.ai/platforms)
- [SocQ Google Ad Library API documentation](https://docs.socq.ai/api-manual/google-ad-library)
- [SocQ integrations overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [SocQ devtools](https://github.com/SocQAPI/socq-devtools)
- [Async tasks](references/async-tasks.md)
- [Authentication](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Errors and recovery](references/errors.md)
- [Pagination and files](references/pagination.md)
- [Google Ad Library endpoint reference](references/platform.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown, text]

**Output Format:** [Markdown guidance with inline commands, endpoint choices, task status, credit usage, normalized findings, and optional raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, pagination state, result counts, collection time, unsupported filters, failed requests, and incomplete coverage notices.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
