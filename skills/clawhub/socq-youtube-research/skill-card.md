## Description:

Research public YouTube content, accounts, keywords, and performance data with SocQ through endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to discover, collect, compare, and analyze public YouTube videos, channels, comments, transcripts, Shorts, playlists, and community posts with SocQ. It helps select the right endpoint, estimate credits, run MCP or CLI collection, handle asynchronous tasks and pagination, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SOCQ_API_KEY could be exposed through prompts, URLs, shell history, committed files, or retained commands.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid URL and prompt exposure, and use scoped keys with rate, IP, and credit limits where possible.

Risk: Large-volume or multi-endpoint runs can consume paid SocQ credits.

Mitigation: Read endpoint billing details, report expected cost, check account limits, and obtain confirmation before expensive runs.

Risk: Using unpinned npx execution can introduce normal supply-chain uncertainty.

Mitigation: Prefer a vetted or pinned @socq/cli version for repeatable operational use.

Risk: Results can be incomplete or misleading when pagination stops early, a provider fails, or requested filters are unsupported.

Mitigation: Preserve task IDs, follow pagination, inspect normalized errors, and clearly label incomplete coverage or unsupported filters.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ YouTube Platform](https://socq.ai/apis/youtube)
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

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown guidance with endpoint selections, MCP or CLI calls, status summaries, and normalized findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, credit estimates, pagination state, result counts, and raw export locations.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
