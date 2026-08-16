## Description:

Research public ads, advertisers, creatives, and campaign activity with SocQ for Facebook Ad Library discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and agents use this skill to collect and analyze public Facebook Ad Library data with SocQ. It helps choose the right endpoint, preserve filters and date ranges, estimate credit usage, submit and poll asynchronous tasks, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ requests require an API key, and exposing the key in prompts, URLs, command history, or committed files could compromise authenticated access.

Mitigation: Keep SOCQ_API_KEY in the environment or SocQ auth config, avoid command-line key arguments during interactive use, and never include the key in prompts, URLs, committed files, or retained commands.

Risk: Large-volume, multi-endpoint, or retried jobs may consume credits.

Mitigation: Estimate expected cost, check account limits when needed, reduce scope for uncertain inputs, and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: Results may be incomplete if pagination stops early, a provider fails, a task is still queued or running, or a requested filter is unsupported.

Mitigation: Preserve task IDs, poll until a terminal status, follow opaque cursors only to the requested cap, and clearly report incomplete coverage, unsupported filters, failed requests, and remaining pages.

Risk: Blindly resubmitting failed or interrupted paid requests can duplicate work or spend.

Mitigation: Inspect normalized errors before retrying, reuse idempotency keys after network failures, and resume polling existing task IDs instead of automatically creating duplicate tasks.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Website](https://socq.ai/)
- [SocQ Facebook Ad Library Platform](https://socq.ai/apis/facebook-ad-library)
- [SocQ Facebook Ad Library API Documentation](https://docs.socq.ai/api-manual/facebook-ad-library)
- [SocQ MCP and CLI Documentation](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Asynchronous Tasks](references/async-tasks.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Errors and Recovery](references/errors.md)
- [Pagination and Files](references/pagination.md)
- [Facebook Ad Library Endpoint Selection](references/platform.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or text with commands and structured result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoints, execution path, task IDs, credit usage, result counts, pagination status, normalized findings, and raw export locations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
