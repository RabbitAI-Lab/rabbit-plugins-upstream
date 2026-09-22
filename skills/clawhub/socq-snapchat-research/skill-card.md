## Description:

Collect and analyze public Snapchat profiles, Spotlight items, and Spotlight comments through SocQ's MCP, CLI, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, analysts, and developers use this skill to select SocQ Snapchat endpoints, estimate credit use, submit public data collection tasks, poll asynchronous results, handle pagination, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends public Snapchat research requests and the SOCQ_API_KEY to SocQ's hosted service.

Mitigation: Install only when this hosted SocQ integration is intended, keep SOCQ_API_KEY in the environment, and avoid putting keys in prompts, URLs, command history, or committed files.

Risk: SocQ requests are credit-metered, and large or multi-endpoint runs can spend account credits.

Mitigation: Check account balance and endpoint pricing, prefer spend limits on the API key, reduce scope when needed, and confirm large paid runs before submission.

Risk: Public Snapchat collections may be incomplete when pagination stops early, providers fail, filters are unsupported, or public counters change over time.

Mitigation: Report collection time, endpoint scope, pages read, whether more data remains, failed requests, unsupported filters, and any incomplete coverage.

## Reference(s):

- [SocQ devtools repository](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platforms](https://socq.ai/platforms)
- [SocQ Snapchat API documentation](https://docs.socq.ai/api-manual/snapchat)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [Snapchat endpoint registry](references/platform.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown, JSON]

**Output Format:** [Markdown guidance with SocQ MCP, CLI, or REST commands and normalized result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, input summary, expected and reported credit usage, task ID and terminal status, result counts, pagination status, collection time, incomplete coverage notes, and raw export locations.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
