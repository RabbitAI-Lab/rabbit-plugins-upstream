## Description:

Research public Google Play content, accounts, keywords, and performance data with SocQ through endpoint selection, credit estimates, asynchronous task execution, pagination, and raw exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to collect and analyze public Google Play app details, rankings, and reviews through SocQ MCP, CLI, or REST API workflows. It helps choose endpoints, estimate credit usage, submit and poll asynchronous tasks, handle pagination, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Google Play research inputs and SocQ authentication to SocQ's hosted service.

Mitigation: Use it only for intended SocQ workflows, keep SOCQ_API_KEY in the environment, avoid putting keys in prompts, URLs, committed files, or retained commands, and use API-key IP, rate, or credit limits where available.

Risk: Ad hoc npx execution can install or run an unpinned @socq/cli version.

Mitigation: Prefer a preinstalled or pinned @socq/cli version before running collection workflows.

Risk: Large or multi-endpoint SocQ jobs can consume credits.

Mitigation: Check expected endpoint costs, account balance, and key limits before submission, then obtain user confirmation for paid large-volume or multi-endpoint runs.

Risk: Incomplete pagination, provider failures, unsupported filters, or differing date windows can lead to misleading conclusions.

Mitigation: Report result counts, pages read, remaining pagination, failed requests, unsupported filters, collection time, and any differences in date windows, filters, locales, or content types.

## Reference(s):

- [SocQ skill page](https://clawhub.ai/socq/skills/socq-google-play-research)
- [SocQ devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platforms](https://socq.ai/platforms)
- [Google Play API documentation](https://docs.socq.ai/api-manual/google-play)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Authentication](references/authentication.md)
- [Billing and cost control](references/billing.md)
- [Asynchronous tasks](references/async-tasks.md)
- [Pagination and files](references/pagination.md)
- [Errors and recovery](references/errors.md)
- [Google Play platform reference](references/platform.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, configuration, guidance]

**Output Format:** [Markdown with endpoint selections, command or API examples, task metadata, result summaries, and optional raw export locations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected endpoint, execution path, input and filter summary, expected and reported credit usage, task ID, terminal status, result count, pages read, pagination status, normalized findings, failed requests, unsupported filters, and incomplete coverage notes.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
