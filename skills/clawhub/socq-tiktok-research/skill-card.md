## Description:

Research public TikTok content, accounts, keywords, and performance data with SocQ. Use when an agent needs TikTok-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research teams use this skill to collect, page through, and summarize public TikTok profiles, videos, comments, hashtags, search results, transcripts, and trend data through SocQ tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends public TikTok research queries and the configured SocQ API key to SocQ's hosted service.

Mitigation: Install only when that data flow is intended, keep SOCQ_API_KEY in the environment, avoid putting keys in prompts or URLs, and consider API key IP, rate, and credit limits.

Risk: SocQ requests are credit-metered, and large or multi-endpoint jobs may spend credits.

Mitigation: Check account balance and endpoint billing before large jobs, estimate expected cost, reduce result limits when needed, and obtain confirmation before paid large-volume runs.

Risk: TikTok collection may be incomplete when pagination stops early, provider failures occur, or requested filters are unsupported.

Mitigation: Preserve task IDs, inspect normalized errors before retrying, report result counts and pages read, and label incomplete coverage or unsupported filters.

## Reference(s):

- [SocQ TikTok Research Skill](https://clawhub.ai/socq/skills/socq-tiktok-research)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ TikTok Platform](https://socq.ai/apis/tiktok)
- [SocQ TikTok API Documentation](https://docs.socq.ai/api-manual/tiktok)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [TikTok Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with endpoint selections, command examples, task status, credit usage, pagination notes, and normalized findings or raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should report selected endpoint, execution path, task ID, terminal status, result count, pages read, remaining data, collection time, unsupported filters, and incomplete coverage.]

## Skill Version(s):

1.0.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
