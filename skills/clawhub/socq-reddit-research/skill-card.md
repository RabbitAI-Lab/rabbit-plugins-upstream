## Description:

Research public Reddit content, accounts, keywords, and performance data with SocQ. Use when an agent needs Reddit-specific discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to select SocQ Reddit endpoints, estimate and control credits, submit asynchronous collection tasks, paginate results, and report normalized public Reddit research findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SocQ API keys can be exposed through prompts, URLs, shell history, or committed files.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid putting keys in prompts or URLs, prefer local configuration for interactive use, and clear credentials when no longer needed.

Risk: Reddit queries, URLs, task metadata, and retrieved results are processed by SocQ.

Mitigation: Use the skill only when SocQ processing is acceptable and collect only public data supported by the selected endpoint.

Risk: Large or repeated Reddit collection jobs can consume paid credits or hit API-key credit limits.

Mitigation: Inspect endpoint billing, check account balance or limits, reduce result scope where possible, and obtain confirmation before paid large-volume or multi-endpoint runs.

Risk: Ad hoc npx execution can make CLI behavior less reproducible.

Mitigation: Prefer a vetted or pinned @socq/cli version for repeatable workflows.

Risk: Pagination stops, provider failures, unsupported filters, or differing date windows can make findings incomplete or incomparable.

Mitigation: Preserve task IDs and cursors, stop only at the requested cap or terminal pagination state, label incomplete coverage, and describe differences in filters, windows, locale, or content type.

## Reference(s):

- [SocQ devtools](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ Reddit API documentation](https://docs.socq.ai/api-manual/reddit)
- [SocQ Reddit platform page](https://socq.ai/apis/reddit)
- [SocQ MCP and CLI integrations](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Reddit endpoint reference](artifact/references/platform.md)
- [Authentication](artifact/references/authentication.md)
- [Billing and cost control](artifact/references/billing.md)
- [Asynchronous tasks](artifact/references/async-tasks.md)
- [Pagination and files](artifact/references/pagination.md)
- [Errors and recovery](artifact/references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with endpoint summaries, command or API call guidance, task status, credit usage, result counts, normalized findings, and raw export locations when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination state, incomplete-coverage notes, failed request details, unsupported filters, and cost information.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
