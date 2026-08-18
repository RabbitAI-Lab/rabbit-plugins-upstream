## Description:

Guides agents through SocQ endpoint selection, task execution, pagination, and reporting for public Truth Social profiles, posts, and user timelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to collect and analyze public Truth Social account, post, and timeline data through SocQ while managing authentication, credits, asynchronous tasks, pagination, and coverage reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocQ API key for CLI, MCP, and REST access.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid placing keys in prompts, URLs, commands retained in history, or committed files, and use key-level controls when available.

Risk: SocQ requests are credit-metered and large or multi-endpoint runs can spend credits.

Mitigation: Review expected costs and scope before submission, use account or API-key credit limits where possible, and obtain confirmation before large paid runs.

Risk: Truth Social collection may be incomplete because pagination can stop early, providers can fail, requested filters may be unsupported, and available endpoints do not cover general keyword search, follower graphs, or thread expansion.

Mitigation: Report pages read, whether more data remains, unsupported filters, provider failures, deleted or unavailable posts, and other coverage gaps with the findings.

## Reference(s):

- [SocQ Truth Social API documentation](https://docs.socq.ai/api-manual/truth-social)
- [SocQ MCP and CLI integration overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [SocQ platform page](https://socq.ai/platforms)
- [SocQ devtools](https://github.com/SocQAPI/socq-devtools)
- [Truth Social endpoint reference](references/platform.md)
- [Authentication](references/authentication.md)
- [Billing and Cost Control](references/billing.md)
- [Asynchronous Tasks](references/async-tasks.md)
- [Pagination and Files](references/pagination.md)
- [Errors and Recovery](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with optional inline shell commands and raw export references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes selected endpoint, execution path, input summary, credit usage, task status, result counts, pagination state, and coverage gaps.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
