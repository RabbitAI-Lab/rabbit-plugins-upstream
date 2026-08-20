## Description:

Research public YouTube content, accounts, keywords, and performance data with SocQ. Use when an agent needs YouTube-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to plan and run credit-metered research on public YouTube videos, channels, comments, transcripts, Shorts, playlists, and community posts through SocQ.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a SocQ API key for CLI, MCP, and REST access.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid putting it in prompts, URLs, committed files, or retained shell commands, and verify API-key access controls before use.

Risk: SocQ requests are credit-metered and large or multi-endpoint jobs can consume paid credits.

Mitigation: Review expected credit costs, check account limits, reduce scope where appropriate, and obtain confirmation before paid large-volume runs.

Risk: Asynchronous collections may be incomplete, fail, or have additional pages remaining.

Mitigation: Preserve task IDs, poll to a terminal status, follow pagination cursors, and report failed requests, unsupported filters, provider failures, and incomplete coverage.

Risk: Raw exports and task outputs can contain research data that should not be shared beyond the intended use.

Mitigation: Retrieve raw files only when needed, treat exports as scoped research artifacts, and share them only with the intended audience.

## Reference(s):

- [SocQ Devtools Repository](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ YouTube API Platform](https://socq.ai/apis/youtube)
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

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with endpoint choices, command examples, task status, result summaries, and raw export locations when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, page counts, credit estimates, normalized public YouTube findings, and incomplete-coverage notes.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
