## Description:

Research public YouTube content, accounts, keywords, and performance data with SocQ. Use when an agent needs YouTube-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to collect and analyze public YouTube data through SocQ endpoints, including searches, channel and video lookups, comments, transcripts, playlists, Shorts, live videos, and community posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a SocQ API key.

Mitigation: Keep SOCQ_API_KEY in the environment, do not place keys in prompts, URLs, committed files, or retained commands, and review API-key limits before use.

Risk: SocQ requests are credit-metered and large or multi-endpoint jobs may spend credits.

Mitigation: Check expected endpoint costs and account limits, reduce scope when needed, and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: YouTube collections may be incomplete when pagination stops early, a provider fails, transcripts are unavailable, or filters are unsupported.

Mitigation: Report endpoint scope, pages read, remaining pagination, failures, unsupported filters, and whether results cover only a subset of requested content.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ YouTube API](https://socq.ai/apis/youtube)
- [SocQ YouTube API Documentation](https://docs.socq.ai/api-manual/youtube)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [YouTube Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with endpoint summaries, task status, normalized findings, raw export locations, and inline command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, credit estimates and usage, result counts, pagination status, collection time, and notes about incomplete coverage.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
