## Description:

Research public Douyin content, accounts, keywords, and performance data with SocQ for endpoint selection, credit estimates, asynchronous task execution, pagination, and exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research analysts use this skill to collect and analyze public Douyin profiles, videos, comments, live room details, product data, and search results through SocQ while tracking costs, pagination, and task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin research targets, keywords, URLs, and collection parameters to SocQ.

Mitigation: Use it only for public Douyin research that is approved for SocQ processing, and avoid sensitive private research topics unless SocQ is approved for that data.

Risk: The skill requires a SOCQ_API_KEY in the agent environment.

Mitigation: Keep the API key in environment or approved local configuration, avoid placing it in prompts, URLs, committed files, or retained commands, and use key rate, credit, or IP limits where available.

Risk: SocQ requests are credit-metered and large or multi-endpoint runs can incur cost.

Mitigation: Estimate expected credits, check account limits, reduce scope where needed, and obtain confirmation before paid large-volume or multi-endpoint execution.

Risk: Pagination, provider failures, unsupported filters, or early stopping can lead to incomplete coverage.

Mitigation: Track task IDs and pagination cursors, report pages read and whether more data remains, and label unsupported filters or incomplete coverage in the final result.

## Reference(s):

- [SocQ Developer Tools](https://github.com/SocQAPI/socq-devtools)
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

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI, MCP, or REST execution details and normalized research summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, input summary, expected and reported credit usage, task ID, terminal status, result count, pages read, raw export location, and caveats about incomplete coverage.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
