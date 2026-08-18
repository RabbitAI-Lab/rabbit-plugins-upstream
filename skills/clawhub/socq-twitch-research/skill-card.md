## Description:

Research public Twitch content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to select SocQ Twitch endpoints, collect public channel profile and recorded-video data, estimate credits, manage asynchronous tasks, paginate results, and summarize normalized findings or raw exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public Twitch usernames, URLs, filters, and task requests are sent to SocQ and billed to a SocQ account.

Mitigation: Use a scoped SOCQ_API_KEY with rate, credit, and IP limits where possible, avoid sensitive prompt context, estimate credits, and confirm cost before broad collection runs.

Risk: Paid or asynchronous collection can be duplicated or misread if failed, queued, running, or paginated tasks are retried without checking status.

Mitigation: Preserve task IDs, reuse idempotency keys for retries, inspect normalized errors before resubmission, and report pagination limits or incomplete coverage.

## Reference(s):

- [SocQ devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platform overview](https://socq.ai/platforms)
- [SocQ Twitch API documentation](https://docs.socq.ai/api-manual/twitch)
- [SocQ integrations overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Twitch profile endpoint](https://docs.socq.ai/api-manual/twitch/profile)
- [Twitch user videos endpoint](https://docs.socq.ai/api-manual/twitch/user-videos)
- [Platform reference](references/platform.md)
- [Authentication reference](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous task reference](references/async-tasks.md)
- [Pagination and files reference](references/pagination.md)
- [Errors and recovery reference](references/errors.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, API calls]

**Output Format:** [Markdown guidance with inline commands, endpoint selections, task status, normalized findings, and raw export locations when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, input summary, credit usage, task ID, pagination status, collection time, unsupported filters, and incomplete coverage notes.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
