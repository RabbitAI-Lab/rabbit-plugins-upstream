## Description:

Research public Google Ad Library content, accounts, keywords, and performance data with SocQ when an agent needs discovery, collection, endpoint selection, credit estimates, asynchronous task execution, pagination, or raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to discover, collect, compare, and analyze public Google Ad Library data through SocQ. It helps choose Google Ad Library endpoints, validate inputs, estimate credits, run asynchronous collection tasks, paginate results, and report normalized findings or raw export locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A SocQ API key is required and could be exposed if placed in prompts, URLs, shell history, committed files, or retained commands.

Mitigation: Keep SOCQ_API_KEY in the environment or local SocQ configuration, avoid API keys in URLs and prompts, and redact credentials from commands and reports.

Risk: Broad collection, multi-endpoint runs, and high result limits can consume credits unexpectedly.

Mitigation: Check account balance and endpoint billing before submission, estimate expected cost, reduce scope when needed, and get user confirmation before paid large-volume work.

Risk: Asynchronous or paginated collection can be incomplete when tasks fail, polling stops early, a provider fails, or more pages remain.

Mitigation: Preserve task IDs, poll to a terminal status, treat cursors as opaque, report pages read and whether more data remains, and label incomplete coverage clearly.

Risk: Raw task exports may contain larger payloads than the summarized output.

Mitigation: Use the standard result view by default, request raw JSONL exports only when needed, and tell users when output is summarized rather than complete raw data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/socq/skills/socq-google-ad-library-research)
- [SocQ developer tools](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platforms](https://socq.ai/platforms)
- [SocQ Google Ad Library API documentation](https://docs.socq.ai/api-manual/google-ad-library)
- [SocQ MCP and CLI integration overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Google Ad Library ad endpoint](https://docs.socq.ai/api-manual/google-ad-library/ad)
- [Google Ad Library advertiser search endpoint](https://docs.socq.ai/api-manual/google-ad-library/advertiser-search)
- [Google Ad Library company ads endpoint](https://docs.socq.ai/api-manual/google-ad-library/company-ads)
- [Google Ad Library platform reference](references/platform.md)
- [Authentication reference](references/authentication.md)
- [Billing and cost control reference](references/billing.md)
- [Asynchronous task reference](references/async-tasks.md)
- [Pagination and file export reference](references/pagination.md)
- [Error handling reference](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown with endpoint summaries, execution steps, task status, result counts, normalized findings, and optional raw export locations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, pagination state, expected and reported credit usage, collection timing, unsupported filters, failed requests, and incomplete coverage notes.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
