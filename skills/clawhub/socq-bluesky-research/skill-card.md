## Description:

Research public Bluesky content, accounts, keywords, and performance data with SocQ through Bluesky-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to collect, paginate, and report on public Bluesky posts and profiles through SocQ. It helps select endpoints, estimate credits, run asynchronous tasks, handle errors, and return normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SOCQ_API_KEY for SocQ CLI, MCP, and REST requests.

Mitigation: Keep the key in environment configuration and do not place it in prompts, URLs, committed files, or retained commands.

Risk: SocQ requests may spend credits, especially for large-volume or multi-endpoint Bluesky collection.

Mitigation: Review expected cost and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: Results can be incomplete when pagination stops early, a provider fails, or a filter is unsupported.

Mitigation: Report pagination status, failures, unsupported filters, and coverage limits with the findings.

Risk: The skill is intended for public Bluesky data collection.

Mitigation: Avoid using it for private or unsupported data collection.

## Reference(s):

- [SocQ devtools homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platforms](https://socq.ai/platforms)
- [SocQ Bluesky API documentation](https://docs.socq.ai/api-manual/bluesky)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Bluesky endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous tasks](references/async-tasks.md)
- [Pagination and files](references/pagination.md)
- [Errors and recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, cost notes, task status, normalized findings, and shell or API command examples when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, pagination status, credit usage, incomplete coverage notes, and raw export locations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
