## Description:

Research public Douyin content, accounts, keywords, and performance data with SocQ through endpoint selection, credit estimates, asynchronous execution, pagination, and raw exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and analysts use this skill to collect, compare, and analyze public Douyin profiles, videos, comments, live rooms, and product data through SocQ. It helps an agent choose the correct endpoint, submit and poll asynchronous tasks, manage pagination, and report normalized results or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SOCQ_API_KEY for authenticated SocQ requests, so accidental key exposure could grant access to the user's SocQ account.

Mitigation: Keep the key in the process environment or local SocQ configuration, avoid placing it in prompts, URLs, committed files, or shell history, and use API-key controls such as IP allowlists and rate limits when available.

Risk: SocQ requests may spend credits, especially for large, paginated, or multi-endpoint Douyin collection jobs.

Mitigation: Check account balance and endpoint billing before submission, set account or key-level spending limits where needed, and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: A task may fail, time out, or return incomplete coverage when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Preserve task IDs, inspect normalized errors before retrying, report incomplete coverage, and do not resubmit paid failed tasks blindly.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Douyin API Documentation](https://docs.socq.ai/api-manual/douyin)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Douyin Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with endpoint summaries, task status, credit usage, normalized findings, and optional raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, filters, result counts, pagination status, task ID, and incomplete coverage notes.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
