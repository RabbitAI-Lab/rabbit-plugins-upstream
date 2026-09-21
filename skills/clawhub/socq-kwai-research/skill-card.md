## Description:

Research public Kwai content, accounts, keywords, and performance data with SocQ. Use when an agent needs Kwai-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to collect and analyze public Kwai posts, profiles, and user-post pages through SocQ. It guides endpoint selection, authentication, credit checks, asynchronous task polling, pagination, and normalized reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends requested Kwai research inputs to SocQ and may consume SocQ credits.

Mitigation: Confirm scope and expected cost before large-volume or multi-endpoint runs, and reduce result limits when the user has not authorized larger spend.

Risk: SOCQ_API_KEY could be exposed through prompts, URLs, committed files, retained commands, or shell history.

Mitigation: Keep the key in the environment, avoid API keys in prompts or URLs, and prefer configured MCP or CLI authentication.

Risk: Results may be incomplete or misleading if pagination stops early, a provider fails, or requested filters are unsupported.

Mitigation: Report task status, pages read, remaining pagination state, failed requests, unsupported filters, and any incomplete coverage.

## Reference(s):

- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Kwai API Documentation](https://docs.socq.ai/api-manual/kwai)
- [SocQ Integrations Overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill Guide](https://docs.socq.ai/integrations/skill)
- [Kwai Endpoint Reference](artifact/references/platform.md)
- [Authentication](artifact/references/authentication.md)
- [Billing and Cost Control](artifact/references/billing.md)
- [Asynchronous Tasks](artifact/references/async-tasks.md)
- [Pagination and Files](artifact/references/pagination.md)
- [Errors and Recovery](artifact/references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with endpoint summaries, command snippets, task status, cost details, normalized findings, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference SocQ task IDs, pagination cursors, credit usage, terminal status, and incomplete coverage notes.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
