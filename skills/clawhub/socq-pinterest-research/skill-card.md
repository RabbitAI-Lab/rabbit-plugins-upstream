## Description:

Research public Pinterest content, accounts, keywords, and performance data with SocQ through its CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to select SocQ Pinterest endpoints, estimate credit costs, submit public-data collection tasks, page through results, and report normalized Pinterest research findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocQ API key for CLI, MCP, and REST requests.

Mitigation: Keep SOCQ_API_KEY in the process environment and avoid placing the key in prompts, URLs, command arguments, shell history, or committed files.

Risk: Pinterest collection is credit-metered and broad or multi-endpoint jobs can spend account credits.

Mitigation: Review endpoint costs and account limits before submission, reduce scope when appropriate, and require confirmation before paid large-volume or multi-endpoint runs.

Risk: Asynchronous tasks, pagination limits, provider failures, or unsupported filters can produce incomplete coverage.

Mitigation: Preserve task IDs, poll to terminal status, follow pagination cursors, and clearly report failed requests, unsupported filters, and any incomplete coverage.

## Reference(s):

- [SocQ devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Pinterest platform page](https://socq.ai/apis/pinterest)
- [SocQ Pinterest API documentation](https://docs.socq.ai/api-manual/pinterest)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Pinterest endpoint reference](references/platform.md)
- [Authentication guidance](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous task handling](references/async-tasks.md)
- [Pagination and files](references/pagination.md)
- [Errors and recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown, Configuration]

**Output Format:** [Markdown with endpoint choices, command or API call guidance, task status, credit usage, normalized findings, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should label pagination coverage, unsupported filters, failed requests, and incomplete provider coverage.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
