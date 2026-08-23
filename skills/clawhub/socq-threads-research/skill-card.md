## Description:

Research public Threads content, accounts, keywords, and performance data with SocQ using endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external agents use this skill to collect and analyze public Threads posts, profiles, and user posts via SocQ while preserving inputs, estimating credits, handling asynchronous tasks, pagination, and normalized outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if placed in prompts, URLs, command history, or committed files.

Mitigation: Keep SOCQ_API_KEY in the process environment or local SocQ auth, and do not include credentials in prompts, URLs, retained commands, or files.

Risk: SocQ requests are credit-metered, and large or multi-endpoint jobs can spend credits unexpectedly.

Mitigation: Review endpoint billing, check account status, report expected cost, and obtain confirmation before large or multi-endpoint runs.

Risk: Results can be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Report pages read, result counts, remaining pagination, provider errors, unsupported filters, and any incomplete coverage.

Risk: Blind retries can duplicate paid work or obscure the original task state.

Mitigation: Inspect normalized errors, preserve task IDs, reuse idempotency keys after network failures, and avoid resubmitting failed paid requests automatically.

Risk: The skill could be misapplied to unsupported or non-public Threads data collection.

Mitigation: Use only SocQ-supported public Threads endpoints and ask for missing required inputs rather than inventing parameters.

## Reference(s):

- [SocQ Threads API documentation](https://docs.socq.ai/api-manual/threads)
- [SocQ Threads platform page](https://socq.ai/apis/threads)
- [SocQ MCP and CLI overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [SocQ devtools homepage](https://github.com/SocQAPI/socq-devtools)
- [Threads endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous tasks](references/async-tasks.md)
- [Pagination and files](references/pagination.md)
- [Errors and recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with concise findings, endpoint and execution details, optional shell commands, task status, credit usage, pagination notes, and raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, credit estimates, normalized result counts, pagination status, and raw JSONL export locations.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
