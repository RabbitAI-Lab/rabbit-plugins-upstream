## Description:

Research public Amazon content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to choose SocQ Amazon endpoints, estimate credit costs, run public Amazon data collection, and summarize normalized results or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ API keys may be exposed if placed in prompts, URLs, committed files, retained commands, or command history.

Mitigation: Keep SOCQ_API_KEY in the environment and prefer environment-based authentication over command-line API-key flags.

Risk: SocQ requests are credit-metered, and large or multi-endpoint runs can spend credits unexpectedly.

Mitigation: Review endpoint cost, check account limits, estimate expected credits, and obtain confirmation before paid large-volume or multi-endpoint execution.

Risk: Results may be incomplete when pagination stops early, a provider fails, or a requested filter is unsupported.

Mitigation: Report pages read, whether more data remains, failed requests, unsupported filters, and incomplete coverage instead of claiming completeness.

## Reference(s):

- [SocQ developer tools homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platforms](https://socq.ai/platforms)
- [SocQ Amazon API documentation](https://docs.socq.ai/api-manual/amazon)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Amazon endpoint reference](artifact/references/platform.md)
- [Authentication](artifact/references/authentication.md)
- [Billing and cost control](artifact/references/billing.md)
- [Asynchronous tasks](artifact/references/async-tasks.md)
- [Pagination and files](artifact/references/pagination.md)
- [Errors and recovery](artifact/references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with endpoint details, command or API guidance, task status, credit usage, result counts, and optional raw JSONL export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCQ_API_KEY; paid or large multi-endpoint runs should be confirmed before execution.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
