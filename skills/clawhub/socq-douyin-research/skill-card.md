## Description:

Research public Douyin content, accounts, keywords, and performance data with SocQ through endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use this skill to collect, page through, and summarize public Douyin account, video, comment, product, and live-room data through SocQ. It is suited for workflows that need endpoint selection, paid credit estimates, task polling, normalized findings, or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin queries, task metadata, and API-key-authenticated requests to SocQ.

Mitigation: Use it only when SocQ is trusted for the requested research data, and keep SOCQ_API_KEY in the environment rather than prompts, URLs, commands, or committed files.

Risk: Unpinned CLI execution can introduce supply-chain exposure.

Mitigation: Prefer a preinstalled or version-pinned socq CLI, and review package provenance before running npx in automation.

Risk: Large or repeated collections can consume paid SocQ credits.

Mitigation: Check the estimated cost and account limits first, set API-key spending limits, and require approval before large-volume or multi-endpoint runs.

Risk: Pagination stops, provider failures, or unsupported filters can produce incomplete coverage.

Mitigation: Report pages read, remaining cursors, failed requests, unsupported filters, and any early stopping instead of claiming complete coverage.

## Reference(s):

- [SocQ devtools homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platform page](https://socq.ai/platforms)
- [SocQ Douyin API documentation](https://docs.socq.ai/api-manual/douyin)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Douyin platform reference](references/platform.md)
- [Authentication reference](references/authentication.md)
- [Billing and cost control reference](references/billing.md)
- [Asynchronous task reference](references/async-tasks.md)
- [Pagination and files reference](references/pagination.md)
- [Error handling reference](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with endpoint details, command or tool arguments, task status, credit usage, normalized findings, and optional raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCQ_API_KEY and a configured SocQ MCP server or CLI; SocQ requests are asynchronous and credit-metered.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
