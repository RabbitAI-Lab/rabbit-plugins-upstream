## Description:

Research public Threads content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to select and run SocQ Threads endpoints for public Threads discovery, collection, comparison, and analysis. It supports endpoint selection, input validation, credit estimates, asynchronous task execution, pagination, and normalized or raw exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ runs require an API key and may consume credits.

Mitigation: Keep SOCQ_API_KEY in the environment or SocQ config, avoid exposing it in prompts or command history, report expected cost, and get confirmation before large paid collections.

Risk: Collection results can be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Report pages read, whether more data remains, failed requests, unsupported filters, and incomplete coverage instead of claiming completeness.

## Reference(s):

- [SocQ devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Threads platform](https://socq.ai/apis/threads)
- [SocQ Threads API documentation](https://docs.socq.ai/api-manual/threads)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Threads endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration, Markdown, JSON]

**Output Format:** [Markdown with inline commands and structured result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, input summary, credit usage, task ID, terminal status, result counts, pagination status, normalized findings, raw export location, and incomplete coverage notes.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
