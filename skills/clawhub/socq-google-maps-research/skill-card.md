## Description:

Research public Google Maps content, accounts, keywords, and performance data with SocQ through MCP, CLI, or REST workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to select SocQ Google Maps endpoints, estimate credits, submit and poll asynchronous collection tasks, paginate results, and summarize normalized public place or review data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocQ API key for MCP, CLI, or REST access.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid placing keys in prompts, URLs, committed files, or retained commands, and use account-side limits where appropriate.

Risk: SocQ requests are credit-metered and large or multi-endpoint jobs may spend credits.

Mitigation: Estimate expected cost before submission, reduce result caps when scope is uncertain, and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: Raw exports may contain public place or review information from the requested Google Maps collection.

Mitigation: Treat raw exports as data files, collect only public data supported by the selected endpoint, and report unsupported filters or incomplete coverage.

Risk: Results can be incomplete when pagination stops early, a provider fails, or a task remains unfinished.

Mitigation: Preserve task IDs, poll asynchronous tasks to a terminal status, follow opaque cursors, and disclose failed requests, pages read, and whether more data remains.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/socq/skills/socq-google-maps-research)
- [SocQ developer tools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Google Maps API documentation](https://docs.socq.ai/api-manual/google-maps)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [Platform endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous tasks](references/async-tasks.md)
- [Pagination and files](references/pagination.md)
- [Errors and recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with MCP, CLI, or REST execution details and JSON/result-file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoints, input summaries, credit estimates, task IDs, terminal status, result counts, pagination state, normalized findings, and raw export locations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
