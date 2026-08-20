## Description:

Research public Facebook content, accounts, keywords, and performance data with SocQ. Use when an agent needs Facebook-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to select and run SocQ Facebook endpoints for public content discovery, collection, comparison, and analysis. It helps estimate credits, submit asynchronous tasks, poll for results, paginate responses, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocQ API key for CLI, MCP, and REST requests.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid putting keys in prompts, URLs, committed files, or retained shell commands, and review API-key allowlists and rate or credit limits before use.

Risk: SocQ requests are credit-metered, and large or multi-endpoint jobs can consume paid credits.

Mitigation: Review endpoint billing, check account limits, reduce result scope where appropriate, and confirm large-volume or multi-endpoint runs before submission.

Risk: Submitted collections are asynchronous, so a successful submission is not a completed collection.

Mitigation: Save the task ID, poll until a terminal status is returned, and resume polling rather than resubmitting when a request is still queued or running.

Risk: Results may be incomplete when pagination stops early, provider errors occur, or requested filters are unsupported.

Mitigation: Track pages read, preserve cursors as opaque values, report failed requests or unsupported filters, and avoid claiming complete coverage when collection limits or errors remain.

## Reference(s):

- [SocQ website](https://socq.ai/)
- [SocQ Facebook platform page](https://socq.ai/apis/facebook)
- [SocQ Facebook API documentation](https://docs.socq.ai/api-manual/facebook)
- [SocQ MCP and CLI documentation](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [SocQ devtools homepage](https://github.com/SocQAPI/socq-devtools)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)
- [Facebook](references/platform.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown, text]

**Output Format:** [Markdown guidance with inline JSON, CLI commands, task identifiers, result summaries, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCQ_API_KEY and access to SocQ MCP, CLI, or REST endpoints; requests may be asynchronous and credit-metered.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
