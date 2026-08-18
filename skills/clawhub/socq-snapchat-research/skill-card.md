## Description:

Research public Snapchat content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external research teams use this skill to collect public Snapchat profile, Spotlight, and Spotlight comment data through SocQ while preserving endpoint choice, costs, task status, pagination, and collection context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party paid SocQ API and can spend credits on larger or multi-endpoint Snapchat collection jobs.

Mitigation: Confirm expected costs and account limits before large runs, reduce scope when needed, and avoid retrying failed paid requests without inspecting the normalized error.

Risk: The workflow requires a SOCQ_API_KEY, which could be exposed if included in prompts, URLs, shell history, or committed files.

Mitigation: Keep the API key in the environment or configured SocQ auth, avoid command-line key arguments during interactive use, and never persist credentials in task notes or source files.

Risk: Snapchat results may be incomplete or time-sensitive when pagination stops early, a provider fails, or public counters and comments change.

Mitigation: Report collection time, pagination state, failed requests, unsupported filters, and incomplete coverage instead of claiming completeness.

## Reference(s):

- [SocQ devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platforms](https://socq.ai/platforms)
- [Snapchat API documentation](https://docs.socq.ai/api-manual/snapchat)
- [SocQ API key dashboard](https://socq.ai/dashboard/api-key)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Snapchat profile endpoint](https://docs.socq.ai/api-manual/snapchat/profile)
- [Snapchat Spotlight endpoint](https://docs.socq.ai/api-manual/snapchat/spotlight)
- [Snapchat Spotlight comments endpoint](https://docs.socq.ai/api-manual/snapchat/spotlight-comments)
- [Platform reference](references/platform.md)
- [Authentication reference](references/authentication.md)
- [Billing reference](references/billing.md)
- [Async tasks reference](references/async-tasks.md)
- [Pagination reference](references/pagination.md)
- [Errors reference](references/errors.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown, JSON]

**Output Format:** [Markdown guidance with command examples, endpoint selections, task status summaries, and JSON or JSONL export references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports selected endpoint, execution path, input scope, expected and reported credit use, task ID, terminal status, result count, pagination state, collection time, unsupported filters, and incomplete coverage.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
