## Description:

Research public Linkedin Ad Library content, accounts, keywords, and performance data with SocQ. Use when an agent needs Linkedin Ad Library-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to collect, compare, and analyze public LinkedIn Ad Library records through SocQ endpoints while preserving query filters, pagination state, task status, and cost context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn Ad Library queries, public ad URLs, filters, and task requests are sent to SocQ under the configured SOCQ_API_KEY and may consume credits.

Mitigation: Keep SOCQ_API_KEY in the environment, report expected costs, check account or endpoint billing details, and get user confirmation before paid large-volume or multi-endpoint runs.

Risk: Using npx to resolve @socq/cli can introduce supply-chain drift from the latest published package.

Mitigation: Use a preinstalled or pinned @socq/cli package when stricter supply-chain control is required.

Risk: Pagination stops, provider failures, unsupported filters, or failed asynchronous tasks can leave research incomplete.

Mitigation: Preserve task IDs, poll to a terminal status, follow next_cursor exactly, and label incomplete coverage, failed requests, unsupported filters, and remaining pages in the final output.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ LinkedIn Ad Library API Documentation](https://docs.socq.ai/api-manual/linkedin-ad-library)
- [SocQ MCP and CLI Integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Linkedin Ad Library Platform Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, API calls, configuration]

**Output Format:** [Markdown with endpoint summaries, task status, credit usage, normalized findings, and optional shell commands or raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports result counts, pages read, whether more data remains, unsupported filters, failed requests, and incomplete coverage when applicable.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
