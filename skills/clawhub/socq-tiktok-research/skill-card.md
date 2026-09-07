## Description:

Research public TikTok content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect, compare, and analyze public TikTok content, profiles, comments, followers, hashtags, trends, live-room metadata, videos, and transcripts through SocQ. It helps an agent select endpoints, estimate credits, submit asynchronous tasks, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends public TikTok research queries and the SocQ API key to SocQ for MCP, CLI, or REST execution.

Mitigation: Install only when SocQ data collection is intended, keep SOCQ_API_KEY in the environment, and do not place keys in prompts, URLs, committed files, or retained commands.

Risk: SocQ requests are credit-metered, and large-volume or multi-endpoint runs can spend account credits.

Mitigation: Estimate endpoint costs, check account limits, set spending ceilings on API keys, and require confirmation before large paid collection.

Risk: Using npx at runtime can increase package supply-chain exposure.

Mitigation: Prefer a pinned or preinstalled @socq/cli package for tighter control.

Risk: Follower, following, transcript, and profile collection can raise privacy or platform-rule concerns even when data is public.

Mitigation: Use these endpoints only for legitimate public-data research with appropriate privacy and platform-rule review.

Risk: Pagination limits, provider failures, unsupported filters, or unfinished asynchronous tasks can create incomplete coverage.

Mitigation: Track task IDs, poll to a terminal status, preserve opaque cursors, report pages read and remaining data, and label incomplete or unsupported coverage.

## Reference(s):

- [SocQ TikTok Research Skill](https://clawhub.ai/socq/skills/socq-tiktok-research)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
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

**Output Format:** [Markdown with endpoint summaries, task status, credit details, normalized findings, and optional raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include the selected endpoint and execution path, input and filter summary, credit usage when available, task ID and terminal status, result count, pages read, and incomplete coverage notes.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
