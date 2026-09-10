## Description:

Research public Google Maps content, accounts, keywords, and performance data with SocQ, including endpoint selection, credit estimates, asynchronous execution, pagination, and raw exports through the SocQ CLI, MCP, or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[socq](https://clawhub.ai/user/socq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to collect and analyze public Google Maps place, review, and search data through SocQ while handling authentication, cost checks, asynchronous task polling, pagination, and exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocQ API key and uses external SocQ services for public Google Maps research.

Mitigation: Keep SOCQ_API_KEY in the environment, avoid putting secrets in prompts, URLs, committed files, or retained commands, and install the skill only when SocQ service use is intended.

Risk: SocQ requests are credit-metered, and large-volume or multi-endpoint runs can spend credits.

Mitigation: Check expected costs and account limits before large runs, reduce scope when needed, and obtain confirmation before paid large-volume or multi-endpoint execution.

Risk: Results may be incomplete when pagination stops early, a provider fails, filters are unsupported, or collection settings differ.

Mitigation: Report pagination status, failed requests, unsupported filters, collection time, and coverage caveats; label comparisons that use different windows, filters, locales, or content types.

## Reference(s):

- [SocQ devtools homepage](https://github.com/SocQAPI/socq-devtools)
- [SocQ website](https://socq.ai/)
- [SocQ platforms](https://socq.ai/platforms)
- [Google Maps API documentation](https://docs.socq.ai/api-manual/google-maps)
- [SocQ MCP and CLI integration overview](https://docs.socq.ai/integrations/overview)
- [SocQ Agent Skill guide](https://docs.socq.ai/integrations/skill)
- [Platform reference](references/platform.md)
- [Authentication reference](references/authentication.md)
- [Billing and cost control reference](references/billing.md)
- [Asynchronous tasks reference](references/async-tasks.md)
- [Pagination and files reference](references/pagination.md)
- [Errors and recovery reference](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with endpoint selections, concise summaries, inline shell commands, task status, credit usage, result counts, normalized findings, and raw export locations when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SocQ task IDs, pagination state, terminal task status, failed request notes, unsupported filter notes, and incomplete coverage caveats.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
