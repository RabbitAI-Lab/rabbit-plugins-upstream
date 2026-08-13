## Description:

Research public X content, accounts, keywords, and performance data with SocQ. Use when an agent needs X-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external agents use this skill to select and run SocQ endpoints for public X research, including account, post, trend, conversation, and network collection. It guides endpoint choice, authentication, credit checks, asynchronous task polling, pagination, and concise reporting of normalized results or raw exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: X search terms, account names, post URLs, WOEIDs, and task requests are sent to SocQ.

Mitigation: Use the skill only for public X data supported by the selected endpoint, preserve user-approved scope, and avoid exposing credentials in prompts, URLs, commands, or retained files.

Risk: SocQ requests may consume account credits, especially broad, paginated, or multi-endpoint collection jobs.

Mitigation: Review estimated costs, check account limits, reduce scope when needed, and require confirmation before large paid runs.

Risk: X search, trend, and relationship data can be incomplete or point-in-time.

Mitigation: Report collection time, pages read, unsupported filters, failures, and whether more data remains; avoid claiming exhaustive coverage when pagination stops early or provider behavior limits visibility.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ X Platform](https://socq.ai/apis/x)
- [SocQ X API Documentation](https://docs.socq.ai/api-manual/x)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Asynchronous Tasks](references/async-tasks.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Errors and Recovery](references/errors.md)
- [Pagination and Files](references/pagination.md)
- [X Endpoint Selection](references/platform.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, command examples, task status, result counts, and normalized findings or raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, credit estimates and usage, collection time, pagination status, unsupported filters, failed requests, and incomplete coverage notes.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
