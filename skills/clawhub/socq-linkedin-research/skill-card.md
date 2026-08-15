## Description:

Research public LinkedIn content, accounts, keywords, and performance data with SocQ. Use when an agent needs LinkedIn-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect and analyze public LinkedIn companies, profiles, jobs, posts, comments, and searches through SocQ. It helps agents select the right endpoint, estimate credits, run asynchronous tasks, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn research targets, queries, URLs, filters, and related request parameters are sent to SocQ's hosted service.

Mitigation: Avoid including confidential internal context unless it is necessary for the research task.

Risk: SocQ requests are credit-metered and large or multi-endpoint runs can spend credits.

Mitigation: Estimate expected cost, check account limits when needed, and obtain user confirmation before paid large-volume or multi-endpoint runs.

Risk: Incomplete pagination, provider failures, unsupported filters, or failed tasks can produce partial coverage.

Mitigation: Report task status, pages read, whether more data remains, failed requests, unsupported filters, and incomplete coverage.

Risk: Authentication material can be exposed if API keys are placed in prompts, URLs, commands, or committed files.

Mitigation: Keep SOCQ_API_KEY in the environment and do not put keys in prompts, URLs, retained commands, or committed files.

## Reference(s):

- [SocQ LinkedIn Research on ClawHub](https://clawhub.ai/socq/skills/socq-linkedin-research)
- [SocQ CLI and MCP Homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ LinkedIn Platform](https://socq.ai/apis/linkedin)
- [SocQ LinkedIn API Documentation](https://docs.socq.ai/api-manual/linkedin)
- [SocQ MCP and CLI Integration](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [LinkedIn Endpoint Reference](references/platform.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint summaries, task status, credit usage, normalized findings, raw export locations, and inline commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCQ_API_KEY and either the SocQ MCP server, socq CLI, npx @socq/cli, or REST fallback.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
