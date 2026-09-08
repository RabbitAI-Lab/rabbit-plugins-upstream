## Description:

Research public Instagram content, accounts, keywords, and performance data with SocQ. Use when an agent needs Instagram-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use this skill to select SocQ Instagram endpoints, estimate credits, run MCP, CLI, or REST collections, poll asynchronous tasks, page through results, and report normalized public Instagram findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Instagram account names, URLs, keywords, filters, and related query parameters are sent to SocQ's hosted service.

Mitigation: Use the skill only for authorized public Instagram research, avoid sensitive or regulated investigation targets unless authorized, and disclose relevant collection limits in the final report.

Risk: The required SOCQ_API_KEY can grant paid API access and may be exposed through prompts, URLs, shell history, or retained commands if handled carelessly.

Mitigation: Keep the key in the environment, use a scoped key with IP allowlists plus spending and rate limits, and avoid passing the key directly in prompts, URLs, committed files, or routine CLI flags.

Risk: SocQ requests are credit-metered, and large or multi-endpoint jobs can create unexpected cost.

Mitigation: Check expected endpoint cost and account limits before submission, reduce scope when needed, and obtain user confirmation before paid large-volume or multi-endpoint runs.

Risk: Pagination stopping early, provider failures, unsupported filters, or mixed date windows can make reported findings incomplete or misleading.

Mitigation: Track task IDs and cursors, report pages read and whether more data remains, inspect normalized errors before retrying, and label differences in date windows, filters, locales, or content types.

Risk: Ad hoc npx execution can fetch changing CLI code at runtime.

Mitigation: Prefer a pinned or preinstalled SocQ CLI when possible and use npx only when the environment has no configured CLI.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Instagram Platform](https://socq.ai/apis/instagram)
- [SocQ Instagram API Documentation](https://docs.socq.ai/api-manual/instagram)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Instagram Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Markdown, JSON]

**Output Format:** [Markdown guidance with inline commands, endpoint identifiers, task status, credit usage, result summaries, and optional JSON or JSONL export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, input summary, task ID, terminal status, result count, pages read, remaining pagination state, failed requests, unsupported filters, and incomplete coverage notes.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
