## Description:

Research public TikTok content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external agents use this skill to select SocQ TikTok endpoints, estimate credits, submit asynchronous collection tasks, paginate results, and report normalized public TikTok findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ API access is required for public TikTok collection workflows.

Mitigation: Keep SOCQ_API_KEY in the environment or SocQ auth storage, never place keys in prompts or URLs, and verify API-key policies such as allowlists and rate limits before running collections.

Risk: Broad or multi-endpoint collection can spend SocQ credits.

Mitigation: Review endpoint costs and account balance, reduce result limits when needed, and obtain user confirmation before large-volume or multi-endpoint paid runs.

Risk: Pagination, provider failures, unsupported filters, or task failures can make results incomplete.

Mitigation: Preserve task IDs, poll asynchronous tasks to a terminal state, follow cursors until the requested cap or completion, and clearly label incomplete coverage or unsupported filters.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ TikTok Platform Page](https://socq.ai/apis/tiktok)
- [SocQ TikTok API Documentation](https://docs.socq.ai/api-manual/tiktok)
- [SocQ MCP and CLI Integration Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [TikTok Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, command or tool guidance, task status, credit usage, normalized findings, and optional raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination status, incomplete coverage notes, failed request details, and unsupported filter disclosures.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
