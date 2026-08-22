## Description:

Research public Truth Social content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research analysts use this skill to choose SocQ Truth Social endpoints, submit authenticated MCP, CLI, or REST collection tasks, estimate credit use, paginate results, and report public account, timeline, or post findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocQ API key for CLI, MCP, and REST workflows.

Mitigation: Store SOCQ_API_KEY in the environment, avoid putting keys in prompts, URLs, committed files, or shell-history-prone command arguments, and use SocQ authentication status checks when needed.

Risk: SocQ requests are credit-metered and large or multi-endpoint runs may spend credits.

Mitigation: Check account balance and endpoint costs, estimate expected credit usage, reduce scope when needed, and obtain confirmation before paid large-volume or multi-endpoint collection.

Risk: Truth Social collections can be incomplete when pagination stops early, provider errors occur, posts are unavailable, or requested filters are unsupported.

Mitigation: Report task status, pages read, remaining pagination, unsupported filters, failed requests, collection time, and coverage gaps instead of claiming complete results.

## Reference(s):

- [SocQ Truth Social Research on ClawHub](https://clawhub.ai/socq/skills/socq-truth-social-research)
- [SocQ developer tools homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platform page](https://socq.ai/platforms)
- [SocQ Truth Social API documentation](https://docs.socq.ai/api-manual/truth-social)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Authentication reference](references/authentication.md)
- [Billing and cost control reference](references/billing.md)
- [Async task reference](references/async-tasks.md)
- [Pagination and files reference](references/pagination.md)
- [Errors and recovery reference](references/errors.md)
- [Truth Social platform reference](references/platform.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, markdown]

**Output Format:** [Markdown guidance with inline commands, endpoint selections, task status summaries, and normalized findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, credit estimates, pagination status, raw export locations, and incomplete coverage notes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
