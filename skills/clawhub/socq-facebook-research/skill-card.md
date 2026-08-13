## Description:

Research public Facebook content, accounts, keywords, and performance data with SocQ endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent operators use this skill to select and run SocQ Facebook endpoints for public Facebook discovery, collection, comparison, and analysis. It supports workflows that estimate credit cost, submit asynchronous tasks, poll results, paginate output, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SocQ as an external service for Facebook research.

Mitigation: Avoid submitting confidential, regulated, or unusually sensitive investigation targets unless the user has authorization.

Risk: SocQ requests are credit-metered, and large or multi-endpoint collection runs can incur meaningful cost.

Mitigation: Report expected cost and obtain user confirmation before large-volume or multi-endpoint paid runs.

Risk: Public data collection may be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Label incomplete coverage, preserve task IDs for resumable polling, and avoid claiming completeness when collection did not finish.

Risk: The skill requires a SocQ API key.

Mitigation: Keep SOCQ_API_KEY in the environment and do not place keys in prompts, URLs, committed files, or retained commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/socq/skills/socq-facebook-research)
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Facebook Platform Page](https://socq.ai/apis/facebook)
- [SocQ Facebook API Documentation](https://docs.socq.ai/api-manual/facebook)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Facebook Endpoint Reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [guidance, text, markdown, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown guidance with MCP, CLI, or REST execution details and normalized research summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected output may include selected endpoint, execution path, input summary, credit usage, task ID, terminal status, result counts, pagination status, normalized findings, raw export location, failed requests, unsupported filters, and incomplete coverage notes.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
