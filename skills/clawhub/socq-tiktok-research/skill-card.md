## Description:

Research public TikTok content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external research agents use this skill to select SocQ TikTok endpoints, estimate credits, submit asynchronous public-data collection tasks, poll for completion, paginate results, and summarize normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SOCQ_API_KEY is required for CLI, MCP, and REST authentication.

Mitigation: Keep the key in the process environment, avoid prompts, URLs, shell history, committed files, and retained commands, and review key restrictions such as IP allowlists or credit limits.

Risk: SocQ requests are credit-metered, and larger or multi-endpoint jobs can consume paid credits.

Mitigation: Check expected costs and account limits before submission, reduce scope when needed, and obtain user confirmation before paid large-volume or multi-endpoint runs.

Risk: TikTok collection can be incomplete when pagination stops early, providers fail, filters are unsupported, or task polling is interrupted.

Mitigation: Track task IDs, paginate only to the requested or approved cap, report terminal status and incomplete coverage, and do not claim completeness without evidence.

Risk: The skill targets public TikTok research and may implicate account limits or compliance requirements.

Mitigation: Collect only public data supported by the selected endpoint and confirm the requested collection fits the user's account limits and compliance needs.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ TikTok API Documentation](https://docs.socq.ai/api-manual/tiktok)
- [SocQ TikTok Platform](https://socq.ai/apis/tiktok)
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

**Output Format:** [Markdown guidance with inline shell commands, endpoint choices, task status, credit usage, result summaries, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected SocQ execution path, normalized public TikTok findings, pagination status, incomplete coverage notes, and cost information.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
