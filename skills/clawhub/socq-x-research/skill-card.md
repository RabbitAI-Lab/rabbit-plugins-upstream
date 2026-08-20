## Description:

Research public X content, accounts, keywords, and performance data with SocQ. Use when an agent needs X-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent operators use this skill to plan, run, and report public X research through SocQ endpoints, including endpoint selection, cost estimates, asynchronous task polling, pagination, and normalized findings or raw exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public X research inputs and SocQ API-authenticated requests are sent to SocQ.

Mitigation: Avoid confidential, regulated, or unnecessary personal context in searches and use the skill only when that external API use is acceptable.

Risk: The skill depends on a SocQ API key for CLI, MCP, and REST access.

Mitigation: Keep the key in the environment, out of prompts, URLs, committed files, and shell history.

Risk: SocQ tasks can consume credits, especially for large-volume or multi-endpoint runs.

Mitigation: Check expected cost, set credit limits where possible, and confirm large paid runs before starting.

Risk: Search visibility, pagination limits, unsupported filters, or provider failures can make coverage incomplete.

Mitigation: Report collection time, endpoint choice, pages read, remaining pagination, failed requests, unsupported filters, and incomplete coverage.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ X API Documentation](https://docs.socq.ai/api-manual/x)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [X Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown with endpoint selections, CLI/MCP/REST commands, JSON task references, and normalized result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, credit estimates, pagination status, collection time, and raw export locations when available.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
