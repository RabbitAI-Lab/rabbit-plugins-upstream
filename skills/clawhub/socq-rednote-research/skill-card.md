## Description:

Research public Rednote content, accounts, keywords, and performance data with SocQ.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research agents use this skill to collect, compare, and report on public Rednote notes, creators, comments, keywords, and performance data through SocQ. It helps select endpoints, estimate credit use, run asynchronous tasks, handle pagination, and produce normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ requests require an API key, and credentials could be exposed if placed in prompts, URLs, commands, or committed files.

Mitigation: Keep SOCQ_API_KEY in the environment or local SocQ configuration, avoid command-line API key flags during interactive use, and do not print or persist credentials.

Risk: Rednote collection is credit-metered, so large or multi-endpoint runs can consume paid credits.

Mitigation: Estimate endpoint costs, check account limits where available, reduce scope for uncertain inputs, and obtain user confirmation before large paid runs.

Risk: Results can be incomplete or misleading when pagination stops early, a provider fails, a filter is unsupported, or collection windows differ.

Mitigation: Report task status, pages read, result counts, remaining data, failed requests, unsupported filters, collection time, and any differences in collection windows or content types.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/socq/skills/socq-rednote-research)
- [SocQ devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ Rednote API documentation](https://docs.socq.ai/api-manual/rednote)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Rednote endpoint reference](artifact/references/platform.md)
- [Authentication](artifact/references/authentication.md)
- [Billing and cost control](artifact/references/billing.md)
- [Asynchronous tasks](artifact/references/async-tasks.md)
- [Pagination and files](artifact/references/pagination.md)
- [Errors and recovery](artifact/references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown, Configuration]

**Output Format:** [Markdown with endpoint summaries, execution steps, credit notes, task status, normalized findings, and optional raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, pagination status, collection timing, incomplete coverage notes, and SOCQ_API_KEY setup guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
