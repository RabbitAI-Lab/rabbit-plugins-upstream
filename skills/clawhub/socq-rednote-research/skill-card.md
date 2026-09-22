## Description:

Research public Rednote content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to select and run SocQ endpoints for public Rednote research. It helps agents estimate credits, submit asynchronous collection tasks, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rednote queries, URLs, user IDs, and the SOCQ_API_KEY are sent to SocQ during use.

Mitigation: Use this skill only when that data sharing is acceptable, keep SOCQ_API_KEY in the environment, and avoid placing secrets in prompts, URLs, command history, or committed files.

Risk: SocQ requests are credit-metered and larger or multi-endpoint runs can incur unexpected cost.

Mitigation: Review endpoint billing, check account balance or limits, estimate expected credits, and obtain confirmation before paid large-volume runs.

Risk: Pagination, provider failures, unsupported filters, or point-in-time recommendation samples can produce incomplete or non-comparable research coverage.

Mitigation: Report pages read, whether more data remains, failed requests, unsupported filters, collection time, and differences in windows, filters, locales, or content types.

Risk: Using an unpinned npx fallback can execute a moving version of the SocQ CLI.

Mitigation: Prefer a pinned or locally installed SocQ CLI when MCP is unavailable.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Rednote API documentation](https://docs.socq.ai/api-manual/rednote)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [SocQ platform page](https://socq.ai/platforms)
- [Rednote endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint selection, execution path, credit estimate, task status, pagination summary, normalized findings, and raw export locations when applicable.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ MCP, CLI, or REST command guidance; task IDs and partial coverage notes are retained so interrupted research can resume without duplicate paid submissions.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
